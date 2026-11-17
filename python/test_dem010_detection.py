
import sqlite3

# Create a temporary in-memory database
conn = sqlite3.connect(":memory:")

conn.execute("""
    CREATE TABLE demographics (
        subject_id TEXT,
        consent_date DATE,
        enrollment_date DATE,
        first_dose_date DATE
    )
""")

# Insert one test subject with a missing consent date
conn.executemany("""
    INSERT INTO demographics
    VALUES (?, ?, ?, ?)
""", [
    ('TEST-001', None, '2026-07-17', '2026-07-20'),
    ('TEST-002', '2026-07-15', None, '2026-07-20'),
    ('TEST-003', '2026-07-15', '2026-07-17', None)
])

# Run DEM-010 detection
missing_records = conn.execute("""
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

print("DEM-010 test results:", missing_records)

conn.close()
