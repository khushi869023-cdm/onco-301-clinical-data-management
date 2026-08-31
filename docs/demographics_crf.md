| Field            | What it captures         |Data type   | Required? | Example |

| Subject ID       | Unique patient identifier| Text       | Yes  | ONCO301-001|
| Age              | Age at enrollment        | Integer    | Yes  | 52|
| Sex              | Biological sex           | Categorical| Yes  | Female |
| Race             | Race category            | Categorica | No   | Asian  |
| Primary Diagnosis| primary cancer diagnosis | Categorical/Text|Yes| HER2-negative metastatic breast cancer |
| ECOG Status      | Baseline performance status| Integer    | Yes       | 1  |
| Informed Consent Date| Date consent obtained | Date  | Yes | 2026-07-15  |
| Enrollment Date  | Date subject entered the trial| Date| Yes | 2026-07-17  |

#Field validation/Permitted Values

| Field | Permitted values / validation rule|
| --------------------- | -------------------------------------------------------------------------- |
| Subject ID| Unique identifier in format `ONCO301-###`                                  |
| Age| Integer; must be ≥18|
| Sex| Female / Male / Other / Unknown|
| Race| Asian / White / Black or African American / Other / Unknown / Not Reported |
| Primary Diagnosis| Must correspond to the trial's eligibility diagnosis     
| ECOG Status| Integer from 0–4|
| Informed Consent Date | Valid date; must not be after Enrollment Date|
| Enrollment Date| Valid date; must be on or after Informed Consent Date|
