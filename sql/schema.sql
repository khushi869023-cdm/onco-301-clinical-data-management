-- ONCO-301 Clinical Data Management Database
-- Schema v2
-- Note: no CHECK constraints on values like age or ECOG. Wrong values must
-- be able to enter the database so edit checks can flag them and raise queries.

PRAGMA foreign_keys = ON;

-- 1. DEMOGRAPHICS (non-repeating: one row per subject)
CREATE TABLE IF NOT EXISTS demographics (
    subject_id          TEXT PRIMARY KEY,
    age                 INTEGER,
    sex                 TEXT,
    race                TEXT,
    primary_diagnosis   TEXT,
    ecog_status         INTEGER,
    consent_date        DATE,
    enrollment_date     DATE,
    first_dose_date     DATE        -- reference date for AE-003
);

-- 2. ADVERSE EVENTS (repeating: many rows per subject)
CREATE TABLE IF NOT EXISTS adverse_events (
    ae_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id        TEXT NOT NULL,
    verbatim_term     TEXT,         -- AETERM
    meddra_pt         TEXT,         -- AEDECOD, filled after coding
    onset_date        DATE,         -- AESTDTC
    resolution_date   DATE,         -- AEENDTC, blank = ongoing
    ctcae_grade       INTEGER,      -- AESEV
    serious           TEXT,         -- AESER
    relationship      TEXT,         -- AEREL
    action_taken      TEXT,         -- AEACN
    outcome           TEXT,         -- AEOUT
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

-- 3. LABORATORY DATA (repeating)
CREATE TABLE IF NOT EXISTS labs (
    lab_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id        TEXT NOT NULL,
    visit             TEXT,
    test_code         TEXT,
    result            REAL,
    unit              TEXT,
    range_low         REAL,
    range_high        REAL,
    normal_indicator  TEXT,
    collection_date   DATE,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

-- 4. TUMOR RESPONSE (repeating)
CREATE TABLE IF NOT EXISTS tumor_response (
    assessment_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id          TEXT NOT NULL,
    assessment_date     DATE,       -- typo fixed
    sum_target_lesions  REAL,
    response            TEXT,
    new_lesions         TEXT,
    confirmed           TEXT,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

-- 5. QUERY MANAGEMENT
CREATE TABLE IF NOT EXISTS queries (
    query_id       TEXT PRIMARY KEY,
    subject_id     TEXT NOT NULL,
    check_id       TEXT NOT NULL,
    field_name     TEXT NOT NULL,
    query_text     TEXT NOT NULL,
    status         TEXT NOT NULL,   -- Open / Answered / Closed
    resolution     TEXT,
    raised_date    DATE NOT NULL,
    resolved_date  DATE,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);