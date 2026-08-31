# Labs Edit Checks

| Check ID | Field(s) | Rule | Expected result |
|---|---|---|---|
| LAB-001 | Subject ID | Must already exist in Demographics table | Reject/query if unknown subject |
| LAB-002 | Test Code | Must match the approved lab panel list | Raise query for unrecognized test |
| LAB-003 | Result | Must be a plausible physiological value for that test | Raise query if implausible |
| LAB-004 | Unit | Must match the standard unit for that test | Raise query if mismatched |
| LAB-005 | Normal Indicator | Must agree with where Result falls vs. Range Low/High | Raise query if indicator contradicts actual result |
| LAB-006 | Collection Date | Must fall within the scheduled visit window | Raise query if outside window |