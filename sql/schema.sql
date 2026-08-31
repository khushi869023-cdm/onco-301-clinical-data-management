-- ONCO-301 Clinical Data Management Database
-- Database schema

PRAGMA foreign_keys = ON;

-------------
-- 1. DEMOGRAPHICS
-------------


create table demographics (
    subject_id text primary key,
    age integer NOT NULL,
    sex text NOT NULL,
    race text,
    primary_diagnosis text NOT NULL,
    ecog_status integer NOT NULL,
    consent_date date NOT NULL,
    enrollment_date date NOT NULL,

);

-- 2. ADVERSE EVENTS

CREATE TABLE IF NOT EXISTS adverse_events (
    ae_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT NOT NULL,
    verbatim_term TEXT NOT NULL,
    onset_date DATE NOT NULL,
    resolution_date DATE NOT NULL,
    ctcae_grade INTEGER NOT NULL,
    serious TEXT NOT NULL,
    relationship TEXT NOT NULL,
    outcome TEXT NOT NULL,

    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

-- 3. LABORATORY DATA

CREATE TABLE IF NOT EXISTS  labs (
    lab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT NOT NULL,
    visit TEXT NOT NULL,
    test_code TEXT NOT NULL,
    result REAL NOT NULL,
    unit TEXT NOT NULL,
    range_low REAL,
    range_high REAL,
    normal_indicator TEXT NOT NULL,
    collection_date DATE NOT NULL,

    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

--4. TUMOR RESPONSE

CREATE TABLE IF NOT EXISTS tumor_response (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT NOT NULL,
    assesment_date DATE NOT NULL,
    sum_target_lesions REAL NOT NULL,
    response TEXT NOT NULL,
    new_lesions TEXT NOY NULL,
    confirmed TEXT,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);