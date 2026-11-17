
import sqlite3
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "onco301.db"


def generate_query_id(conn):

    conn.execute("""
        CREATE TABLE IF NOT EXISTS query_id_sequence (
            sequence_id INTEGER PRIMARY KEY CHECK (sequence_id = 1),
            last_number INTEGER NOT NULL
        )
    """)

    conn.execute("""
        INSERT OR IGNORE INTO query_id_sequence (
            sequence_id, last_number
        )
        SELECT 1, COALESCE(
            MAX(CAST(SUBSTR(query_id, 5) AS INTEGER)), 0
        )
        FROM queries
        WHERE query_id GLOB 'QRY-[0-9]*'
    """)

    conn.execute("""
        UPDATE query_id_sequence
        SET last_number = last_number + 1
        WHERE sequence_id = 1
    """)

    next_number = conn.execute("""
        SELECT last_number
        FROM query_id_sequence
        WHERE sequence_id = 1
    """).fetchone()[0]

    return f"QRY-{next_number:03d}"


def main():

    conn = sqlite3.connect(DB)

    try:
        # 1. Find subjects with age below 18 (DEM-002)
        failed_records = conn.execute("""
            SELECT subject_id, age
            FROM demographics
            WHERE age < 18
        """).fetchall()

        # 2. Diagnostic check for missing age
        missing_age_records = conn.execute("""
            SELECT subject_id
            FROM demographics
            WHERE age IS NULL
                OR TRIM(CAST(age AS TEXT)) = ''
        """).fetchall()

        print("DEM-002 records:", failed_records)
        print("Missing age records:", missing_age_records)

        # 3. Find missing DEM-010 dates
        missing_dem010_records = conn.execute("""
            SELECT subject_id, 'Consent Date' AS field_name
            FROM demographics
            WHERE consent_date IS NULL
                OR TRIM(CAST(consent_date AS TEXT)) = ''

            UNION ALL

            SELECT subject_id, 'Enrollment Date' AS field_name
            FROM demographics
            WHERE enrollment_date IS NULL
                OR TRIM(CAST(enrollment_date AS TEXT)) = ''

            UNION ALL

            SELECT subject_id, 'First Dose Date' AS field_name
            FROM demographics
            WHERE first_dose_date IS NULL
                OR TRIM(CAST(first_dose_date AS TEXT)) = ''
        """).fetchall()

        print("DEM-010 missing records:", missing_dem010_records)

        # 4. Process DEM-002 records
        for subject_id, age in failed_records:

            existing_query = conn.execute("""
                SELECT query_id
                FROM queries
                WHERE subject_id = ?
                AND check_id = 'DEM-002'
                AND status IN ('Open', 'Answered')
            """, (subject_id,)).fetchone()

            if existing_query:
                print(
                    f"Query already exists for {subject_id}: "
                    f"{existing_query[0]}"
                )
                continue

            query_id = generate_query_id(conn)

            conn.execute("""
                INSERT INTO queries (
                    query_id, subject_id, check_id,
                    field_name, query_text, status,
                    raised_date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                query_id,
                subject_id,
                "DEM-002",
                "Age",
                "Please verify the subject's age against source documentation.",
                "Open",
                date.today().isoformat()
            ))

            print(f"Generated query: {query_id} for {subject_id}")

        
        # 5. Process DEM-010 records
        for subject_id, field_name in missing_dem010_records:

            # Check whether an unresolved query already exists
            existing_query = conn.execute("""
                SELECT query_id
                FROM queries
                WHERE subject_id = ?
                AND check_id = 'DEM-010'
                AND field_name = ?
                AND status IN ('Open', 'Answered')
            """, (subject_id, field_name)).fetchone()

            if existing_query:
                print(
                    f"Query already exists for {subject_id} "
                    f"({field_name}): {existing_query[0]}"
                )
                continue

            # Generate a new query ID
            query_id = generate_query_id(conn)

            # Prepare neutral query text
            query_text = (
                f"Please verify the {field_name} against source "
                "documentation and provide the appropriate correction "
                "or clarification."
            )

            # Insert the new query
            conn.execute("""
                INSERT INTO queries (
                    query_id, subject_id, check_id,
                    field_name, query_text, status,
                    raised_date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                query_id,
                subject_id,
                "DEM-010",
                field_name,
                query_text,
                "Open",
                date.today().isoformat()
            ))

            print(
                f"Generated query: {query_id} "
                f"for {subject_id} ({field_name})"
            )

        # 6. Commit database changes
        conn.commit()

    finally:
        conn.close()


if __name__ == "__main__":
    main()
