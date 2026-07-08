# Reports: Certificates {: #certificate_reports}

This page describes the structure of the Excel files generated with the [report templates of the category Certificates](../area_modules/Coaching_Reports.md). Each file contains the worksheet "Individual courses" and, if the Course Planner module is active, an additional worksheet "Products".

## Worksheet "Individual courses" [:octicons-tag-16:{ title="from Release 20.0 (OO-8371)" }](https://track.frentix.com/issue/OO-8371) {: #individual_courses}

| Column                | Source      | Description                                |
|-----------------------|-------------|---------------------------------------------|
| Certificate ID        | Certificate | Unique number of the certificate           |
| Course                | Course      | Title of the course                        |
| Ext. ref.             | Course      | External reference of the course           |
| User data             | Person      | According to the configuration in the administration; by default last name, first name and e-mail address |
| Initial course launch | Course      | Date of the first visit to the course      |
| Success status        | Course      | "Passed", "Not passed" or "Undefined"      |
| Issued on             | Certificate | Date of issue of the certificate           |
| Valid until           | Certificate | Expiry date of the certificate; empty if no validity period is configured |

## Worksheet "Products" [:octicons-tag-16:{ title="from Release 20.0 (OO-8371)" }](https://track.frentix.com/issue/OO-8371) {: #products}

The worksheet "Products" lists the certificates of courses that are assigned to an educational product (curriculum element). In addition to all columns of the worksheet "Individual courses", it contains the following columns at the beginning of each row:

| Column    | Source         | Description                     |
|-----------|----------------|---------------------------------|
| Element   | Course Planner | Title of the curriculum element |
| Ext. ref. | Course Planner | External reference of the element |
| Element type | Course Planner | Title of the element type    |

If a course is assigned to several curriculum elements, the values in the cell are listed separated by a vertical bar.

[To the top of the page ^](#certificate_reports)
