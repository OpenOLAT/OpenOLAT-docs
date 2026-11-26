# Course Planner: Import/Export - Reference {: #import_export_reference}

If the [import wizard](Course_Planner_Import_Export/index.md) shows an error or a warning for a cell, this page tells you what the message means and in which columns it can occur. The page lists the error and warning messages of the import wizard as well as the rules for each column of the Excel file. It is intended for people preparing larger or more complex imports.

## Fixed values and column prefixes {: #enum_reference}

Some column headers carry a prefix. It shows which object the reference relates to: "PROD" to the product, "IMPL" to the implementation, "ORG" to the organisation and "REF", for an event, to the course the event belongs to. The "Level" column contains the number of an element in the structure of its implementation. For courses, course templates and events it contains the number of the element they belong to.

The "Object type" column in the Excel file uses the following fixed values:

| Value | Meaning |
|---|---|
| IMPL | Implementation |
| ELEM | Element |
| TMPL | Course template |
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

The "Status" column uses the following values for implementations and elements (IMPL, ELEM):

| Value | Meaning |
|---|---|
| PREPARATION | Preparation |
| PROVISIONAL | Provisional |
| CONFIRMED | Confirmed |
| ACTIVE | Active |
| CANCELLED | Canceled |
| FINISHED | Finished |

For courses and course templates (COURSE, TMPL) it uses the status of the learning resource:

| Value | Meaning |
|---|---|
| PREPARATION | Preparation |
| REVIEW | Review |
| COACHPUBLISHED | Access for coach |
| PUBLISHED | Published |
| CLOSED | Finished |

Upper and lower case do not matter for the status. Events (EVENT) have no status.

The "Absences", "Calendar", and "Progress" columns accept the values "ON", "OFF", and (for elements and implementations) "DEFAULT". The "Unit" column of an event accepts a whole number from 0 to 12.

