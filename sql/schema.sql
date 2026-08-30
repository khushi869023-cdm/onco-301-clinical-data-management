create table demographics (
    subject_id text primary key,
    age integer,
    sex text,
    race text,
    primary_diagnosis text,
    ecog_status integer,
    consent_date date,
    enrollment_date date

);

CREATE TABLE adverse_events (
    ae_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT,
    ae_term TEXT,
    ae_coded_term TEXT,
    onset_date TEXT,
    resolution_date TEXT,
    ctcae_grade INTEGER,
    serious TEXT,
    relationship TEXT,
    action_taken TEXT,
    outcome TEXT,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

CREATE TABLE labs (
    lab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT,
    visit TEXT,
    test_code TEXT,
    result REAL,
    unit TEXT,
    range_low REAL,
    range_high REAL,
    normal_indicator TEXT,
    collection_date TEXT,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);

CREATE TABLE tumor_response (
    response_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id TEXT,
    visit TEXT,
    assessment_date TEXT,
    sum_target_lesions REAL,
    response TEXT,
    new_lesions TEXT,
    confirmed TEXT,
    FOREIGN KEY (subject_id) REFERENCES demographics(subject_id)
);