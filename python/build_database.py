
"""Build the ONCO-301 SQLite database from the SQL schema."""

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "sql" / "schema.sql"
DB = ROOT / "onco301.db"


def main():

    if not SCHEMA.exists():
        raise FileNotFoundError(f"Schema not found: {SCHEMA}")

    # Enable foreign key enforcement on this connection
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)

    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))

        subjects = [
            (
                "ONCO301-001", 52, "Female", "Asian",
                "HER2-negative metastatic breast cancer",
                1, "2026-07-15", "2026-07-17", "2026-07-20"
            ),
            (
                "ONCO301-002", 17, "Female", "Asian",
                "HER2-negative metastatic breast cancer",
                1, "2026-07-15", "2026-07-17", "2026-07-20"
            ),
        ]

        conn.executemany(
            """
            INSERT INTO demographics (
                subject_id, age, sex, race, primary_diagnosis,
                ecog_status, consent_date, enrollment_date,
                first_dose_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            subjects,
        )

        conn.execute(
            """
            INSERT INTO queries (
                query_id, subject_id, check_id, field_name,
                query_text, status, resolution, raised_date,
                resolved_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "QRY-001",
                "ONCO301-002",
                "DEM-002",
                "Age",
                "Please verify the subject's age against the source documentation.",
                "Open",
                None,
                "2026-08-31",
                None,
            ),
        )

        conn.commit()

        print("\nDATABASE BUILD SUCCESSFULLY")

        for table in (
            "demographics",
            "adverse_events",
            "labs",
            "tumor_response",
            "queries",
        ):
            count = conn.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]

            print(f"{table}: {count} rows")

        result = conn.execute(
            "SELECT query_id, check_id FROM queries WHERE query_id = ?",
            ("QRY-001",),
        ).fetchone()

        print("QRY-001:", result)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
