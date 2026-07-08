# Course Planner: Import/Export - Reference {: #import_export_reference}

This page lists all error and warning messages as well as the detailed field rules of the [import wizard](Course_Planner_Import_Export.md). It is intended for people preparing larger or more complex imports.

## Object types and roles {: #enum_reference}

The "Object type" column in the Excel file uses the following fixed values:

| Value | Meaning |
|---|---|
| IMPL | Implementation |
| ELEM | Element |
| TMPL | Template |
| COURSE | Course |
| EVENT | Event |

The "Role" column in the "Memberships" sheet uses the following fixed values:

| Value | Meaning |
|---|---|
| PARTICIPANT | Participant |
| COACH | Coach |
| MASTER_COACH | Master coach |
| COURSE_OWNER | Course owner |
| ELEM_OWNER | Element owner |

The "Absences", "Calendar", and "Progress" fields accept the values "ON", "OFF", and (for elements and implementations) "DEFAULT".

[Back to top ^](#import_export_reference)

---

## Error and warning codes {: #errors_warnings_reference}

### Errors

| Code | Message |
|---|---|
| E1 | \<Column header\>: Insufficient permissions |
| E2 | \<Column header\>: Value required |
| E3 | \<Column header\>: Value not unique |
| E4 | \<Column header\>: \<value\> does not exist |
| E5 | \<Column header\>: This value cannot be changed |
| E6 | \<Column header\>: "\<value\>" is not a valid value |
| E7 | \<Column header\>: Value is too long |
| E8 | \<Column header\>: No corresponding parent element exists |
| E9 | \<Column header\>: Invalid format |
| E10 | \<Column header\>: Invalid period |
| E11 | \<Column header\>: Must be empty for this object type |
| E12 | The element type is not permitted as an implementation |
| E13 | The parent element must not have any child elements |
| E14 | The parent element must not have any child elements of this element type |
| E15 | The element must not have any content |
| E16 | The element can only contain 1 course/template |
| E17 | The element must not have a template |
| E19 | The learning resource has the wrong usage |
| E21 / E24 | \<Column header\>: Does not exist in "\<Sheet\>" |
| E22 | \<Column header\>: Cannot be imported due to errors in "\<Sheet\>" |
| E23 | \<Column header\>: Has been ignored in "\<Sheet\>" |
| E25 | Password: Must be empty for existing users |
| (no code) | On identifier conflicts during import: Both external references must be the same |
| (no code) | Account expiration: The date must be in the future |

### Warnings

| Code | Message |
|---|---|
| W1 | \<Column header\>: "\<value\>" is not a valid value. Change will not be applied |
| W2 | \<Column header\>: Value is too long and will be truncated accordingly |
| W3 | Element has been updated in the meantime |
| W4 | \<Column header\>: Invalid format. Change will not be applied |
| W5 | \<Column header\>: \<value\> does not exist. Change will not be applied |
| W7 | \<Column header\>: \<value\> has changed. Change will not be applied |

[Back to top ^](#import_export_reference)

---

## Field rules per sheet {: #attribute_rules}

### "Products" sheet {: #rules_products}

| Attribute | Mandatory | Updatable | Possible message |
|---|---|---|---|
| Title | Yes | Yes | E2 (empty), W2 (too long), change is detected |
| Ext. Ref. | Yes | No | E2 (empty), E3 (not unique), E7 (too long) |
| ORG - Ext. Ref. | Yes | No | E1 (no permission), E2 (empty), E4 (does not exist), E5 (value cannot be changed) |
| Absences | Yes | Yes | E2 (empty), E6 (not a valid value on creation), W1 (not a valid value on update), change is detected |
| Description | No | Yes | W2 (too long), change is detected |
| Last modified | No | No | W3 (element already updated since export) |

### "Implementations" sheet (IMPL / ELEM / TMPL / COURSE / EVENT) {: #rules_implementations}

| Attribute | Mandatory | Updatable | Possible message |
|---|---|---|---|
| PROD - Ext. Ref. | Yes | No | E2, E1, E4 |
| IMPL - Ext. Ref. | Yes | No | E2, E4 |
| Object type | Yes | No | E2, E6, E5 |
| Level | Yes (except IMPL) | No | E2, E5, E8 (no parent element for ELEM) |
| Title | Yes | Yes | E2, W2, change is detected |
| Ext. Ref. | Yes | No | E2, E7, E3 (depending on object type), additionally E1/E4/E19 for TMPL/COURSE |
| Status | Yes (except EVENT) | Yes | E2, E6, W1, change is detected |
| Date/Time Begin and End | Yes for EVENT | Yes | E2 (EVENT), E9 (invalid format), E10 (invalid period), W4, change is detected |
| Unit | Yes for EVENT | Yes | E2, E6, change is detected |
| REF - Ext. Ref. | Yes for EVENT with course | No | E2, E5, E4 |
| Location | No | Yes | W2, change is detected |
| ELEM Type - Ext. Ref. | Yes for IMPL/ELEM | No | E2, E3, E4 |
| Calendar / Absences / Progress | Yes for IMPL/ELEM/TMPL/COURSE | Yes | E2, E6, W1, change is detected |
| Subjects | No | Yes | E4 (on creation), W5 (on update), change is detected |
| Last modified | No | No | W3 |

**Additional structural rules** (depending on the configuration of the respective element type):

| Object type | Rule | Message on violation |
|---|---|---|
| IMPL | Element type must allow "Permitted as implementation" | E12 |
| ELEM | Element type with disabled "Composite type" must not have child elements | E13 |
| ELEM | Element type with defined subtypes may only have matching child elements | E14 |
| TMPL / COURSE | Element type without content does not allow assignment | E15 |
| TMPL / COURSE | Element may only be referenced by one course/template | E16 |
| TMPL | Element type with unlimited courses does not allow templates | E17 |
| EVENT | Element must reference a course | not found in code, see note above |

### "Memberships" sheet {: #rules_memberships}

| Attribute | Mandatory | Possible message |
|---|---|---|
| PROD - Ext. Ref. / IMPL - Ext. Ref. / Ext. Ref. | Yes | E2, E7, E1, additionally E21/E22/E23 on creation |
| Role | Yes | E2, E6 |
| Username | Yes | E2, additionally E21/E22/E23 on creation |

Memberships can only be newly created, not updated.

### "Users" sheet {: #rules_users}

| Attribute | Mandatory (on creation) | Possible message |
|---|---|---|
| Username | Yes | E2, E6, additionally E21/E22 on creation |
| First name | Yes | E2, E7, W7 (changed for existing users) |
| Last name | Yes | E2, E7, W7 |
| E-mail | Yes, unless the system setting "E-mail mandatory" is disabled | E2, E6, W7 |
| ORG affiliation | Yes | E2, E1, E4, W7 |
| Password | No | E25 (must be empty for existing users), E6 (invalid value on creation) |
| Account expiration | No | Must be in the future on creation, otherwise an error message; W7 on change to existing accounts |

Users can only be newly created, not updated.

[Back to top ^](#import_export_reference)

---

## Further information {: #further_information}

[Course Planner: Import / Export >](Course_Planner_Import_Export.md)<br>

[Back to top ^](#import_export_reference)
