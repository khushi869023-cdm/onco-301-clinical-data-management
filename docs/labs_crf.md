# Laboratory (LB) CRF Specification

**Domain type:** Repeating: one record per test, per visit, per subject.

| Field (CDASH name) | Type | Mandatory | Edit check |
|---|---|---|---|
| Subject ID | Text | Yes | Must already exist in Demographics (LAB-001) |
| Visit | Coded | Yes | Screening / C1D1 / Day 1 of each later cycle / End of Treatment |
| Test Code (LBTESTCD) | Coded | Yes | Must be on the approved panel (LAB-002) |
| Result (LBORRES) | Numeric | Yes | Must be physiologically plausible (LAB-003) |
| Unit (LBORRESU) | Coded | Yes | Must match the standard unit for the test (LAB-004) |
| Range Low (LBORNRLO) | Numeric | Yes | Lower limit of normal |
| Range High (LBORNRHI) | Numeric | Yes | Upper limit of normal |
| Normal Indicator (LBNRIND) | Coded | Yes | L / N / H; must agree with Result vs. range (LAB-005) |
| Collection Date (LBDTC) | Date | Yes | Must fall within the visit window (LAB-006) |

## Approved panel and standard units
| Test | Test code | Standard unit |
|---|---|---|
| Hemoglobin | HGB | g/dL |
| White blood cells | WBC | 10^9/L |
| Absolute neutrophil count | ANC | 10^9/L |
| Platelets | PLT | 10^9/L |
| Alanine aminotransferase | ALT | U/L |
| Aspartate aminotransferase | AST | U/L |
| Total bilirubin | BILI | mg/dL |
| Creatinine | CREAT | mg/dL |

**Note:** An out-of-range result with the correct indicator is valid data and is
not queried. A query is raised only when the indicator contradicts the result.