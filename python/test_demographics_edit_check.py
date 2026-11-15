
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "onco301.db"

conn = sqlite3.connect(DB)

try:
    results = conn.execute("""
        SELECT
            subject_id,
            age,
            CASE
                WHEN age < 18 THEN 'FAIL'
                ELSE 'PASS'
            END AS check_result
        FROM demographics
    """).fetchall()

    for record in results:
        print(record)

finally:
    conn.close()
