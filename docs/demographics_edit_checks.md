| Check ID | Field(s)        | Rule                                            | Expected result                   |
| -------- | --------------- | ----------------------------------------------- | --------------------------------- |
| DEM-001  | Subject ID      | Subject ID must not be blank                    | Raise query if missing            |
| DEM-002  | Age             | Age must be ≥18                                 | Raise query if age <18            |
| DEM-003  | Sex             | Value must be Female, Male, Other, or Unknown   | Raise query for invalid value     |
| DEM-004  | ECOG Status     | Value must be between 0 and 4                   | Raise query if outside range      |
| DEM-005  | Consent Date    | Consent Date must not be after Enrollment Date  | Raise query if violated           |
| DEM-006  | Enrollment Date | Enrollment Date must not be before Consent Date | Raise query if violated           |
| DEM-007  | Subject ID      | Subject ID must be unique                       | Raise query/duplicate discrepancy |
