# Adverse Events Edit Checks

| Check ID | Field(s) | Rule | Expected result |
|---|---|---|---|
| AE-001 | Subject ID | Must already exist in Demographics table | Reject/query if unknown subject |
| AE-002 | Verbatim Term | Must not be blank | Raise query if missing |
| AE-003 | Onset Date | Must be on or after first dose date | Raise query if violated |
| AE-004 | Resolution Date | If present, must be on or after Onset Date | Raise query if violated |
| AE-005 | CTCAE Grade | Must be 1–5 | Raise query if outside range |
| AE-006 | Serious (Y/N) | Must not be blank | Raise query if missing |
| AE-007 | Relationship | Must be one of: Not related / Unlikely / Possible / Probable / Definite | Raise query for invalid value |
| AE-008 | Outcome | If Outcome = Fatal, Serious must = Y | Raise query if contradiction |