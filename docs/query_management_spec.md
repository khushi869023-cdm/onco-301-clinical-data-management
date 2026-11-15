# Query Management Specification

## 1. Purpose

This document defines the process for identifying, raising, tracking, resolving, and closing data discrepancies in the ONCO-301 clinical trial database.

## 2. Query Record Structure

Queries are maintained in the `queries` database table.

| Field | Description |
|---|---|
| query_id | Unique query identifier (QRY-###) |
| subject_id | Subject associated with the discrepancy |
| check_id | Edit check ID that triggered the query |
| field_name | Database field containing the discrepancy |
| query_text | Neutral question communicated to the site |
| status | Open, Answered, or Closed |
| resolution | Site response and action taken |
| raised_date | Date the query was raised |
| resolved_date | Date the query was closed |

## 3. Query Lifecycle

1. **Open:** An edit check identifies a discrepancy and the CDM team raises a query.
2. **Answered:** The site provides clarification or a correction supported by source documentation.
3. **Closed:** The correction is verified and the data passes the relevant edit check.
4. **Re-query:** If the response is inadequate or the discrepancy remains unresolved, the query is returned to the site for clarification. Its status remains Open until adequately answered.

## 4. Query Management Rules

- The CDM team must not modify clinical data based on assumptions or guesses.
- Data corrections must be performed by authorized site personnel using appropriate source documentation.
- Query text must remain neutral, clear, and non-leading.
- Each distinct discrepancy should generate an appropriate query.
- Duplicate queries for the same unresolved discrepancy should be avoided.
- Every data modification must be documented in the audit trail, including the old value, new value, user, date/time, and reason for change.
- Edit check IDs must never be renumbered or reused. Retired checks retain their original IDs.

## 5. Query Management Metrics

The following metrics will be implemented in future database reporting:

- Total number of open queries.
- Total number of closed queries.
- Query aging (days between query initiation and resolution).
- Number of queries generated per edit check ID.

## 6. Example: QRY-001

| Attribute | Value |
|---|---|
| Query ID | QRY-001 |
| Subject ID | ONCO301-002 |
| Check ID | DEM-002 |
| Field | Age |
| Recorded value | 17 |
| Validation rule | Subject age must be 18 years or older |
| Query text | Please verify the subject's age against the source documentation. |
| Status | Open |

**Expected action:** The site must verify the subject's age against the source documentation and provide an appropriate correction or explanation.