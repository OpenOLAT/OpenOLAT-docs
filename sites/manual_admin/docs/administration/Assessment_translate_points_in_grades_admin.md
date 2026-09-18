# e-Assessment Administration: Levels/Grading {: #grades_points}

[:octicons-tag-16:{ title="from Release 16.2 (OO-6007)" }](https://track.frentix.com/issue/OO-6007)

Administrators enable the module "Levels/Grading" and create the rating systems that convert points into grades. You find the module in the system administration under:<br>
`Administration > e-Assessment > Levels/Grading`

![Levels/Grading page in the e-assessment area: the enabled module provides eight grading systems, the Usage column shows how often a system is in use](assets/Admin_Noten_en.png){ class="shadow lightbox" }

The term "Note" is used here as a placeholder for all possible output formats. (Examples could be: 1-6, A-F, "very good" - "unsatisfactory", "Beginner"/"Advanced"/"Expert" etc.).

After activation, course owners can enable Levels/Grading in the course editor in assessable course elements, for example in Test, Task, Assessment or Video task.

## Grading system

System administrators can make the following settings to configure the rating systems:

![Edit rating system dialog with type Numerical: resolution, rounding and the lowest and highest rating, plus the Passed with threshold when the success status is enabled](assets/admin_Noten_Bewertungssystem_en.png){ class="shadow lightbox" }

### Numeric type

Numeric rating systems can be customised in the resolution (whole, half, quarter, tenth) and in the rounding. OpenOlat calculates the performance classes from the entered maximum number of points and the "Passed with" limit. The rating scale follows from this.

### Textual type

With textual rating systems, one defines the number of performance classes and their name/label. The maximum number of points and the score lower bound per performance class then determine the general conditions of the rating scale.

![Edit rating system dialog with type Textual: performance classes define the levels instead of numeric ranges, and the Passed column sets the outcome per class](assets/admin_Noten_Bewertungssystem_textuell_en.png){ class="shadow lightbox" }

Further examples of useful labels are: Beginner, Advanced, Professional or various emojis.

Several rating systems can be stored and made available in the system administration.
