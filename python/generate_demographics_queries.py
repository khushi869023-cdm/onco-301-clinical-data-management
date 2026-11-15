
import sqlite3
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "onco301.db"


def main():

    conn = sqlite3.connect(DB)

    try:
        failed_records = conn.execute("""
            SELECT subject_id, age
            FROM demographics
            WHERE age < 18
        """).fetchall()

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

            query_id = conn.execute("""
                SELECT COUNT(*) FROM queries
            """).fetchone()[0] + 1

            query_id = f"QRY-{query_id:03d}"

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

        conn.commit()

    finally:
        conn.close()


if __name__ == "__main__":
    main()
