# Tumor Response Edit Checks

| Check ID | Field(s) | Rule | Expected result |
|---|---|---|---|
| TR-001 | Subject ID | Must already exist in Demographics table | Reject/query if unknown subject |
| TR-002 | Assessment Date | Must fall within the scheduled visit window | Raise query if outside window |
| TR-003 | Sum of Target Lesions | Must be ≥0 | Raise query if negative |
| TR-004 | Response | Must be one of: CR / PR / SD / PD only | Raise query for invalid value |
| TR-005 | New Lesions + Response | If New Lesions = Y, Response must = PD | Raise query if contradiction |
| TR-006 | Confirmed | Only applicable if Response = CR or PR | Raise query if populated for another response |