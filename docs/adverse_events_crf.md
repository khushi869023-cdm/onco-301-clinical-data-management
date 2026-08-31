# Adverse Events (AE) CRF Specification

**Domain type:** Repeating — one record per adverse event, per subject.
A subject can have zero AE records, or several.

| Field (CDASH name) | Type | Mandatory | Edit check |
|---|---|---|---|
| Subject ID | Text | Yes | Must already exist in the Demographics table |
| Verbatim Term (AETERM) | Text | Yes | Free text — what the site actually reported |
| MedDRA Coded Term (AEDECOD) | Coded | Yes, post-coding | Must be a valid MedDRA Preferred Term |
| Onset Date (AESTDTC) | Date | Yes | Must be on or after first dose date |
| Resolution Date (AEENDTC) | Date | No (blank = ongoing) | If present, must be on or after Onset Date |
| CTCAE Grade (AESEV) | Coded (1–5) | Yes | Must be 1–5 only |
| Serious (AESER) | Coded (Y/N) | Yes | — |
| Relationship to Study Drug (AEREL) | Coded | Yes | Not related / Unlikely / Possible / Probable / Definite |
| Action Taken (AEACN) | Coded | Yes | None / Dose reduced / Interrupted / Discontinued |
| Outcome (AEOUT) | Coded | Yes | Recovered / Recovering / Not recovered / Recovered with sequelae / Fatal |

**Note:** If Outcome = Fatal, Serious must = Y — a fatal event is serious by definition, so a record claiming otherwise is a logic contradiction, not just missing data.