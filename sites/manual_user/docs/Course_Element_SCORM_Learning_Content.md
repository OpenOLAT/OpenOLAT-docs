#  [Course Element: SCORM Learning
Content](Course+Element%EF%B9%95+SCORM+Learning+Content.html)

##

##
![](../../download/thumbnails/108600599/scorm%EF%B9%96version=1&modificationDate=1567436381000&api=v2.png)

SCORM means "Sharable Content Object Reference Model" and is another
standardized e-learning format supported by OpenOlat. Use the course element
"SCORM learning content" to include learning content in SCORM format (SCORM
version 1.2) in your course. Your SCORM package has to be created externally,
e.g. with [eLML](http://www.elml.org "eLML").

Go to your course and add a course element "SCORM learning content" to the
course. Afterwards you can configure the course in the tab "Learning content".

## Tab Learning Content

In the first step, select or import a SCORM content. Click "Import" to upload
a new SCORM package, or select an existing SCORM package from your entries.
SCORM packages can either be imported to the course editor or by means of the
"Authoring;" for further information please go to the chapter "Actions in the
'Authoring' section", section
["Import"](Actions+in+the+'Authoring'+section.html#Actionsinthe'Authoring'section-
_importieren). If you have not selected a ZIP file as SCORM learning content
yet the message _No SCORM learning content selected_ will appear in the title
**Selected SCORM learning content**.

If you have already added SCORM learning content, its name appears as a link.
Follow this link to get to the preview. In order to change the assignment of
your SCORM learning content you have to click on "Replace SCORM learning
content" in the tab "Learning content" before selecting another SCORM package.

In the section "Settings" you can determine how your learning content should
be presented to course participants.

 **Show menu:** Determine if there should be a navigation menu on the left
along with your SCORM packet.

 **Skip launch page:** Determine if the SCORM learning content should launch
automatically if the corresponding menu-node is selected within the course. If
you do not select this option, a start-page is displayed instead.

 **Show navigation buttons:** Determine if it should be possible to navigate
via the back and forward buttons within your SCORM content.

 **Display only module, hide LMS:** Check this box if you want OpenOlat to be
hidden while the SCORM module is active.

 **Close module automatically on finish:** Check this box if the SCORM module
should automatically close when it's finished, returning the participant to
the course.

 **Transfer score from SCORM:** Determine if the total score of your SCORM
packet should be transferred to the OLAT assessment system.

 **Score needed to pass:** Determine an integer to indicate your minimum score
for passing that SCORM test.

 **Prevent subsequent attempts from decreasing score:** If this box is
checked, a score already achieved will not be decreased by further attempts.

 **Count attempts only if score is transferred:  **Solution attempts are only
counted for the user if points are also transferred from the scorm to
OpenOlat. Depending on when the scorm delivers the points (e.g. regularly or
only at the end of processing), the option already applies when a user has
processed part of the scorm activities or only when the scorm is closed.

 **Max number of attempts:** By means of the drop-down menu the number of
attempts available can be limited.

##   Tab Layout

In the "Layout" tab you can define the settings for the display of the SCORM
package. You can either use the layout configuration settings from the
learning resource, or modify the standard settings. If you choose the "Modify"
option, the following settings are available. You can then determine whether
the SCORM package should be displayed unaltered, or optimized for OpenOlat.
The display mode "Optimized for OpenOlat" allows you to e.g. apply the course
layout to the SCORM package.

Under "Settings" you can determine how the learning content is to be displayed
to your course participants.

 Display options

 **Use standard configuration:** If you embed learning resources from the
learning resources management in the course you can choose to use the display
configuration from the learning resource management (option "Use from learning
resource layout configuration"). If you want to override the standards values
for this course, then select option "Modify".

* * *

 **Display mode:** Select the mode "Standard" to display the resource
unmodified. This mode is useful for resource that encounter render issues when
using the mode "Optimized for OpenOlat". Use the mode "Optimized for OpenOlat"
when you want to embed the course layout, a JavaScript library, the OpenOlat
glossary or when you want to use the automatic height detection of the page.
In case of SCORM modules the mode "Standard" is recommended.

* * *

 **Embed Javascript library:** To use the features of the display mode
"Optimized for OpenOlat" the JavaScript library "jQuery" must be activated.
The option "Prototype" should only be used in case your content requests this
library. Select no JavaScript library if you have display issues with your
content within OpenOlat.

 **Embed glossary terms:** Select this option to activate the glossary terms
embedding on that page if you have a glossary configured for this course. This
option requires the JavaScript library "jQuery".

 **Display height:** By means of the drop-down menu you can determine the
height of your content. You have the possibility to set them via "Automatic"
to the respective window height or to a certain value of your choice.

 **Adapt layout:** Select the option "OpenOlat stylesheets" to embedd the
OpenOlat and course layout into this page (font type, colors, sizes etc.). If
you do not want this option select "None".

* * *

 **Content character set:** OpenOlat tries to detect a character set
automatically. If the option "Automatic" is not successful it is possible to
configure the content coding by means of a predefined character set (should
there be no coding the character set ISO-8899-1 will be used by default).

 **Javascript character set:** This permits the coding of Javascript by means
of a predefined character set (by default the same set will be used for
content and Javascript).

SCORM learning content will always be presented with a homepage. If such
content contains tasks as well as tests you will learn from that homepage more
about your score and remaining attempts to take tests.

