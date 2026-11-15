
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "onco301.db"

conn = sqlite3.connect(DB)

try:
    conn.execute("PRAGMA foreign_keys = ON")

    print(
        "Foreign keys enabled:",
        conn.execute("PRAGMA foreign_keys").fetchone()[0]
    )

    try:
        conn.execute(
            """
            INSERT INTO adverse_events
            (subject_id, verbatim_term)
            VALUES (?, ?)
            """,
            ("ONCO301-099", "Headache")
        )

        conn.commit()
        print("ERROR: Orphan AE was accepted")

    except sqlite3.IntegrityError as error:
        print("PASS: Orphan AE rejected")
        print("Reason:", error)
        conn.rollback()

finally:
    conn.close()
