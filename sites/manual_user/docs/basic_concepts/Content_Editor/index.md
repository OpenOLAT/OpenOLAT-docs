# Content Editor

## What is the Content Editor? {: #content_editor}

With the Content Editor you design a page from various content elements, arranged according to a layout you choose yourself. The page is optimised for mobile devices. OpenOlat saves your changes automatically.

The Content Editor is used in several places in OpenOlat. Who uses it depends on the place: in the course element "Page" the owners of the course and authorised coaches, in the learning resource "Form" its owners, in the portfolio the owners of the binder.

![A page in edit mode: selected title block with its toolbar, on the right the inspector with the tabs Style and Layout, below further blocks and the link Add content](../assets/content_editor_v2_en.png){ class="shadow lightbox" title="Content Editor in the course element Page · 2026.11.10" }

!!! note "Note"

    Besides the Content Editor, OpenOlat also has the HTML editor "TinyMCE", which is used in the [course element "HTML page"](../../learningresources/Course_Element_HTML_Page.md), for example.


## Tasks in the Content Editor {: #tasks}

Each task in the Content Editor has its own page:

| Page | What for |
|---|---|
| [Layout](Editor_Layout.md) | Divide a page into areas, arrange content in them and set spacing, background and alert boxes. |
| [Add content](Editor_Add_Content.md) | Insert texts, images, videos, documents and other content, also from your Media Center, the store for your media files. |
| [Quiz and AI feedback](Editor_Quiz.md) | Ask learners questions about the content in the course element "Page" and give them AI feedback on free-text answers. |
| [Import](Editor_Import.md) | Take over a Markdown or Word file into a page and, if the AI feature is set up, let the AI generate questions. |

[To the top of the page ^](#content_editor)

---


## Where is the Content Editor used? {: #content_editor_use}

The Content Editor is used in the [course element Page](../../learningresources/Course_Element_Page.md), in the [learning resource "Form"](../../learningresources/Form/index.md) and in the ["Portfolio 2.0"](../../area_modules/The_portfolio_editor_17_1.md).

### Course element page [:octicons-tag-16:{ title="from Release 18.0.0 (OO-6966)" }](https://track.frentix.com/issue/OO-6966){:target="_blank"} {: #course_element_page}

In the course element "Page" you open the Content Editor in two ways: in the course editor in the tab "Page content" with "Edit page", or with the course editor closed directly in the course element by switching on the edit mode. You reach the course editor under: `Course > Administration > Course editor`.

**When the course editor is closed:**

![The Edit mode switch is set to Off, highlighted in turquoise.](../assets/content_editor_page_run_mode_v1_de.png){ class="shadow lightbox" title="Course element Page in the course" }

The switch "Edit mode" turns editing of the page on and off.

**In the course editor:**

![Three marked steps: course element Page, tab Page content, button Edit page.](../assets/content_editor_page_edit_v1_de.png){ class="shadow lightbox" title="Course element Page in the course editor" }

In the tab "Page content" you define under "Rights" whether, in addition to course owners, coaches may also edit the page when the course editor is closed: option "Edit page" for "Coach". With "Show advanced configuration" you additionally grant the right to individual roles, groups or users, optionally with a start and end.

![The option Edit page is ticked for coaches.](../assets/content_editor_page_edit_right_coach_v1_de.png){ class="shadow lightbox" title="Page content tab of the course element Page" }

OpenOlat stores the media content of the [Course Element "Page"](../../learningresources/Course_Element_Page.md) (images, audio, video, diagrams, citations, documents, etc.) in the [Media Center](../../personal_menu/Media_Center.md), not in the course’s storage folder as with the [Course Element "HTML Page"](../../learningresources/Course_Element_HTML_Page.md).

The media of a portfolio binder are also stored in the Media Center. The learning resource "Form", by contrast, stores images in the learning resource itself.

[To the top of the page ^](#content_editor)

---


### Learning resource form {: #form}

The [learning resource Form](../../learningresources/Form/index.md) and all elements that use a form also use the Content Editor.

The displayed options for inserting content are adapted to the form, e.g. different question types are available here.

![The Add content dialog in the form editor with the additional group Question type.](../assets/Formular_Inhalt_hinzufuegen19.jpg){ class="shadow lightbox" title="Add content dialogue in the form editor" }

[To the top of the page ^](#content_editor)

---


### E-portfolio [:octicons-tag-16:{ title="from Release 11.0 (OO-2057)" }](https://track.frentix.com/issue/OO-2057){:target="_blank"} {: #portfolio}

The Content Editor is also used for entries in [binders](../../area_modules/My_portfolio_binders.md), which can be used both independently of a course and in conjunction with [portfolio templates](../../learningresources/Portfolio_template_Creation.md) and [portfolio tasks](../../learningresources/Course_Element_Portfolio_Task.md).

![Selection of the layout templates with nine grids, opened via Insert new layout.](../assets/content_editor_layout_portfolio_v1_de.png){ class="shadow lightbox" title="Layout templates of a portfolio binder" }

[Portfolio >](../../area_modules/The_portfolio_editor_17_1.md)

[To the top of the page ^](#content_editor)

---


## Further information {: #further_information}

**Further reading**<br>
[Media Center Concept >](../Media_Center_Concept/index.md)<br>
[Accessibility: Basic principles >](../Accessibility_Principals.md)

[To the top of the page ^](#content_editor)
