# Copy a course with wizard {: #course_copy_wizard}

![Menu item Copy with wizard highlighted, directly above it the menu item Copy](assets/course_copy_with_wizard_v1_de.png){ class="shadow lightbox" title="Administration menu of a course" }

You can find this option in the course under `Course > Administration > Copy with wizard`. It is available to course owners with the role Author, learning resource managers and administrators. Other authors get it if "copy" is checked under "Authors can" in `Course > Administration > Settings > Tab "Share"`.

The wizard can be used to select the elements of a course to be copied. This makes it even more effective to transfer elements for a new course run.

In the first step "General settings" you choose the copy mode "Automatic" or "Custom". In the copy mode "Custom", the course objects to be copied can be selected and further settings can be made, e.g. with regard to member administration and certain course elements. 

This function is only available for [learning path courses](Learning_path_course.md). To copy a conventional course for the next run, use `Course > Administration > Copy`, see [Copy (a course)](Course_Copy.md).


!!! tip "Tip"

    Always create a course copy if you want to repeat a course instead of just removing the people from the member list. This will also remove all entries in the assessment tool and you will receive a completely clean course.

!!! tip "Tip"

    It also makes sense to create a course copy as a backup after the course has been completed and before the start of the course.

!!! tip "Tip"

    Copying can also be called up in the list of the authoring area. There you will find the option after clicking on the 3 dots at the end of a line.


## Events and room bookings [:octicons-tag-16:{ title="from Release 16.0 (OO-4416)" }](https://track.frentix.com/issue/OO-4416){:target="_blank"} {: #events_rooms}

If you copy a course for the next run, you can copy the events along with it instead of recording them again. The "Events" selection appears if the course has events and you choose the copy mode "Custom" in the "General settings" step. The "Copy options" step then shows it under "Further options" with "Copy", "Customize" and "Don't copy". With "Customize", the "Events" step follows, in which you change the date and location of each event and reassign the teachers.

In the copy mode "Automatic", the default setting of your OpenOlat instance applies; by default, no events are copied. The help at the "Copy mode" field shows which setting applies. The default setting is part of the server configuration. frentix customers contact the frentix support for a change: [support@frentix.com](mailto:support@frentix.com)

If the ["Rooms" module](../../manual_admin/administration/Modules_Rooms.md) is activated, every copied event also adopts the room bookings of the original event. The period of the room booking follows the copied event. The room booking always adopts the room from the original event, even if you change the "Location" field in the "Events" step. OpenOlat does not check during copying whether the room is still free in the new period. An overlap is shown as a warning in the [room scheduling in the Course Planner](../area_modules/Course_Planner_Rooms.md#warnings). [:octicons-tag-16:{ title="from Release 21.0 (OO-9459)" }](https://track.frentix.com/issue/OO-9459){:target="_blank"}


## Further information {: #further_information}

**Mentioned on this page**<br>
[Learning path course - Overview >](Learning_path_course.md)<br>
[Copy (a course) >](Course_Copy.md)<br>
[Module Rooms (Administration) >](../../manual_admin/administration/Modules_Rooms.md)<br>
[Course Planner: Room management >](../area_modules/Course_Planner_Rooms.md)

**Further reading**<br>
[Save (a course) as template >](Course_Copy_Template.md)<br>
[Events and absences >](Events_and_absences.md)

[To the top of the page ^](#course_copy_wizard)