[To the top of the page ^](#import_export_reference)

---

## Error and warning codes {: #errors_warnings_reference}

The import wizard shows each message together with the column header of the affected cell. It does not show the codes in the "Code" column: they apply only on this page and connect the messages with the tables under [Column rules per sheet](#attribute_rules). The numbers are not consecutive.

With E4, the import finds no matching object for the value, neither in OpenOlat nor in the sheets of the file, for example no organisation with this reference. When OpenOlat checks a username, an e-mail address or a password, the message gives the reason in its own wording; these messages are not in the lists.

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
| E12 | ELEM Type - Reference: The element type is not permitted as an implementation |
| E13 | ELEM Type - Reference: The parent element must not have any child elements |
| E14 | ELEM Type - Reference: The parent element must not have any child elements of this element type |
| E15 | ELEM Type - Reference: The element must not have any content |
| E16 | ELEM Type - Reference: The element can only contain 1 course/template |
| E17 | ELEM Type - Reference: The element must not have a template |
| E19 | Object type: The learning resource has the wrong usage |
| E21 / E24 | \<Column header\>: Does not exist in "\<Sheet\>" |
| E22 | \<Column header\>: Cannot be imported due to errors in "\<Sheet\>" |
| E23 | \<Column header\>: Has been ignored in "\<Sheet\>" |
| E25 | Password: Must be empty for existing users |
| (no code) | IMPL - Reference: Both references must be the same |
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
| (no code) | Object type: The learning resource has the usage "Standalone". It is recommended to only use courses with the usage "Use in Course Planner". [:octicons-tag-16:{ title="from Release 20.3.1 (OO-9424)" }](https://track.frentix.com/issue/OO-9424){:target="_blank"} |

For W3, the import still applies the values from the file and overwrites the change in OpenOlat.

[To the top of the page ^](#import_export_reference)

---

## Column rules per sheet {: #attribute_rules}

For each column, the tables state whether it must be filled in, whether an import can change the value and which messages are possible. "Change is detected" is not a message: the wizard marks the changed cell and shows the old and the new value under "Change (old/new)".

### "Products" sheet [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9191)" }](https://track.frentix.com/issue/OO-9191){:target="_blank"} {: #rules_products}

| Column | Mandatory | Updatable | Possible message |
|---|---|---|---|
| Title | Yes | Yes | E2 (empty), W2 (too long), change is detected |
| Reference | Yes | No | E2 (empty), E3 (not unique), E7 (too long) |
| ORG - Reference | Yes | No | E1 (no permission), E2 (empty), E4 (does not exist), E5 (value cannot be changed) |
| Absences | Yes | Yes | E2 (empty), E6 (not a valid value; on update the same message as a warning), change is detected |
| Description | No | Yes | Change is detected |
| Last modified | No | No | W3 (element already updated since export) |

### "Implementations" sheet (IMPL / ELEM / TMPL / COURSE / EVENT) [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9210)" }](https://track.frentix.com/issue/OO-9210){:target="_blank"} {: #rules_implementations}

| Column | Mandatory | Updatable | Possible message |
|---|---|---|---|
| PROD - Reference | Yes | No | E2, E1, E4, E5 (element belongs to another product) |
| IMPL - Reference | Yes | No | E2, E4, E5 (element belongs to another implementation), for IMPL the message "Both references must be the same" if the value differs from the reference of the row |
| Object type | Yes | No | E2, E6, E19 (TMPL: usage is not "Template"; COURSE: usage is not "Use in Course Planner"), for COURSE with the usage "Standalone" administrators get a warning instead of E19 |
| Level | Yes for ELEM | No | E2 (ELEM), E8 (no element with this level) |
| Title | Yes | Yes | E2, W2, change is detected |
| Reference | Yes | No | E2, E7, E3 (depending on object type), additionally E1/E4 for TMPL/COURSE: there the reference is the one of an existing learning resource |
| Status | Yes (except EVENT) | Yes | E2, E6, W1, change is detected |
| Date/Time Begin and End | Yes for EVENT | Yes | E2 (EVENT), E9 (invalid format), E10 (invalid period), E11 (time except for EVENT), W4, change is detected |
| Unit | No | Yes | E6 (not a valid value; on update the same message as a warning), change is detected |
| REF - Reference | Yes for EVENT with course | No | E2, E5, E4 |
| Location | No | Yes | W2, change is detected |
| Rooms (EVENT only) [:octicons-tag-16:{ title="from Release 21.0.1 (OO-9303)" }](https://track.frentix.com/issue/OO-9303){:target="_blank"} | No | Yes | E4 (on creation), W5 (on update), E9 (value not in the format "building reference:room reference", also on update), change is detected |
| ELEM Type - Reference | Yes for IMPL/ELEM | No | E2, E4, E5, E12 to E17 (see structural rules) |
| Calendar / Absences / Progress | Yes for IMPL/ELEM | Yes | E2, E6 (not a valid value; on update the same message as a warning), change is detected |
| Subjects | No | Yes | E4 (on creation), W5 (on update), change is detected |
| Last modified | No | No | W3 |

**Additional structural rules**

Administrators define how an element type is configured in the system administration, in the [Module Course Planner](../../manual_admin/administration/Modules_Course_Planner.md#configuration). The import checks each implementation and each element against the configuration of its element type and reports a violation in the column "ELEM Type - Reference" of the row whose element type breaks the rule. The courses and course templates of an element are the COURSE and TMPL rows that belong to this element.

| Object type | Rule | Message on violation |
|---|---|---|
| IMPL | An element type with "For use as" "Element" is not permitted as an implementation | E12 |
| IMPL / ELEM | An element type whose setting "Subelements" is "No" must not have subelements | E13 |
| ELEM | The element type must be selected in the setting "Child elements" of the parent element's type. This setting defines which types are allowed below | E14 |
| IMPL / ELEM | An element type with "Content" "No content" allows no courses and no course templates | E15 |
| IMPL / ELEM | An element type with "Content" "Single course" allows at most one course and at most one course template; one course and one course template together are allowed | E16 |
| IMPL / ELEM | An element type with "Content" "Course bundle" allows no course templates | E17 |

### "Memberships" sheet [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9224)" }](https://track.frentix.com/issue/OO-9224){:target="_blank"} {: #rules_memberships}

| Column | Mandatory | Possible message |
|---|---|---|
| PROD - Reference / IMPL - Reference / Reference | Yes, all three | E2, E4, E22, E23 |
| Role | Yes | E2, E6 |
| Username | Yes | E2, E21/E24 (username missing in the "Users" sheet), E22 (account with errors), E23 (account ignored) |

Memberships can only be newly created, not updated.

### "Users" sheet {: #rules_users}

| Column | Mandatory (on creation) | Possible message |
|---|---|---|
| Username | Yes | E2, E7, on creation a message if the username is not permitted, E21/E24 (username missing in the "Memberships" sheet) |
| First name | Yes | E2, E7, W7 (changed for existing accounts) |
| Last name | Yes | E2, E7, W7 |
| E-mail | Yes, unless the option "Mandatory" is switched off in the [Email Settings](../../manual_admin/administration/E-Mail_Settings.md#email_address) | E2, E7, a message if the address is invalid or another account already uses it |
| ORG - Affiliation | Yes | E2, E1, E4, for existing accounts without this organisation the message of E5 as a warning |
| Password | No | E25 (must be empty for existing accounts), on creation a message if the password does not meet the requirements in the tab ["Password syntax"](../../manual_admin/administration/Login_Password_and_Authentication.md#tab-password-syntax) |
| Account expiration | No | Must be in the future on creation, otherwise an error message; W7 on change to existing accounts |

Each account in the "Users" sheet needs at least one row in the "Memberships" sheet, otherwise the import reports E21/E24. Existing accounts may be in the sheet so that their memberships are imported. The import does not change their details: it only creates new accounts and reports differing values of existing accounts as a warning.

[To the top of the page ^](#import_export_reference)

---

## Further information {: #further_information}

[Course Planner: Import / Export >](Course_Planner_Import_Export/index.md)<br>
[Module Course Planner >](../../manual_admin/administration/Modules_Course_Planner.md)<br>
[Email Settings >](../../manual_admin/administration/E-Mail_Settings.md)<br>
[Password and Authentication >](../../manual_admin/administration/Login_Password_and_Authentication.md)<br>
[Course Planner: Implementations >](Course_Planner_Implementations.md)<br>
[Import templates >](../basic_concepts/Import_Templates.md)

[To the top of the page ^](#import_export_reference)
