# Demographics Edit Checks

| Check ID | Field(s) | Rule | Expected result |
|---|---|---|---|
| DEM-001 | Subject ID | Subject ID must not be blank | Raise query if missing |
| DEM-002 | Age | Age must be 18 or older | Raise query if age < 18 |
| DEM-003 | Sex | Must be Female, Male, Other or Unknown | Raise query for invalid value |
| DEM-004 | ECOG Status | Must be between 0 and 4 (valid scale) | Raise query if outside range |
| DEM-005 | Consent Date, Enrollment Date | Consent Date must be on or before Enrollment Date | Raise query if violated |
| DEM-006 | (Retired) | Duplicate of DEM-005. ID kept reserved, do not reuse | None |
| DEM-007 | Subject ID | Subject ID must be unique | Raise query/duplicate discrepancy |
| DEM-008 | ECOG Status | ECOG must be 0 or 1 at enrollment (protocol eligibility) | Raise query if ECOG is 2 or higher |
| DEM-009 | Enrollment Date, First Dose Date | First Dose Date must be on or after Enrollment Date | Raise query if violated |
| DEM-010 | Consent, Enrollment, First Dose Date | Must not be blank | Raise query if missing |