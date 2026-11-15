# Tumor Response (TR) CRF Specification

**Domain type:** Repeating: one record per tumor assessment, per subject.
Assessments follow RECIST 1.1 and are done about every 6 weeks.

| Field | Type | Mandatory | Edit check |
|---|---|---|---|
| Subject ID | Text | Yes | Must already exist in Demographics (TR-001) |
| Assessment Date | Date | Yes | Must fall within the scheduled visit window (TR-002) |
| Sum of Target Lesions (mm) | Numeric | Yes | Must be 0 or more (TR-003) |
| Response | Coded | Yes | CR / PR / SD / PD only (TR-004) |
| New Lesions | Coded (Y/N) | Yes | If Y, Response must be PD (TR-005) |
| Confirmed | Coded (Y/N) | No | Only applicable if Response is CR or PR (TR-006) |

## Response categories (RECIST 1.1)
| Code | Meaning |
|---|---|
| CR | Complete Response |
| PR | Partial Response |
| SD | Stable Disease |
| PD | Progressive Disease |

**Note:** Objective Response Rate (ORR) = subjects with CR or PR divided by all
subjects. A new lesion always means PD.