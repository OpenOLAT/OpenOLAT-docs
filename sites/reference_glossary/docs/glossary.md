# Glossary

A reference glossary of product-specific terms used in OpenOlat. These terms have specific meaning within the OpenOlat LMS. The glossary is generated automatically from the OpenOlat term model and holds 698 terms.

## Catalogue, booking and payment

From the catalogue entry to the paid membership.

### Access code

An offer type in which only people with the right code can book. The code is handed out outside OpenOlat.

*German: Zugangscode* · [Manual](../manual_user/basic_concepts/Offer_Concepts.md)

### Access control

The module that decides who may enter a learning resource and on what conditions. It manages the offers, the bookings and the payment methods.

*German: Zugangskontrolle* · [Manual](../manual_admin/administration/Core_functions.md)

### Billing address

The address the invoice goes to. It can differ from the address of the person booking, for example when the employer books.

*German: Rechnungsadresse* · [Manual](../manual_user/area_modules/Reports_BookingOrders.md)

### Booking

The process by which a person gains access to a learning resource. It ends with the membership in the course or with a place on the waiting list.

*German: Buchung* · [Manual](../manual_user/personal_menu/Bookings.md)

### Booking order

The record created by a booking. It holds who booked what, when and at what price, and is kept after the course has ended as well.

*German: Buchungsauftrag* · [Manual](../manual_user/area_modules/Reports_BookingOrders.md)

### Catalog (module)

The module that puts learning resources and implementations with an offer on display for booking. It is structured through the taxonomy and the launchers. Without an offer a resource does not appear. Without signing in it is reachable as the web catalog, if that is switched on.

*German: Katalog* · [Manual](../manual_admin/administration/Modules_Catalog_2.0.md)

### Catalog (navigation entry)

The Catalog entry in the main navigation through which signed-in people open the catalog. It is the platform's shop window. For people without an account the web catalog mirrors it.

*German: Katalog* · [Manual](../manual_admin/administration/Modules_Catalog_2.0.md)

### Catalog administration

The entry in the main navigation through which catalog 1.0 is maintained: its categories and the assignment of learning resources. It appears only when catalog 1.0 is switched on. Catalog 2.0 is managed in the administration under modules.

*German: Katalogverwaltung* · [Manual](../manual_user/area_modules/catalog1.0.md)

### Cost center

The place in the organisation's accounting that carries the cost of a booking.

*German: Kostenstelle* · [Manual](../manual_user/area_modules/Reports_BookingOrders.md)

### Credit

A transaction that adds credit points to a person, as a rule after a passed course.

*German: Gutschrift*

### Credit points

The module that keeps credit points per person in a credit point system, credits them for passed courses and debits them again in certification programs for recertification. Paying for bookings with credit points is announced but not implemented.

*German: Kreditpunkte* · [Manual](../manual_user/personal_menu/Credit_Points.md)

### Credit point system

A named system of credit points with its own unit and its own rules, for example ECTS. One installation can run several of them.

*German: Kreditpunktesystem* · [Manual](../manual_admin/administration/e-Assessment_Credit_Points.md)

### Debit

A transaction that subtracts credit points from a person, for example when they are redeemed for a recertification.

*German: Belastung*

### Invoice

The payment method in which the amount is invoiced later instead of being paid online straight away.

*German: Rechnung* · [Manual](../manual_admin/administration/Payment_Invoice.md)

### Launcher

A configurable section on the start page of the catalog that assembles catalog entries by a rule. There are seven launcher types, for example taxonomy level, recently published or popular courses.

*German: Launcher* · [Manual](../manual_admin/administration/Modules_Catalog_2.0.md)

### Offer

The definition of the conditions under which a learning resource can be booked: for whom, in which period, at what price and in what way. One resource can carry several offers side by side.

*German: Angebot* · [Manual](../manual_user/area_modules/catalog2.0_angebote.md)

### PayPal

The connection to PayPal as a payment method for paid offers.

*German: PayPal* · [Manual](../manual_admin/administration/Payment_PayPal.md)

### Pre-order

A booking recorded before the person has an account. It waits until the person signs in through Shibboleth or self-registration, and is then carried out.

*German: Vorbestellung*

### Transaction

A single movement on the credit point account: credit, debit, removal, reversal or expiration. The balance is the sum of all transactions.

*German: Transaktion*

### VAT

The value added tax on a paid offer. The rate is set system-wide and shown on the invoice.

*German: Mehrwertsteuer* · [Manual](../manual_admin/administration/Payment_modules.md)

### Waiting list

The queue of people who wanted to book a course or enter a group when no place was left. When a place opens up, the first person moves up, on request on its own.

*German: Warteliste* · [Manual](../manual_user/groups/Create_Groups.md)

### Web catalog

The mirror of the catalog outside the login: people without an account see offers, prices and free places and are led through registration only when they book. It requires a catalog 2.0 and is switched on in the administration.

*German: Web-Katalog* · [Manual](../manual_user/area_modules/catalog2.0_web.md)

## Course Planner

The planning layer above the courses: which educational offering exists (product), how it is structured (element) and when it actually runs (implementation).

### Automation

The rules the Course Planner uses to carry out recurring work on its own, for example creating courses from templates or opening and closing implementations.

*German: Automatisierung* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Automation rule

A single rule of the automation. It consists of a trigger, either a status change or a point in time relative to the implementation period, and an action such as instantiate a course or set a status. The element type provides it, the implementation can override it.

*German: Automatisierungsregel* · [Manual](../manual_admin/administration/Modules_Course_Planner.md)

### Course Planner (Course Planner)

The module that switches on the planning of the educational offering in OpenOlat: products with elements and implementations, element types, course templates, automation, to-dos and reports. It replaces the earlier Curriculum module and grants the memberships of the courses it embeds.

*German: Course Planner* · [Manual](../manual_admin/administration/Modules_Course_Planner.md)

### Course template

A course assigned to an element in the Course Planner in order to instantiate a course of its own from it for every implementation. The template itself is not attended and stays unchanged.

*German: Kurstemplate* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Educational products

An educational offering kept in the Course Planner, made up of several courses and implementations, as coaching and the catalogue show it.

*German: Bildungsprodukte* · [Manual](../manual_user/area_modules/Coaching_Educational_Products.md)

### Element

A node in the structure of a product. Depending on the element type it stands for a study programme, a semester, a module or an implementation. The elements form the hierarchy the courses are hung into.

*German: Element* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Element type

The kind of an element in the Course Planner. The element type sets which elements are allowed below it, whether the element keeps members and how it appears in the catalogue.

*German: Elementtyp* · [Manual](../manual_admin/administration/Modules_Course_Planner.md)

### Implementation

The concrete run of an educational offering, with a period, a location, members and courses. The product describes what is offered, the implementation when and with whom it actually runs.

*German: Durchführung* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Instantiation

Creating a course from a course template for a particular implementation. The template stays unchanged and serves further implementations.

*German: Instanziierung* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Membership (Course Planner)

The belonging of a person to a course, a group or an element of the Course Planner, together with their role in it.

*German: Mitgliedschaft* · [Manual](../manual_user/area_modules/Course_Planner_Implementations.md)

### Product

The top level in the Course Planner. A product describes an educational offering with its structure, with the elements and the implementations hanging below it.

*German: Produkt* · [Manual](../manual_user/area_modules/Course_Planner_Products.md)

### Reports (Course Planner)

The area of the Course Planner with ready-made analyses of the booking orders, produced as Excel files from report templates. It is available in the overview for all implementations and as a tab on every product and every implementation for their own.

*German: Reports* · [Manual](../manual_user/area_modules/Course_Planner_Reports.md)

### Time period

A centrally maintained, named period such as a semester or a quarter that a course can choose as its implementation period. It serves filtering and sorting in the authoring area and in the Course Planner lists.

*German: Zeitabschnitt* · [Manual](../manual_admin/administration/Modules_Time_Period.md)

### Timetable

All the events of an implementation put together into one plan, with rooms and coaches.

*German: Stundenplan* · [Manual](../manual_admin/administration/Modules_Course_Planner.md)

### To-do (Course Planner)

An open item on an element of the Course Planner, with a responsible person and a deadline. It keeps the planning work on the object instead of in a separate list.

*German: To-do* · [Manual](../manual_user/area_modules/Course_Planner_Todos.md)

## Learning resources

What sits in the authoring area, how it is described and classified, and what makes up the single learning resource types: blog and podcast, glossary, video, files.

### Animation

A learning resource for an animation file.

*German: Animation* · [Manual](../manual_user/learningresources/index.md)

### Annotation

A text box that appears over the video for a set time and shows an explanation.

*German: Annotation* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Audio (Learning resources)

A learning resource for a single audio file.

*German: Audio* · [Manual](../manual_user/learningresources/index.md)

### Audio/video recording

The module with which people record audio and video directly in the browser: in the media center, in the content editor, in the task and in the video editor. The recording is converted in the background into a browser-friendly format, locally or by an external service.

*German: Audio/Video-Aufnahme* · [Manual](../manual_admin/administration/Modules_Audio_Video_Recording.md)

### Blog (Learning resources)

A learning resource for posts in reverse chronological order. Readers can subscribe to the posts and comment on them.

*German: Blog* · [Manual](../manual_user/learningresources/Blog.md)

### Chapter

A jump mark in the video. Learners pick a chapter and land at that point.

*German: Kapitel* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Comment

An overlay as text or as a short video that gives extra information at one point of the video.

*German: Kommentar* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Comments and ratings

The service with which readers comment on a piece of content and rate it with one to five stars. Blog and podcast switch it on per feed; comments can carry attachments and be replied to.

*German: Kommentare und Bewertungen* · [Manual](../manual_user/learningresources/Blog_Blogging.md)

### Competence

An ability attributed to a person, named through a taxonomy level. It comes about through assignment or through passing a course.

*German: Kompetenz* · [Manual](../manual_user/personal_menu/Competences.md)

### CP learning content (Learning resources)

A learning resource in the IMS Content Packaging format. It holds finished learning content with its own navigation, produced in another tool.

*German: CP-Lerninhalt* · [Manual](../manual_user/learningresources/Course_Element_CP_Learning_Content.md)

### Embed glossary terms

The highlighting of the glossary terms in the course text. A dotted underline marks a term; the definition appears on hover. Learners switch the highlighting on and off in the toolbar.

*German: Glossarbegriffe einbinden* · [Manual](../manual_user/learningresources/Glossary_usage.md)

### Entry (Learning resources)

A post in a blog, with title, summary, content, image and publication date. It is a draft, scheduled or published; readers can comment on it, rate it and take it into the media center.

*German: Eintrag* · [Manual](../manual_user/learningresources/Blog_Blogging.md)

### Episode

A post in a podcast with an audio or video file attached. It is played in OpenOlat, downloaded or listened to in a podcast app through the RSS feed.

*German: Episode* · [Manual](../manual_user/learningresources/Podcast_listen_and_watch.md)

### Excel

A learning resource for an Excel document. It can be edited in the browser when ONLYOFFICE or Microsoft 365 is connected.

*German: Excel* · [Manual](../manual_user/learningresources/index.md)

### File

A learning resource for a single uploaded file whose format OpenOlat does not treat specially.

*German: Datei* · [Manual](../manual_user/learningresources/index.md)

### Glossary

A learning resource with terms and their explanation. Embedded in a course it highlights the terms in the course text and shows the explanation on hover.

*German: Glossar* · [Manual](../manual_user/learningresources/Glossary.md)

### Image (Learning resources)

A learning resource for a single image file.

*German: Bild* · [Manual](../manual_user/learningresources/index.md)

### Learning resource

A content object managed in the authoring area: course, test, form, video, wiki and others. It carries metadata, owners and a lifecycle and can be embedded into courses.

*German: Lernressource* · [Manual](../manual_admin/administration/Modules_Learning_Resource.md)

### Level type

The kind of a taxonomy level. The level type sets whether levels of this type are visible, can serve as a competence and may group evidence of achievement.

*German: Ebenentyp* · [Manual](../manual_admin/administration/Modules_Taxonomy.md)

### Lost+found

The storage folder of a taxonomy for the documents of deleted taxonomy levels, for example from the document pool. It is the last tab of the taxonomy; the documents cannot be restored from there.

*German: Lost+found* · [Manual](../manual_admin/administration/Modules_Taxonomy.md)

### Media server

An external video platform whose videos OpenOlat may embed by URL: YouTube, Vimeo, nanoo.tv and custom servers. The administration enables the servers in the security settings; restricted domains are not played.

*German: Medien-Server* · [Manual](../manual_user/learningresources/Single_Page_Add_edit_video.md)

### Metadata (Learning resources)

The describing entries on a learning resource: title, description, language, authorship, license, taxonomy and effort. They feed the catalogue and the search.

*German: Metadaten* · [Manual](../manual_user/learningresources/Course_Settings_Metadata.md)

### Movie

A learning resource for a video file that is only played, without the extras of the Video learning resource.

*German: Film*

### Other file

A learning resource for an uploaded file whose format matches none of the other types.

*German: Andere Datei* · [Manual](../manual_user/learningresources/index.md)

### PDF

A learning resource for a PDF document. OpenOlat shows it in the built-in viewer, without it having to be downloaded.

*German: PDF* · [Manual](../manual_user/learningresources/index.md)

### Podcast (Learning resources)

A learning resource for audio and video episodes that can be subscribed to. It provides an RSS feed through which episodes are listened to outside OpenOlat as well.

*German: Podcast* · [Manual](../manual_user/learningresources/Podcast.md)

### Portfolio 2.0 template

A learning resource that prescribes the structure and the assignments of a portfolio binder. The portfolio task course element assigns every participant a binder made from this template.

*German: Portfolio 2.0 Vorlage* · [Manual](../manual_user/learningresources/Portfolio_template_Creation.md)

### PowerPoint

A learning resource for a PowerPoint presentation. It can be edited in the browser when ONLYOFFICE or Microsoft 365 is connected.

*German: PowerPoint* · [Manual](../manual_user/learningresources/index.md)

### Questionnaire (Learning resources)

Legacy: a questionnaire learning resource in the QTI 1.2 format that collected opinions instead of measuring knowledge. It can neither be created nor imported. The questionnaire course element today embeds a test learning resource configured as a questionnaire.

*German: Fragebogen* · [Manual](../manual_user/learningresources/Course_Element_Survey.md)

### Quiz (Learning resources)

A question that stops the video at a set point. Learners answer before it goes on.

*German: Quiz* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Rating (Learning resources)

The rating of a learning resource or a piece of content by its users with one to five stars. Shown is the average of all stars given; a person can change their own rating at any time. The administration switches the feature on or off system-wide.

*German: Beurteilung* · [Manual](../manual_user/learningresources/Blog_Blogging.md)

### SCORM 1.2 (Learning resources)

A learning resource in the SCORM 1.2 format. Unlike CP learning content the package reports progress and points back to OpenOlat, which is why it is assessable.

*German: SCORM 1.2* · [Manual](../manual_user/learningresources/index.md)

### Segment (Learning resources)

A time section of the video with start, duration and a term as its label. Segments do not overlap; the video task lets learners assign the segments to a term.

*German: Segment* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Subtitles

A subtitle track for the video, one WebVTT file per language. OpenOlat can also generate them itself.

*German: Untertitel* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Taxonomy

A hierarchical tree of terms that learning resources, questions, documents and competences are classified with. It is not Bloom's taxonomy of learning objectives.

*German: Taxonomie* · [Manual](../manual_admin/administration/Modules_Taxonomy.md)

### Taxonomy level

A node in a taxonomy. It classifies learning resources, questions and documents and can be used as a competence.

*German: Taxonomieebene* · [Manual](../manual_admin/administration/Modules_Taxonomy.md)

### Term (Learning resources)

An entry in the glossary: the word that is explained, with its definition, its synonyms and its flections. In the course every term is highlighted in the text.

*German: Begriff* · [Manual](../manual_user/learningresources/Glossary_create.md)

### Test (Learning resources)

A learning resource with questions in the QTI 2.1 format that measures knowledge. It is embedded into a course through the test or self-test course element and can take questions from the question pool.

*German: Test* · [Manual](../manual_user/learningresources/Course_Element_Test.md)

### Test (QTI 1.2 - no longer supported)

Legacy: a test learning resource in the QTI 1.2 format. Since release 15.0 it no longer runs, since 16.0 it can no longer be converted. It can neither be created nor imported and appears only in lists of old entries.

*German: Test (QTI 1.2 - nicht mehr unterstützt)* · [Manual](../manual_user/learningresources/Changing_from_QTI_1.2_to_QTI_2.1.md)

### Timeline (Learning resources)

The time axis below the video. It shows every event in its place: chapter, annotation, comment, quiz and segment.

*German: Timeline* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Transcoding

The conversion of an uploaded video file into several resolutions, so that playback matches the connection. It runs in the background.

*German: Transkodierung* · [Manual](../manual_admin/administration/Modules_Video.md)

### Video (Learning resources)

A learning resource for a video file in mp4 format, extended with chapters, quiz questions, comments, segments and annotations. OpenOlat converts the file into several resolutions.

*German: Video* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Video editor

The working surface of the video learning resource. Chapters, annotations, comments, quiz questions and segments are made here, all tied to a point in time in the video.

*German: Video-Editor* · [Manual](../manual_user/learningresources/Learning_resource_Video.md)

### Wiki (Learning resources)

A learning resource for pages that several people write together and link to each other. Every change is versioned.

*German: Wiki* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

### Word

A learning resource for a Word document. It can be edited in the browser when ONLYOFFICE or Microsoft 365 is connected.

*German: Word* · [Manual](../manual_user/learningresources/index.md)

## Content and media

What content is built with: the content editor with its content elements, and the media center where the media sit across courses.

### Audio (Content and media)

An audio recording on a page, from the Media Center or recorded in the browser.

*German: Audio* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Citation

A highlighted quotation with its source. It lives as a medium in the Media Center and can be used more than once.

*German: Zitat* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Code example

A block of source code with syntax highlighting, optionally with line numbers and a copy button.

*German: Code-Beispiel* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Container

A layout frame that holds other content elements in columns. It sets the number of columns and the spacing.

*German: Container* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Content editor

The block-based editor that content is assembled from out of paragraphs, images, tables and form elements. It provides the page course element, the form learning resource and the portfolio pages.

*German: Content Editor* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Content element

A building block of a page: a paragraph, an image, a table, a quiz. The "add content" dialog offers them in groups, and they can be moved around the page freely.

*German: Inhaltselement* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Diagram

A drawing made with draw.io on a page: a flowchart, a process, an org chart. It stays editable.

*German: Diagramm* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Document (Content and media)

A file on a page, to download or as an embedded preview.

*German: Dokument* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Gallery

Several images as a gallery on a page, with thumbnails and a large view.

*German: Galerie* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### HTML text code

A block of raw HTML, for embeddings no other element covers.

*German: HTML-Textcode* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Image (Content and media)

An image on a page. It comes from the Media Center and is therefore available across courses.

*German: Bild* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Image comparison

Two images on top of each other with a slider that moves between them.

*German: Bildvergleich* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Inspector

The panel in the content editor that opens for a selected layout or content element and sets its properties: the options of the element type, the style with background and alert box, and layout and spacing. The gear icon shows and hides it.

*German: Inspektor* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Math formula

A formula written in LaTeX and rendered as typeset mathematics.

*German: Mathematische Formel* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Media Center (Content and media)

The module in which each person stores and manages their media: images, videos, audio, documents, citations, diagrams and texts. Media can be versioned, given tags and a license, and shared with people, groups, courses and organisations. Pages, forms and portfolios embed them instead of copying them.

*German: Media Center* · [Manual](../manual_user/basic_concepts/Media_Center_Concept.md)

### Quiz (Content and media)

Questions right on the page, with no test element of their own. Learners answer while reading and see the result at once.

*German: Quiz* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Separator

A horizontal line that separates two sections of a page.

*German: Separator* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Shares (Content and media)

Sharing a medium of the Media Center with other people, groups, courses or organisations, optionally with the right to edit it.

*German: Freigaben* · [Manual](../manual_admin/administration/Modules_Media_Center.md)

### Table

A table, entered directly on the page.

*German: Tabelle* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Table of contents

A list built from the titles of the page, which grows with them.

*German: Inhaltsverzeichnis* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Text

A block of text with the full formatting toolbar. The most common content element of a page.

*German: Text* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Title

A heading on the page, in one of six levels.

*German: Titel* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### Video (Content and media)

A video on a page, either as a file from the Media Center or through a URL from YouTube or Vimeo.

*German: Video* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

## Course

The course as a learning resource, its elements, its configuration and its lifecycle from preparation to the trash.

### Access configuration

The area of a learning resource where the offers are set: who may book, at what price and in which period.

*German: Zugangskonfiguration* · [Manual](../manual_user/learningresources/Access_configuration.md)

### Access for coach

The publication status in which a course is visible to the coaches but not yet to the participants. It serves the preparation in the team before the start.

*German: Freigabe Betreuer:innen* · [Manual](../manual_user/learningresources/Access_configuration.md)

### Additional condition

A further rule beside the first one. The interface separates the main condition from the additional ones, but all of them are checked alike.

*German: Zusatzbedingung* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Adobe Connect (Course)

A course element that embeds an Adobe Connect room into the course. Coaches schedule sessions, participants join from inside the course.

*German: Adobe Connect* · [Manual](../manual_user/learningresources/Course_Element_Adobe_Connect.md)

### Appointment

A single selectable time slot in an occasion of the appointment scheduling, with a start, an end, a location, an optional limit of participants, an enrolment deadline and an online room. Participants enter and withdraw themselves.

*German: Termin* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Appointment booking

A type of occasion: participants enter themselves for one or more fixed appointments from a selection, optionally with a limited number of participants and confirmation by the organizers.

*German: Terminbuchung* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Appointment finding

A type of occasion: participants pick all appointments that suit them, the organizers then confirm the final common appointment.

*German: Terminfindung* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Appointment scheduling

A course element that groups appointments into occasions. As an appointment booking, participants enter themselves for fixed appointments; as an appointment finding, they pick suitable appointments and the organizers confirm one of them.

*German: Terminplanung* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Archiving & Reporting

The course tool with which owners create a complete or a partial archive of the course and generate reports such as the forum report.

*German: Archivierung & Reports* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Assessment (Course)

A course element in which coaches assess a performance without anything being submitted in OpenOlat. It serves performances outside the platform, for example a presentation or an exam in the classroom.

*German: Bewertung* · [Manual](../manual_user/learningresources/Course_Element_Assessment.md)

### Assignment of dates

A course element for handing out single dates, for example exam or consultation slots.

*German: Terminvergabe*

### BigBlueButton (Course)

A course element that embeds BigBlueButton rooms into the course. Coaches schedule sessions, participants join from inside the course, recordings stay available in the course.

*German: BigBlueButton* · [Manual](../manual_user/learningresources/bigbluebutton/index.md)

### Blog (Course)

A course element that embeds a blog learning resource into the course. It informs participants about current topics in reverse chronological order.

*German: Blog* · [Manual](../manual_user/learningresources/Course_Element_Blog.md)

### Calendar (Course)

A course element that ties the course calendar into the course menu.

*German: Kalender* · [Manual](../manual_user/learningresources/Course_Element_Calendar.md)

### card2brain flashcards

A course element that shows a flashcard set of the card2brain platform in the course so that participants practise with online flashcards.

*German: card2brain Lernkarten* · [Manual](../manual_user/learningresources/Course_Element_card2brain_Flashcards.md)

### Check box

A single item of a check list, with a label, a description, an optional file and points. Participants or only coaches tick it off.

*German: Checkbox* · [Manual](../manual_user/learningresources/Course_Element_Checklist.md)

### Check list

A course element with a list of points that participants or coaches tick off. Working on it can be locked after a submission date, and the ticks can award points.

*German: Checkliste* · [Manual](../manual_user/learningresources/Course_Element_Checklist.md)

### Check list (old)

The earlier implementation of the check list, kept for existing courses. New courses use the check list.

*German: Checkliste (alt)*

### Coach files

The folder of a course that only owners and coaches see. It holds material not meant for participants.

*German: Unterlagen Betreuer:innen* · [Manual](../manual_user/learningresources/Coach_Files.md)

### Complete archive

A course archive with all course elements, course results, course chat and log files. It can be created for one course or as a bulk action for several courses in the authoring area.

*German: Gesamtarchiv* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Condition

The rule that steers the visibility and access of a course element in the conventional course: blocked for learners, depending on date, group or assessment, only in assessment mode. In expert mode it is written as an expression.

*German: Bedingung* · [Manual](../manual_user/learningresources/General_Configuration_of_Course_Elements.md)

### Consents

The recorded consents of a person to the terms of use, with the point in time and the version of the text.

*German: Einwilligungen* · [Manual](../manual_user/learningresources/Members_management.md)

### Conventional course

A course design in which the participants navigate the course menu freely. Access to single elements is steered through conditions, not through an order.

*German: Herkömmlicher Kurs* · [Manual](../manual_user/learningresources/Creating_Course.md)

### Course

A course is a learning resource, but a special one: it is the only one that keeps members, roles and assessments. No other learning resource has any of that, and they are embedded into a course in order to reach participants. The course ties content, activities and assessment into one structured sequence.

*German: Kurs* · [Manual](../manual_admin/administration/Modules_Course.md)

### Course archive

All the data of a course assembled into a file for keeping, with assessments, submissions, forum posts and test results. It preserves the evidence beyond the deletion of the course.

*German: Kursarchiv* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Course editor

The area where the structure of a course is edited: creating, arranging and configuring elements. Changes only take effect once they are published.

*German: Kurseditor* · [Manual](../manual_user/learningresources/Learning_path_course_Course_editor.md)

### Course element

An element that can be added to the course structure in the course editor.

*German: Kursbaustein* · [Manual](../manual_user/learningresources/Course_Elements.md)

### Course execution

The counter of how often a person has run through the same course: the first run or a repetition for recertification.

*German: Kursdurchführung* · [Manual](../manual_user/learningresources/Learning_path_course_Course_editor.md)

### Course reminders

Automatic e-mails to participants, fired by a condition in the course, for example a missing submission or an approaching deadline.

*German: Kurserinnerungen* · [Manual](../manual_admin/administration/Modules_Course_Reminders.md)

### Course statistics

The course tool that counts the accesses to the course elements and shows them as a table and a chart: per hour, per day, per weekday and per week. Counted is the click on an element in the course menu, not the click inside its content.

*German: Kurs Statistiken* · [Manual](../manual_user/learningresources/Statistics_Course.md)

### Course to-do

An open item inside a course, with a responsible person and a deadline. It appears in that person's personal to-do list as well.

*German: Kurs To-do* · [Manual](../manual_user/learningresources/Course_todos.md)

### CP learning content (Course)

A course element that shows learning content in the IMS Content Packaging format.

*German: CP-Lerninhalt* · [Manual](../manual_user/learningresources/Course_Element_CP_Learning_Content.md)

### Document (Course)

A course element that shows a single document straight in the course: a PDF, an image, an Office file or a draw.io diagram. Per role it can be set who may edit and download the document.

*German: Dokument* · [Manual](../manual_user/learningresources/Course_Element_Document.md)

### Drop box (Course)

The folder in the participant folder element where a participant uploads their files. Only they and the coaches see it.

*German: Abgabeordner* · [Manual](../manual_user/learningresources/Course_Element_Participant_Folder.md)

### Edubase (Course)

A course element that opens licensed e-books of the Edubase textbook platform in the course, optionally from a given page.

*German: Edubase* · [Manual](../manual_user/learningresources/Course_Element_Edubase.md)

### edu-sharing (Course)

A course element that shows a content item from the edu-sharing education cloud in the course. The content stays in edu-sharing and is only referenced.

*German: edu-sharing* · [Manual](../manual_user/learningresources/Course_Element_edu_Sharing.md)

### E-mail (Course)

A course element with a contact form. Participants write through it to recipients set in advance, without knowing their address.

*German: E-Mail* · [Manual](../manual_user/learningresources/Course_Element_EMail.md)

### E-mail message

The text a reminder sends: subject and body, with variables for name, course and course link.

*German: E-Mail-Benachrichtigung* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Enrolment (course element)

A course element participants use to enter themselves into course groups. It can limit places and keep a waiting list.

*German: Einschreibung* · [Manual](../manual_user/learningresources/Course_Element_Enrolment.md)

### Enrolment (concept)

The binding allocation of a topic to a participant in the topic broker. It follows the selection period, triggered automatically or by hand, and is calculated with a fair algorithm from selections and priorities.

*German: Einschreibung* · [Manual](../manual_user/learningresources/Course_Element_Topic_Broker.md)

### Enrolment process

One run of the allocation algorithm. Started by hand, several runs can be calculated and compared; the coaches accept one of them.

*German: Einschreibevorgang* · [Manual](../manual_user/learningresources/Course_Element_Topic_Broker.md)

### Exception

A deviation from the execution of a course element for particular people: by group, organisation, account, user property, passed course element or course execution number. Several exceptions are joined with "or".

*German: Ausnahme* · [Manual](../manual_user/learningresources/Learning_path_course_Course_editor.md)

### Expert mode

The view of the visibility and access tabs in which the condition is written as an expert rule: an expression of functions such as isCourseCoach(0), operators and dates.

*German: Expertenmodus* · [Manual](../manual_user/learningresources/Access_Restrictions_in_the_Expert_Mode.md)

### External page

A course element that shows an external web page in the course and ties it into the course navigation.

*German: Externe Seite* · [Manual](../manual_user/learningresources/Course_Element_External_Page.md)

### File dialog

A course element that combines the folder and the forum. Every uploaded document gets a discussion of its own.

*German: Dateidiskussion* · [Manual](../manual_user/learningresources/Course_Element_File_Dialog.md)

### Folder (Course)

A course element that offers files for download, for example course material. Coaches can also open the folder for uploads by participants.

*German: Ordner* · [Manual](../manual_user/learningresources/Course_Element_Folder.md)

### Form (Course)

A course element that embeds a form learning resource for participants to fill in. Unlike the survey the answers can be traced to a person.

*German: Formular* · [Manual](../manual_user/learningresources/Course_Element_Form.md)

### Forum (Course)

A course element for asynchronous online discussions. Participants open topics, reply to each other and subscribe to new posts.

*German: Forum* · [Manual](../manual_user/learningresources/Course_Element_Forum.md)

### GoToMeeting (Course)

A course element that embeds GoToMeeting and GoToTraining sessions into the course.

*German: GoToMeeting* · [Manual](../manual_user/learningresources/Course_Element_GoToMeeting.md)

### Highscore

The ranking of the points reached in an assessable course element. It can be shown anonymised and motivates through comparison.

*German: Rangliste* · [Manual](../manual_user/learningresources/Assessment.md)

### HTML page

A course element that shows a single HTML page with texts, images and videos. The page sits as a file in the storage folder of the course.

*German: HTML-Seite* · [Manual](../manual_user/learningresources/Course_Element_HTML_Page.md)

### Info page (Course)

The page that describes a learning resource before a person enters it, with the description, the period, the coaches and the option to book.

*German: Infoseite* · [Manual](../manual_user/learningresources/Info_page.md)

### JupyterHub (Course)

A course element that provides a Jupyter image. Participants start their own Jupyter environment for interactive computing from it.

*German: JupyterHub* · [Manual](../manual_user/learningresources/Course_Element_JupyterHub.md)

### Learning path

The ordered sequence of the course elements in a learning path course. It sets what is to be done in which order, measures the progress per element and can exempt elements for individual people.

*German: Lernpfad* · [Manual](../manual_user/learningresources/Learning_path_course_Course_editor.md)

### Learning path course

A course design that puts the course elements into an order and measures the progress per element. It steers through the learning path and exceptions, whereas the conventional course steers through conditions.

*German: Lernpfadkurs* · [Manual](../manual_user/learningresources/Learning_path_course.md)

### Life cycle

The scheduled course of a course or a group from its creation through the automatic finishing and deactivation to its deletion.

*German: Lebenszyklus* · [Manual](../manual_admin/administration/Life_cycles_-_Administration.md)

### Link list

A course element that shows an ordered collection of links in the course menu.

*German: Linkliste* · [Manual](../manual_user/learningresources/Course_Element_Link_List.md)

### LTI page

A course element that embeds an external learning application through the LTI standard. The external application can report points back, which is why the element is assessable.

*German: LTI-Seite* · [Manual](../manual_user/learningresources/Course_Element_LTI_Page.md)

### MediaSite

A course element that shows a presentation or a channel of the lecture recording system Sonic Foundry Mediasite in the course.

*German: MediaSite* · [Manual](../manual_user/learningresources/Course_Element_Mediasite.md)

### Microsoft Teams (Course)

A course element that embeds Microsoft Teams meetings into the course. OpenOlat creates the meeting and opens it for the course members.

*German: Microsoft Teams* · [Manual](../manual_user/learningresources/Course_Element_Microsoft_Teams.md)

### Notifications

A course element for course notifications. Coaches publish short messages, optionally for a limited time, and can send them by e-mail.

*German: Mitteilungen* · [Manual](../manual_user/learningresources/Course_Element_Notifications.md)

### Occasion

A set of several individually selectable appointments in the appointment scheduling, with a title, a description, organizers and a location. The occasion is either an appointment booking or an appointment finding.

*German: Anlass* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Opencast (Course)

A course element that shows video recordings from an Opencast server in the course, as a single recording or as a series.

*German: Opencast* · [Manual](../manual_user/learningresources/Course_Element_Opencast.md)

### OpenMeetings (Course)

A course element that embeds a room of the web conferencing system Apache OpenMeetings into the course.

*German: OpenMeetings* · [Manual](../manual_user/learningresources/Course_Element_OpenMeetings.md)

### Organizer

Course role. The person responsible for an occasion and shown to the participants. The course element sets whether owners, coaches or both count as organizers.

*German: Organisator:in* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Page

A course element that presents content in a block-based layout. The page is written in the content editor straight in the course and needs no file.

*German: Seite* · [Manual](../manual_user/learningresources/Course_Element_Page.md)

### Partial archive

A course archive with chosen course elements and optionally further objects such as course results or log files.

*German: Teilarchiv* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Partial elements

The steps of a course element that can be switched on, for example submission, revision and assessment in the task. Only the steps that are switched on appear to the participants.

*German: Teilbausteine* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Participant folder

A course element for exchanging files between participants and coaches. Every participant gets their own drop box and return box, seen only by them and the coaches.

*German: Teilnehmer:innen Ordner* · [Manual](../manual_user/learningresources/Course_Element_Participant_Folder.md)

### Participant list

A course element that shows the members of the course grouped by role. Which roles and which entries are visible is configurable.

*German: Liste der Teilnehmer:innen* · [Manual](../manual_user/learningresources/Course_Element_Participant_List.md)

### Participants accepted

The group of a topic in the topic assignment that lists the participants accepted for the topic.

*German: Akzeptierte Teilnehmer:innen* · [Manual](../manual_user/learningresources/Course_Element_Topic_Assignment.md)

### Participation

The entry of a person in an appointment. Participants enter and withdraw themselves, organizers can add, remove or rebook them to another appointment.

*German: Teilnahme* · [Manual](../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)

### Podcast (Course)

A course element that embeds a podcast learning resource into the course. Participants listen to or watch the episodes and can subscribe to them.

*German: Podcast* · [Manual](../manual_user/learningresources/Course_Element_Podcast.md)

### Portfolio task

A course element that assigns every participant a portfolio binder made from a template. Participants work on the binder and submit it for assessment.

*German: Portfolioaufgabe* · [Manual](../manual_user/learningresources/Course_Element_Portfolio_Task.md)

### Practice (Course)

A course element for practising. Participants answer questions from a stock of questions over and over until they have solved a set number correctly. It serves the transfer of knowledge and self-checking.

*German: Übung* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Publication

Making the changes made in the course editor visible to the participants. Until the publication the owners work on the course without disturbing the running operation.

*German: Veröffentlichung* · [Manual](../manual_user/learningresources/Using_additional_Course_Editor_Tools.md)

### Questionnaire (Course)

A course element that embeds a test learning resource (QTI 2.1) configured as a questionnaire. The answers are analysed anonymously.

*German: Fragebogen*

### Recipients

Who receives the reminder. Either the course member the rules apply to, or specified recipients only, instead of that person.

*German: Empfänger:innen* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Reminder (Course)

An automatic e-mail set up in a course. It goes to a course member as soon as all of its rules are met, and once per person only.

*German: Erinnerung* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Resource folder

A learning resource that stores files for several courses in one place. Instead of copying the same file into every course, the courses embed the resource folder.

*German: Ressourcenordner* · [Manual](../manual_user/learningresources/Resource_Folder.md)

### Responsible for the topic

The group of a topic in the topic assignment that lists the coaches responsible for the topic.

*German: Zuständig für dieses Thema* · [Manual](../manual_user/learningresources/Course_Element_Topic_Assignment.md)

### Return box (Course)

The folder in the participant folder element where coaches return files to a participant.

*German: Rückgabeordner* · [Manual](../manual_user/learningresources/Course_Element_Participant_Folder.md)

### Rule

A criterion that must be met before a reminder goes out, for example the enrolment date or the course status. Several rules are always joined with "and".

*German: Bedingung* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Sample solution (Course)

The sample solution of a task, which the coaches only release once the submission deadline has passed.

*German: Musterlösung* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### SCORM 1.2 (Course)

A course element that plays a SCORM 1.2 package. The package reports progress and points back, which is why the element is assessable.

*German: SCORM 1.2* · [Manual](../manual_user/learningresources/Course_Element_SCORM_Learning_Content.md)

### Selection (course element)

A course element with which participants pick a set number of course elements below it themselves. Only the ones they picked appear in their course menu afterwards. It can only be used in learning path courses.

*German: Auswahl* · [Manual](../manual_user/learningresources/Course_Element_Selection.md)

### Selection (concept)

The choice of a topic by a participant in the topic broker, with a priority. From the selections of all persons OpenOlat calculates the enrolment.

*German: Auswahl* · [Manual](../manual_user/learningresources/Course_Element_Topic_Broker.md)

### Self-test (Course)

A course element that embeds a test learning resource for self-checking. The result does not feed into the course assessment and cannot be seen by the coaches.

*German: Selbsttest* · [Manual](../manual_user/learningresources/Course_Element_Self_Test.md)

### Sent reminder

The log entry for a reminder that actually went out, with recipient, send time and status. It is what prevents a second delivery to the same person.

*German: Versendete Erinnerung* · [Manual](../manual_user/learningresources/Course_Reminders.md)

### Simple mode

The view of the visibility and access tabs with predefined check boxes: blocked for learners, depending on date, group or assessment, only in assessment mode.

*German: Einfacher Modus* · [Manual](../manual_user/learningresources/General_Configuration_of_Course_Elements.md)

### SMS reminders

Reminders as a text message instead of an e-mail. They depend on an SMS provider and are switched on separately in the administration.

*German: SMS Erinnerungen*

### Storage folder

The file area of a course where the files of the course sit. Participants do not see it; they reach the files only through the course elements.

*German: Ablageordner* · [Manual](../manual_user/learningresources/Storage_folder.md)

### Structure

A course element that structures the course menu into chapters. It combines the assessments of the elements below it into one overall assessment.

*German: Struktur* · [Manual](../manual_user/learningresources/Course_Element_Structure.md)

### Survey

A course element that embeds a form learning resource as a survey. The answers are analysed anonymously.

*German: Umfrage* · [Manual](../manual_user/learningresources/Course_Element_Survey.md)

### Topic

A selectable topic in the topic broker, with a title, a description, a minimum and maximum number of participants, an optional execution period and a group restriction. Participants pick several topics and rank them by priority.

*German: Thema* · [Manual](../manual_user/learningresources/Course_Element_Topic_Broker.md)

### Topic assignment

A course element for advertising, assigning and supervising topics. Coaches advertise topics, participants apply for them and the coaches hand out the places.

*German: Themenvergabe* · [Manual](../manual_user/learningresources/Course_Element_Topic_Assignment.md)

### Topic broker

A course element participants use to sign up for working on particular topics themselves.

*German: Themenbörse* · [Manual](../manual_user/learningresources/Course_Element_Topic_Broker.md)

### Trash (Course)

The area deleted learning resources are moved to first. From there they can be restored, until they are deleted for good.

*German: Papierkorb* · [Manual](../manual_user/learningresources/Access_configuration.md)

### Unpublished changes

Changes in the course editor that are not published yet and that the participants therefore do not see.

*German: Nicht publizierte Änderungen* · [Manual](../manual_user/learningresources/Using_additional_Course_Editor_Tools.md)

### Video (Course)

A course element that plays a video learning resource, together with the elements added in OpenOlat such as quiz questions, comments, segments and annotations.

*German: Video* · [Manual](../manual_user/learningresources/Course_Element_Video.md)

### Video live stream

A course element that shows up to two live streams in a set time window, single or side by side. The administration sets up the stream addresses as URL templates.

*German: Video Livestream* · [Manual](../manual_user/learningresources/Course_Element_Video_Livestream.md)

### Video task (Course)

A course element in which participants mark places in a video and assign categories to them. It serves the observation and judgement of situations in the video.

*German: Videoaufgabe* · [Manual](../manual_user/learningresources/Course_Element_Video_Task.md)

### vitero (Course)

A course element that embeds booked vitero team rooms into the course.

*German: vitero* · [Manual](../manual_user/learningresources/Course_Element_vitero.md)

### Wiki (Course)

A course element that embeds a wiki learning resource into the course so that participants write content together.

*German: Wiki* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

### Zoom (Course)

A course element that embeds a Zoom meeting into the course through LTI. Participants join from inside the course.

*German: Zoom* · [Manual](../manual_user/learningresources/zoom/index.md)

## Collaboration

Groups and the tools people work with inside them, plus everything that tells users about what is new.

### Activities

The complete list of the actions in a project, with the person and the point in time. It makes it traceable who changed what.

*German: Aktivitäten* · [Manual](../manual_user/area_modules/Project_Timeline.md)

### Activity

A single action in the project, for example creating a note or changing an event.

*German: Aktivität* · [Manual](../manual_user/area_modules/Project_Timeline.md)

### Alias

A self-chosen name a person writes under in a forum. The alias hides the real name from the other participants, not from the coaches.

*German: Pseudonym* · [Manual](../manual_user/learningresources/Course_Element_Forum.md)

### Article

The content part of a wiki page, as opposed to its discussion and its version history.

*German: Artikel* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

### Calendar (Collaboration)

A calendar with events. OpenOlat keeps personal, course and group calendars apart and shows them layered. Calendars can be subscribed to from an external calendar program.

*German: Kalender* · [Manual](../manual_user/personal_menu/Calendar.md)

### Catalog (Collaboration)

The folder structure of the library as readers see it. It is the content of the resource folder chosen as the library in the administration.

*German: Katalog* · [Manual](../manual_user/area_modules/Library.md)

### Chat

Short messages in real time between signed-in people, one to one or in the room of a course or a group.

*German: Chat* · [Manual](../manual_user/basic_concepts/Chat.md)

### Chatroom

A chat room belonging to a course or a group. All members can enter it without writing to each other one by one.

*German: Chatraum* · [Manual](../manual_user/basic_concepts/Chat.md)

### Collaborative tools

The tools switched on individually for a group: information for members, e-mail, calendar, folder, forum, chat, wiki, portfolio and the virtual classrooms. Tools that are switched off do not appear in the group.

*German: Kollaborative Werkzeuge* · [Manual](../manual_user/groups/Group_Administration.md)

### Decision (Collaboration)

A decision recorded in the project, with a date and a justification. It keeps a traceable record of what was decided and why.

*German: Entscheid* · [Manual](../manual_user/area_modules/Project_Decisions.md)

### Discussion

The discussion on a wiki page. It keeps the conversation about the content apart from the content itself.

*German: Diskussion* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

### Document pool (Collaboration)

The module for a document collection structured by the taxonomy. Permissions are granted per taxonomy level, which makes it suitable for documents of differing confidentiality.

*German: Dokumentenpool* · [Manual](../manual_admin/administration/Modules_Document_pool.md)

### E-mail (tool)

The group tool with which members of a group write an e-mail to all or selected coaches and participants. It is a contact form, not a mailbox.

*German: E-Mail* · [Manual](../manual_user/groups/Group_Administration.md)

### E-mail (concept)

A message OpenOlat sends or receives: notifications, reminders, messages from the E-mail course element and from the members management.

*German: E-Mail* · [Manual](../manual_user/learningresources/Course_Element_EMail.md)

### Event (Collaboration)

An entry in a calendar with title, start, end, location, description and links. It sits in the personal, the course or the group calendar and can recur.

*German: Termin* · [Manual](../manual_user/personal_menu/Calendar.md)

### Externally managed groups

Groups that an external system creates and maintains, for example the fxSyncher through the REST interface. Managed properties such as title, members or tools are locked in OpenOlat; administrators can override the lock.

*German: Extern verwaltete Gruppen* · [Manual](../manual_admin/administration/REST_API.md)

### Files (collaboration.files)

The files of a course, a group or a project, stored together and searchable together.

*German: Dateien* · [Manual](../manual_user/area_modules/Project_Files.md)

### Files (collaboration.project_files)

The file area of a project. Files can be uploaded, created in the project or taken over from other areas of OpenOlat.

*German: Dateien* · [Manual](../manual_user/area_modules/Project_Files.md)

### Folder (Collaboration)

A folder for files, with permissions per folder, versioning and access through WebDAV.

*German: Ordner* · [Manual](../manual_user/learningresources/Course_Element_Folder.md)

### Forum (Collaboration)

An area for asynchronous discussions. Posts stay readable for good, can be searched and can be subscribed to.

*German: Forum* · [Manual](../manual_user/learningresources/Course_Element_Forum.md)

### Group

A group of people who work together, with members, tools and a lifecycle of their own. It can exist inside a course or independently of any course in the Groups area.

*German: Gruppe* · [Manual](../manual_user/groups/index.md)

### Group life cycle

The scheduling of a group. It sets when a group automatically becomes inactive, when it is deleted and who is warned beforehand.

*German: Gruppen-Lebenszyklus* · [Manual](../manual_admin/administration/Automatic_Group_Lifecycle.md)

### Group management

The area for group managers in the Groups menu. It shows all groups of the system, other people's included, and allows editing, merging, inactivating and deleting any group.

*German: Gruppenverwaltung* · [Manual](../manual_user/area_modules/Group_Management.md)

### ICal feed link

The personal address under which an OpenOlat calendar can be fetched in the iCal format. A foreign calendar program subscribes to the calendar through this address and shows the events there.

*German: iCal Feed-Link* · [Manual](../manual_user/personal_menu/Calendar.md)

### Information for members

The group tool for messages to all members of a group. Coaches or, depending on the setting, all members write the messages; subscribers receive them by e-mail.

*German: Information an Mitglieder* · [Manual](../manual_user/groups/Group_Administration.md)

### Instant Messaging

The module for short messages in real time. It shows who is signed in and allows conversations between single people as well as in course and group rooms.

*German: Instant-Messaging* · [Manual](../manual_admin/administration/Instant_Messaging.md)

### Invitations (Collaboration)

Access for external people without an account. The invited person gets access to a single resource through a link, and their account expires with the invitation.

*German: Einladungen* · [Manual](../manual_user/learningresources/Members_management.md)

### Learning area

A named grouping of several course groups. A condition in the course then addresses the learning area instead of every group one by one.

*German: Lernbereich* · [Manual](../manual_user/learningresources/Learning_Areas.md)

### Learning groups

A group inside a course. It steers who sees which course elements and is the unit participants enter themselves into through the enrolment.

*German: Lerngruppen* · [Manual](../manual_user/learningresources/Members_management.md)

### Library (Collaboration)

The module for a shared document collection of the whole system. People submit documents, an administrative body releases them, and afterwards everybody can read them.

*German: Bibliothek* · [Manual](../manual_user/area_modules/Library.md)

### List of calendars

The list of all calendars a person sees layered in the personal calendar: their own, the course and group calendars and imported calendars. Display and colour can be chosen per calendar.

*German: Kalenderliste* · [Manual](../manual_user/personal_menu/Calendar.md)

### Members

The people of a group with their roles. Coaches manage the members, invite people and keep the waiting list.

*German: Mitglieder* · [Manual](../manual_user/learningresources/Members_management.md)

### Message

The text of a message or e-mail that OpenOlat sends.

*German: Nachricht*

### Milestone

An event in the project that can be marked as reached. It shows whether an intermediate goal is done.

*German: Meilenstein* · [Manual](../manual_user/area_modules/Project_Schedule.md)

### News

The collected changes from all subscriptions of a person, as a list under Subscriptions and as a portlet on the start page. The list shows the latest change per resource in the chosen period.

*German: Neuigkeiten* · [Manual](../manual_user/personal_menu/Subscriptions.md)

### Note

A note in the project. It holds text that all project members can read and edit, and it can be linked to other objects of the project.

*German: Notiz* · [Manual](../manual_user/area_modules/Project_Notes.md)

### Notes

Personal notes on a course. Only the person writing them sees them, and they are kept after leaving the course.

*German: Notizen* · [Manual](../manual_user/personal_menu/Notes.md)

### Notification

A message about a change a person has subscribed to. OpenOlat collects the notifications and sends them bundled as an e-mail.

*German: Benachrichtigung* · [Manual](../manual_user/personal_menu/Subscriptions.md)

### Personal RSS Feed

An RSS feed with the news from all subscriptions of a person. An RSS reader fetches it through a personal address, without signing in to OpenOlat.

*German: Persönlicher RSS-Feed* · [Manual](../manual_user/personal_menu/Subscriptions.md)

### Post

A single post in a forum, with text, attachments and a note of which post it replies to.

*German: Beitrag* · [Manual](../manual_user/learningresources/Course_Element_Forum.md)

### Project

The module for the project work of a group of people, with events, milestones, to-dos, decisions, notes, files and a whiteboard in one place. Unlike the course it teaches no content and assesses nobody.

*German: Projekt* · [Manual](../manual_user/area_modules/Project_Whiteboard.md)

### Published groups

Groups with an offer that people join themselves in the Groups area. The offer is freely available, protected by an access code or paid; when the group is full the waiting list takes over.

*German: Veröffentlichte Gruppen* · [Manual](../manual_user/groups/Group_Administration.md)

### Quick start

The area at the start of a project that shows the six most recently used files and notes and offers the upload directly.

*German: Schnellzugriff* · [Manual](../manual_user/area_modules/Project_Notes.md)

### Schedule

The schedule of a project with single events, recurring events and milestones. The events appear in the personal calendar of the members as well.

*German: Terminplan* · [Manual](../manual_user/area_modules/Project_Schedule.md)

### Subscription

Signing up to changes on an object. OpenOlat collects the changes and sends them bundled as an e-mail to the subscriber.

*German: Abonnement* · [Manual](../manual_user/personal_menu/Subscriptions.md)

### Thread

A line of discussion in a forum. It starts with an opening post that further posts reply to.

*German: Diskussionsthema* · [Manual](../manual_user/learningresources/Course_Element_Forum.md)

### Timeline (Collaboration)

The chronological overview of everything that has happened in the project. It shows events, decisions, notes and files in one strand.

*German: Timeline* · [Manual](../manual_user/area_modules/Project_Timeline.md)

### Whiteboard

A shared drawing surface in the project that several people work on at the same time. It is based on draw.io.

*German: Whiteboard* · [Manual](../manual_user/area_modules/Project_Whiteboard.md)

### Wiki (Collaboration)

An area for pages that several people write together and link to each other. Every change is versioned and can be undone.

*German: Wiki* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

### Wiki page

A single page inside a wiki. It comes into being as soon as a link to a name that does not exist yet is created.

*German: Wiki-Seite* · [Manual](../manual_user/learningresources/Course_Element_Wiki.md)

## Tasks and practice

Everything where learners submit, revise or practise something, and the workflow the coaches go through for it.

### Assessment (Tasks and practice)

The step in which coaches assess the submitted work and award points, a status or a grade.

*German: Bewertung* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Assignment (Tasks and practice)

The step in which the participant receives their assignment. It is assigned to them or chosen by them from a list.

*German: Aufgabenstellung* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Assignment coaches/participants

The workflow setting that assigns one coach to every participant, manually or automatically. The assigned coach then assesses these submissions and is notified about new ones.

*German: Zuweisung Betreuende/Teilnehmende* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Challenge

An intermediate goal made up of several practice series. After finishing a challenge the participant sees their ranking and their learning status statistics.

*German: Challenge* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Correction request

The coaches' request to revise a submitted solution. It starts another round of revision.

*German: Korrekturanforderung* · [Manual](../manual_user/learningresources/Assessment.md)

### Drop box (Tasks and practice)

The folder inside a task element where a participant uploads their work. Only they and the coaches see it.

*German: Abgabeordner*

### Group task

A course element with the same task workflow as the task, but for groups. A group submits together and receives one assessment.

*German: Gruppenaufgabe* · [Manual](../manual_user/learningresources/Course_Element_Grouptask.md)

### Late submission

The setting that allows a submission after the deadline up to a second date. Such submissions carry the marking Late, and coaches see the delay in the assessment tool.

*German: Verspätete Abgabe* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Learning status

A person's standing per question, expressed as a level. Answering a question correctly three times in a row reaches level 3; a wrong answer lowers the level again. Progress can be read off this way without points.

*German: Lernstand* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Level

The compartment of the flashcard file in the practice. Every right answer raises a question by one level, a wrong one lowers it by one; the configuration sets the number of levels.

*German: Level* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Peer review

The step in which participants review the work of other participants and give them feedback. OpenOlat distributes who gets whose work.

*German: Peer-Review* · [Manual](../manual_how-to/peer_review/peer_review.md)

### Practice (Tasks and practice)

A course element for practising on the flashcard principle. Participants answer questions from test learning resources or from shares of the question bank in practice series; wrongly answered questions come back. It awards no points, coaches see the learning status as levels.

*German: Übung* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Practice series

A block of questions a participant works through in one go, for example ten questions. The configuration sets the number.

*German: Übungsserie* · [Manual](../manual_user/learningresources/Course_Element_Practice.md)

### Quality feedback for reviewer

The peer review setting with which participants judge a review they received: whether it was helpful, with thumbs or stars.

*German: Qualitäts-Feedback für Reviewer:in* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Return and feedback

The step in which the coaches return the corrected work and their feedback to the participant.

*German: Rückgabe und Feedback* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Return box (Tasks and practice)

The folder inside a task element where coaches return the corrected work to the participant.

*German: Rückgabeordner*

### Review object

The work of another participant that is to be reviewed in the peer review.

*German: Review-Objekt* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Revision

The step in which the participant revises their solution after feedback and submits it again. It can be run through several times.

*German: Überarbeitung* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Sample solution (Tasks and practice)

The sample solution of a task, stored as a document. It becomes visible from a set date, for all participants or only for those whose submission was accepted.

*German: Musterlösung* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Segment (Tasks and practice)

A stretch of the video that holds a situation to be judged. Segments are set in the video editor of the learning resource.

*German: Segment* · [Manual](../manual_user/learningresources/Course_Element_Video_Task.md)

### Submission

The step in which the participant uploads their solution or writes it straight in the browser. After the submission date no submission is possible any more.

*German: Abgabe* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Task

The course element for a task workflow with configurable steps: assign the task, submit the solution, revise it, assess it and release the sample solution. Every participant works on their own.

*German: Aufgabe* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

### Term (Tasks and practice)

A term participants assign to a segment. The terms form the grid the video is observed by.

*German: Begriff* · [Manual](../manual_user/learningresources/Course_Element_Video_Task.md)

### Video task (Tasks and practice)

A course element in which participants mark places in a video and assign terms to them. It serves the observation and judgement of situations, for example in teacher training or in nursing.

*German: Videoaufgabe* · [Manual](../manual_user/learningresources/Course_Element_Video_Task.md)

### Workflow

The sequence of steps a task goes through. Every step can be switched on individually, so that everything from a plain submission to the full run with revision and peer review is possible.

*German: Workflow* · [Manual](../manual_user/learningresources/Course_Element_Task.md)

## Events and absences

Classroom operation: when something takes place, who was present and how an absence is handled.

### Absence

A person missing an event. It counts as authorized or not authorized, depending on whether a recognised reason has been given.

*German: Absenz* · [Manual](../manual_user/personal_menu/Absences.md)

### Absence list

The printable list of the recorded absences of an event, per participant and unit. It is produced from the event's menu after the roll call.

*German: Absenzenliste* · [Manual](../manual_user/area_modules/Coaching_Events_Absences.md)

### Absence management

The entry in the main navigation for handling absences across courses by absence managers: cockpit, events, absences, notices, appeals, user search and report over all courses.

*German: Absenzenverwaltung* · [Manual](../manual_user/area_modules/Absence_Management.md)

### Appeal

A person's objection against a recorded absence. It is only possible within the appeal period.

*German: Rekurs* · [Manual](../manual_user/personal_menu/Absences.md)

### Attendance

The record that a person took part in an event. It is recorded per unit and condensed into the attendance rate.

*German: Anwesenheit* · [Manual](../manual_user/learningresources/Events_and_absences.md)

### Attendance list

The printable list of the participants of an event with a column for the signature. It is signed before or during the event and proves attendance on paper.

*German: Präsenzliste* · [Manual](../manual_user/area_modules/Coaching_Events_Absences.md)

### Building

A building that rooms belong to. It carries a reference, an address with a map, a colour for lists and calendars and the restriction to particular organisations.

*German: Gebäude* · [Manual](../manual_admin/administration/Modules_Rooms.md)

### Dispensation

The advance exemption from the attendance requirement for a period. The units concerned do not count against the attendance rate.

*German: Dispens* · [Manual](../manual_user/personal_menu/Absences.md)

### Event (Events and absences)

A schedulable teaching unit of 1 to 12 units, with a date, a room and lecturers. It is the unit attendance is recorded for.

*German: Termin* · [Manual](../manual_user/learningresources/Toolbar_Events.md)

### Events and absences

The module for classroom operation: events with teachers and units, the roll call per event and the resulting absences, notices and appeals. The administration switches it on system-wide and sets the defaults, course owners activate it per course in the settings under Execution.

*German: Termine und Absenzen* · [Manual](../manual_admin/administration/Modules_Events_and_Absences.md)

### Multi-absence recording

Recording the attendance for several events in one pass instead of event by event.

*German: Multi-Absenzenerfassung*

### Notice

The entry that reports an absence for a period or for particular events: as a notice of absence, as a dispensation or as an absence without notification. Notices are recorded by participants themselves, by teachers or by absence managers.

*German: Meldung* · [Manual](../manual_user/area_modules/Coaching_Events_Absences.md)

### Notice of absence

The advance notice that a person will miss an event. It is given before the event, the absence is established afterwards.

*German: Abmeldung* · [Manual](../manual_user/personal_menu/Absences.md)

### Online meeting (Events and absences)

The link between an event and an online session in BigBlueButton, in Microsoft Teams or through the meeting link of another provider. Participants enter the session straight from the event.

*German: Online Meeting* · [Manual](../manual_user/learningresources/Events_and_absences.md)

### Reason of absence

The classification of an absence maintained by the administration, for example illness or accident. It is chosen from a list on the absence or notice and has a say in whether the absence is authorized.

*German: Absenzenbegründung* · [Manual](../manual_admin/administration/Modules_Events_and_Absences.md)

### Reasons events

The list of reasons maintained by the administration for closing an event with a deviation, for example ended early. When closing, teachers choose a reason from the list; without entries the selection does not appear.

*German: Begründungen Termine* · [Manual](../manual_admin/administration/Modules_Events_and_Absences.md)

### Roll call

The recording of attendance per participant and per unit of an event by the teachers. It can be switched on per course and yields the absences the attendance rate is built from.

*German: Anwesenheitskontrolle* · [Manual](../manual_user/learningresources/Toolbar_Events.md)

### Room

A physical room in a building, with a reference, a number of seats, additional information and an occupancy. Events book it; an inactive room can no longer be booked.

*German: Raum* · [Manual](../manual_admin/administration/Modules_Rooms.md)

### Room booking

The occupancy of a room by an event, with start, end and an optional buffer before and after. It comes into being when a room is assigned to an event and appears in room scheduling with its warnings.

*German: Raumbuchung* · [Manual](../manual_user/area_modules/Course_Planner_Rooms.md)

### Room management

The Room management area in the Course Planner: a read-only view of room scheduling and of the rooms of one's own organisations. Buildings and rooms are not maintained here but in the administration in the Rooms module.

*German: Raumverwaltung* · [Manual](../manual_user/area_modules/Course_Planner_Rooms.md)

### Rooms

The module for the physical rooms: buildings, rooms with a number of seats and their booking by events. The administration maintains buildings and rooms, room scheduling shows all bookings; without the module no rooms can be booked on events.

*German: Räume* · [Manual](../manual_admin/administration/Modules_Rooms.md)

### Room scheduling

The overview of all room bookings, with filters and a calendar view. It reports double bookings, too few seats and inactive rooms as a warning.

*German: Raumplanung* · [Manual](../manual_user/area_modules/Course_Planner_Rooms.md)

## ePortfolio

How learners document their learning processes, reflect on them and share them for feedback: the binder with its sections, entries and assignments, the access control, the evaluation with the form and the assessment by coaches.

### Assessment (ePortfolio)

The coaches' judgement on a binder: points and passed per section, entered in the binder's Assessment tab. The result flows into the portfolio task course element and thus into the course's assessment tool. Single entries are not assessed, only commented on.

*German: Bewertung* · [Manual](../manual_user/learningresources/Portfolio_assignment_Grading.md)

### Assignment (ePortfolio)

A brief in a section of the binder, set by the template: an essay, a document or a form. The learner picks the assignment for editing and answers it with an entry.

*German: Aufgabe* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### Binder

The collection in which a person organises their portfolio work: a binder is divided into sections, and every section holds entries and assignments. It comes into being empty, from a template, from existing entries or by collecting a portfolio task in a course. The owning person shares it, wholly or in parts, for commenting and assessment.

*German: Mappe* · [Manual](../manual_user/portfolio/Three_steps_to_your_portfolio_binder.md)

### Comments

Feedback below an entry. Shared persons with comment rights write them once the entry is published; administration sets whether comments are visible in the overview and in the entries.

*German: Kommentare* · [Manual](../manual_user/learningresources/Portfolio_assignment_Grading.md)

### Entry (ePortfolio)

A page in a binder, built with the content editor from text, images, videos, documents and forms. An entry answers an assignment or stands on its own. The person writes it as a draft and publishes it; after that it can no longer be edited, only commented on.

*German: Eintrag* · [Manual](../manual_user/portfolio/Three_steps_to_your_portfolio_binder.md)

### ePortfolio

The module learners use to document and reflect on their learning processes. It gives every person binders, sections and entries, and the portfolio task course elements distribute binders from a template through it. Administration switches it on or off under e-Assessment.

*German: ePortfolio* · [Manual](../manual_admin/administration/eAssessment_ePortfolio.md)

### Evaluation (ePortfolio)

The filled-in form of an assignment of type form. The person evaluates themselves, and depending on the setting shared persons give an external evaluation, openly or anonymously; the comparison sets several evaluations side by side.

*German: Einschätzung* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### External evaluation

The evaluation a shared person gives on another person's assignment. It is only possible if the assignment allows it, and it can be anonymous.

*German: Fremdeinschätzung* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### Floating entry

An entry that is assigned to no binder. It is created under My entries, can later be imported into a binder and, without a share, is visible to the person alone.

*German: Floating Eintrag* · [Manual](../manual_user/area_modules/My_entries.md)

### History

The tab of a binder that lists all changes in chronological order, the newest at the top. Administration can switch it off.

*German: Änderungsprotokoll* · [Manual](../manual_user/area_modules/My_portfolio_binders.md)

### My entries

The list of all of a person's own entries in chronological order, independent of the binder. It shows the status of every entry, offers a list view and a table view and the timeline. Not the tab of the same name in the authoring area, which lists one's own learning resources.

*German: Meine Einträge* · [Manual](../manual_user/area_modules/My_entries.md)

### My portfolio binders

The list of all of a person's own binders under Portfolio 2.0. Here the person creates new binders: empty, from a template, from a course's portfolio task or from existing entries. Binders collected from a course carry a red side stripe and the course name.

*German: Meine Portfoliomappen* · [Manual](../manual_user/area_modules/My_portfolio_binders.md)

### Portfolio 2.0

The entry Portfolio 2.0 in the personal menu. It leads to the person's own binders, own entries, the media center, the shares and the trash.

*German: Portfolio 2.0* · [Manual](../manual_user/personal_menu/Portfolio.md)

### Portfolio template

The binder that authors build in the learning resource Portfolio 2.0 template: sections with assignments, dates and settings. Every person who collects the portfolio task or books the template receives their own copy of it; changes to the template are synchronised into the copies.

*German: Portfoliovorlage* · [Manual](../manual_user/learningresources/Portfolio_template_Creation.md)

### Section (ePortfolio)

A chapter of a binder. A section carries a title, a summary, a begin date and an end date, and it holds entries and assignments; there are no subsections. Coaches close a section and assess it with points and passed.

*German: Bereich* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### Self evaluation

The evaluation the owning person gives on their own assignment. It is possible with every form; whether invitees see it is set by the assignment, and only after their own external evaluation.

*German: Selbsteinschätzung* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### Shared by me

The list of the person's own binders that they have shared with others. It shows who may access which binder and leads to the binder's access control to change rights.

*German: Von mir freigegeben* · [Manual](../manual_user/area_modules/Shared_by_me.md)

### Shared with me

The list of binders and entries other people have shared with the logged-in person. Coaches find their learners' binders here in the tabs Favorites, Entries / To do and Binders and comment on, assess or close them.

*German: An mich freigegeben* · [Manual](../manual_user/area_modules/Shared_with_me.md)

### Sharing

The tab of a binder in which the owning person grants access rights. They choose course participants, course coaches, course owners or invite external persons by e-mail, set the shared sections and entries and the level: read, comment, assess. Without a share even course coaches do not see a binder collected from the course.

*German: Freigabe* · [Manual](../manual_user/learningresources/Portfolio_task_and_assignment_Collecting_and_editing.md)

### Template (ePortfolio)

A document or form in the template folder of a binder from which users create a new entry. The template folder is a setting of the portfolio template; if it is mandatory, new entries come only from a template.

*German: Vorlage* · [Manual](../manual_user/learningresources/Portfolio_template_Administration_and_editing.md)

### Timeline (ePortfolio)

The graphical overview of the activities under My entries. Coloured dots show when an entry was edited and which status it has; administration can switch the timeline off.

*German: Zeitstrahl* · [Manual](../manual_user/area_modules/My_entries.md)

### Trash (ePortfolio)

The place for a person's deleted binders and entries in Portfolio 2.0. From there they can be restored or deleted for good.

*German: Papierkorb*

## Testing and question bank

How an exam is built, run, corrected and analysed, and where the questions come from.

### Additional sheet

An extra sheet in the printout of a test that gives the candidate room for side calculations and notes.

*German: Zusätzliche Seite* · [Manual](../manual_user/learningresources/Test_settings.md)

### Answer

One answer option of a question. It is stored as right or wrong and carries the points that choosing it brings.

*German: Antwort* · [Manual](../manual_user/learningresources/Configure_test_questions.md)

### Correction tool

The tool in which coaches or correctors correct the manually assessed questions of a test: award points and leave comments, question by question or person by person.

*German: Korrekturwerkzeug* · [Manual](../manual_user/learningresources/Assessing_tests.md)

### Correct solution

The right answer of a question, stored as feedback. The candidate sees it automatically after a wrong answer; for essay, upload file and drawing it serves the correctors as a reference.

*German: Korrekte Lösung* · [Manual](../manual_user/learningresources/Configure_test_questions.md)

### Drag and Drop

A question type like the matrix but with dragging instead of ticking. The candidate drags the terms into the matching categories.

*German: Drag and Drop* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Drawing

A question type in which the candidate works on a given background image with drawing tools. It has to be assessed manually.

*German: Zeichnen* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Essay

A question type with a free text field. The candidate writes the answer themselves, which is why the question has to be assessed manually.

*German: Freitext* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Feedback

A text the candidate sees after answering. It can be stored separately for the right answer, the wrong answer and single answer options.

*German: Feedback* · [Manual](../manual_user/learningresources/Configure_test_questions.md)

### Gap FIB numerical

A question type like the gap text but for numbers only. A permitted tolerance can be set for every gap.

*German: Lückentext numerisch* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Gap FIB text

A question type with a running text that has gaps built into it. The candidate types the missing text in.

*German: Lückentext* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Gap mixed

A question type that combines text gaps, numerical gaps and dropdown gaps in one running text. It can hold a calculation and its justification in a single question, for example.

*German: Lückentext gemischt* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Gap with dropdown

A question type that combines the gap text with single choice. Instead of typing, the candidate picks the content of the gap from a dropdown.

*German: Lückentext mit Dropdown* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Hotspot

A question type with an image that has areas defined on it. The candidate clicks the areas that apply, either one or several.

*German: Hotspot* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Hottext

A question type in which single terms in a running text can be marked. The candidate picks the terms that apply in the text.

*German: Hottext* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Kprim

A question type with exactly four statements. The candidate decides for each statement whether it applies. Zero to four statements can be right, and the point scheme is fixed.

*German: Kprim* · [Manual](../manual_user/learningresources/Test_question_types.md)

### List

A personal collection of questions in the question bank with which a person orders their own questions. The list changes nothing about who sees a question.

*German: Liste* · [Manual](../manual_user/area_modules/Question_bank_possible_operations.md)

### Match

A question type with rows and columns. Per row the candidate ticks which column applies, either as single choice or as multiple choice.

*German: Matrix* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Multiple choice (Testing and question bank)

A question type with at least two answer options, of which several can be chosen and several can be right.

*German: Multiple Choice* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Order

A question type in which the candidate drags texts or images into the right order.

*German: Reihenfolge* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Pool

A collection in the question bank that questions are shared into so that others see them and take them into their own tests. Question bank managers create the pools; usually there is one public pool.

*German: Pool* · [Manual](../manual_user/area_modules/Question_Bank_Administration.md)

### Question

A single question in a test, in a questionnaire or in the question bank. It carries the question text, the answer options, the points and the feedback.

*German: Frage* · [Manual](../manual_user/learningresources/Configure_test_questions.md)

### Question bank (Testing and question bank)

The area where questions are collected, tagged, released and reviewed independently of a single test. The same question can be used in several tests this way.

*German: Fragenpool* · [Manual](../manual_user/area_modules/Question_Bank.md)

### Questionnaire (Testing and question bank)

The course element that embeds a test learning resource (QTI 2.1) configured as a questionnaire. It collects opinions instead of knowledge and analyses the answers anonymously.

*German: Fragebogen* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Question type

The kind of a question. The question type determines how the candidate answers, how the points are calculated and whether OpenOlat can assess automatically.

*German: Fragetyp* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Results

The evaluation of a test attempt that the candidate sees after submitting or on the test start page. The setting "Overview results" decides how detailed: from the test summary down to question, answer and solution.

*German: Resultate* · [Manual](../manual_user/learningresources/Course_Element_Test.md)

### Review process

The quality process of the question bank. Peers rate a new question with stars; it goes through the statuses Draft, Review, Revision where needed, and Final before it may be used in tests.

*German: Beurteilungsprozess* · [Manual](../manual_user/area_modules/Question_Bank_Review_Process.md)

### Section (Testing and question bank)

A level of structure inside a test part. The section bundles questions into a block and can draw a random selection from it, so that not all candidates get the same questions.

*German: Sektion* · [Manual](../manual_user/learningresources/Configure_tests.md)

### Self-test (Testing and question bank)

The course element that embeds a test learning resource for self-checking. The result does not feed into the course assessment, the results are stored anonymised, and the number of runs is unlimited.

*German: Selbsttest* · [Manual](../manual_user/learningresources/Course_Element_Self_Test.md)

### Shares (Testing and question bank)

Sharing questions of the question bank with a group or a pool. It decides who sees a question and may take it into their own tests.

*German: Freigaben* · [Manual](../manual_user/area_modules/Question_Bank.md)

### Single choice (Testing and question bank)

A question type with several answer options, of which exactly one can be chosen and exactly one is right.

*German: Single Choice* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Supervisor chat

A chat during an exam. Candidates ask their questions in it, the supervisor answers.

*German: Betreuer:innen-Chat* · [Manual](../manual_how-to/communication_during_exam/communication_during_exam.md)

### Test (Testing and question bank)

The course element that embeds a test learning resource into the course. The result counts towards the course assessment.

*German: Test* · [Manual](../manual_user/learningresources/Course_Element_Test.md)

### Test part

The top level of structure of a test. A test part bundles sections and sets for all of them together whether the candidate may go back and change answers.

*German: Test-Part* · [Manual](../manual_user/learningresources/Configure_tests.md)

### Test receipt

A digitally signed confirmation of a completed test attempt. It proves later what was submitted at what time.

*German: Testquittung* · [Manual](../manual_how-to/achievements/achievements.md)

### Test run

One person's run through a test, from the first question to the submission. It holds the answers, the duration and the points.

*German: Testversuch* · [Manual](../manual_user/learningresources/Assessing_tests.md)

### Test Statistics

The analysis of a test that has been taken: figures per question, discrimination index, difficulty and the distribution of the results.

*German: Test Statistiken* · [Manual](../manual_user/learningresources/Statistics_Test.md)

### True/false

A question type like Kprim but with any number of rows. Per statement the candidate chooses between unanswered, true and false.

*German: True/false* · [Manual](../manual_user/learningresources/Test_question_types.md)

### Upload file (Testing and question bank)

A question type in which the candidate uploads one or more files as the answer. It has to be assessed manually.

*German: Datei hochladen* · [Manual](../manual_user/learningresources/Test_question_types.md)

## Assessment

Everything that records a performance, assesses it, turns it into a grade and releases it.

### Assessment (Assessment)

The judgement on a person's performance in an assessable course element, expressed as a status, points or a grade. It judges people; quality management judges offerings instead.

*German: Bewertung* · [Manual](../manual_user/learningresources/Course_Element_Assessment.md)

### Assessment documents

Files coaches store with an assessment, for example a corrected exam sheet or an assessment rubric.

*German: Bewertungsdokumente* · [Manual](../manual_user/learningresources/The_assessment_form.md)

### Assessment inspection

The supervised look at one's own corrected exam. The person who took the exam sees their answers and the assessment in a set window of time, without being able to change anything.

*German: Prüfungseinsicht* · [Manual](../manual_user/learningresources/Assessment_inspection.md)

### Assessment management

The management of assessment mode and assessment inspection. In the course it is the tool of the course administration with the two tabs assessment mode and assessment inspection. In the administration under e-Assessment it lists the assessment modes of all courses and holds the settings.

*German: Prüfungsverwaltung* · [Manual](../manual_user/learningresources/Assessment_Management.md)

### Assessment mode

A window of time in which a course becomes an exam. During the assessment mode all other areas of OpenOlat are locked, access can be limited to particular machines and the Safe Exam Browser can be required.

*German: Prüfungsmodus* · [Manual](../manual_user/learningresources/Assessment_mode.md)

### Assessment orders

The area of the coaching site that collects one's own open assessment work across all courses: open assessments, open levels/gradings, assessments to release and one's own grading assignments.

*German: Bewertungsaufträge* · [Manual](../manual_user/area_modules/Coaching_Assessment_Orders.md)

### Assessment tool

The area of a course where coaches and owners see, assess, release and reset all results of the participants.

*German: Bewertungswerkzeug* · [Manual](../manual_user/learningresources/Assessment_tool_overview.md)

### Bulk assessment

Assessing many participants in one pass, through an uploaded table or an input form. It saves opening every single person.

*German: Massenbewertung* · [Manual](../manual_how-to/bulk_assessment/bulk_assessment.md)

### Change log

The record of every change to an assessment, with the person and the point in time. It is the basis when an assessment is contested later.

*German: Änderungsverlauf*

### Correction

A person reviewing and grading a submitted piece of work. It is needed wherever OpenOlat cannot assess automatically, for instance with free text questions.

*German: Korrektur* · [Manual](../manual_user/learningresources/Test_settings.md)

### Courses (Assessment)

The area of the coaching site that lists all courses in which the person is coach or owner, with the number of participants, progress and success status per course.

*German: Kurse* · [Manual](../manual_user/area_modules/Coaching_Courses.md)

### Disadvantage compensation

An adjustment of the exam conditions for a person with a disability or an impairment, as a rule as extra time. It applies to that person and leaves the task unchanged.

*German: Nachteilsausgleich* · [Manual](../manual_admin/usermanagement/Configure_User.md)

### Events / Absences

The area of the coaching site for events and absences of the coached persons, with the tabs cockpit, events, absences, notices, appeals and user search. It appears only when the events and absences module is switched on.

*German: Termine / Absenzen* · [Manual](../manual_user/area_modules/Coaching_Events_Absences.md)

### Exam course

A course created only to run an exam. The wizard creates it with the assessment mode and the test in one step.

*German: Prüfungskurs* · [Manual](../manual_how-to/test_creation_procedure/test_creation_procedure.md)

### Generated report

The Excel file a report template has produced. It stays available for download for ten days, shows the remaining time and can be copied or deleted.

*German: Generierter Report* · [Manual](../manual_user/area_modules/Coaching_Reports.md)

### Grade

The value a performance is named with under a grading system, for example the grade 5 or the verdict good. It comes from the points through the grading scale.

*German: Note* · [Manual](../manual_user/learningresources/Assessment_translate_points_in_grades.md)

### Grading assignment

The order given to a correcting person to grade a particular test submission by hand, with a deadline and recorded correction time. It serves where the correction is given out and billed outside the course team.

*German: Korrekturauftrag* · [Manual](../manual_user/area_modules/Coaching_Order_Management.md)

### Grading scale

The assignment of ranges of points to grade values. It translates a score into a grade.

*German: Bewertungsskala* · [Manual](../manual_user/learningresources/Assessment_translate_points_in_grades.md)

### Grading system

A named system of grade values, for example the Swiss scale from 1 to 6. It sets which values exist and which of them count as passed.

*German: Bewertungssystem* · [Manual](../manual_admin/administration/Assessment_translate_points_in_grades_admin.md)

### Groups (Assessment)

The area of the coaching site that lists all coached groups from courses, with the participants of the group and their state.

*German: Gruppen* · [Manual](../manual_user/area_modules/Coaching_Groups.md)

### Levels/Grading

The module where the grading systems and their scales are maintained. It sets which grades exist and from which score a grade is reached.

*German: Einstufung/Noten* · [Manual](../manual_user/learningresources/Assessment_translate_points_in_grades.md)

### Order management

The area of the coaching site for the correction workflow of tests. Owners of a test see their correctors, their grading assignments and the submissions not yet assigned, and they assign orders.

*German: Auftragsverwaltung* · [Manual](../manual_user/area_modules/Coaching_Order_Management.md)

### People

The area of the coaching site that lists all participants a person coaches across all courses, grouped by the role one holds towards them. From there one click leads to the person's assessment tool.

*German: Personen* · [Manual](../manual_user/area_modules/Coaching_People.md)

### Performance summary

The block with status, score, grade and comment of an assessment. Participants see it in the course element, coaches in the assessment form and there additionally as a preview of the participants' view.

*German: Leistungsübersicht* · [Manual](../manual_user/learningresources/Course_Element_Structure.md)

### Reports (Assessment)

The area of the coaching site where authorised roles produce Excel files about the coached persons from report templates, for example about issued certificates, absences or open booking orders. It evaluates the operation, not single learners.

*German: Reports* · [Manual](../manual_user/area_modules/Coaching_Reports.md)

### Report templates

A predefined query a report is produced from, with name, category, description and type. OpenOlat ships seven templates in the categories absences, booking orders and certificates; only those the role is authorised for are shown.

*German: Reportvorlagen* · [Manual](../manual_user/area_modules/Coaching_Reports.md)

### Rubric assessment

The criteria-based assessment of an element with the help of a rubric. It is switched on at the assessment element and uses a rubric form for it.

*German: Rubrik-Bewertung* · [Manual](../manual_user/learningresources/Course_Element_Assessment.md)

### Rubric form

A form with a rubric that coaches fill in while assessing. It makes the criteria visible and the assessment comparable between several coaches.

*German: Rubrik-Formular* · [Manual](../manual_user/learningresources/Forms_in_Rubric_Scoring.md)

### Safe Exam Browser

The connection to the Safe Exam Browser. The assessment mode requires this browser and thereby locks every other program on the device during the exam.

*German: Safe Exam Browser* · [Manual](../manual_how-to/SEB/SEB.md)

### User search

The search form of the coaching site that finds a coached person by name, username or further attributes. Without input it returns the whole list of coached persons.

*German: Personensuche* · [Manual](../manual_user/area_modules/Coaching_User_Search.md)

## Evidence

What comes out at the end and can be proven: the evidence of achievement from the course, the certificate as a document, the certification program as a running membership and the badge as an open credential.

### Award criteria

The conditions under which a badge is awarded, for example a passed course or a score that has been reached.

*German: Vergabekriterien* · [Manual](../manual_user/learningresources/OpenBadges.md)

### Awarded badge

The single badge a person has received from a badge class, with recipient, date of award and image. The metadata sits inside the image itself; that way the badge can be downloaded, shared on LinkedIn and verified.

*German: Vergebener Badge* · [Manual](../manual_user/personal_menu/OpenBadges.md)

### Badge

A digital credential following the Open Badges standard, with an image, criteria and an issuing body. Unlike the certificate it can be shown outside OpenOlat and checked by a machine.

*German: Badge* · [Manual](../manual_user/personal_menu/OpenBadges.md)

### Badge class

The kind of a badge, with an image, a description, an issuer and award criteria. The single credential is one issue of this class to a person. A badge class can exist in several versions; recipients keep the version that was awarded.

*German: Badge-Klasse* · [Manual](../manual_user/learningresources/OpenBadges.md)

### Certificate

A PDF that certifies the successful participation in a course or the completion of a certification program, with name, date and serial number. The evidence of achievement shows what someone has done; the certificate attests it to the outside world. Externally earned certificates can be uploaded if the administration allows it.

*German: Zertifikat* · [Manual](../manual_user/personal_menu/Certificates.md)

### Certificate template

The template OpenOlat generates a certificate PDF from. It is a PDF form or an HTML template as a ZIP with index.html; the HTML template needs the PDF service. The administration provides system-wide templates, course owners upload their own.

*German: Zertifikatsvorlage* · [Manual](../manual_user/learningresources/Course_Settings_Assessment_Certificate.md)

### Certification program

A program that ties several courses together into one certification and watches over its validity. It calls for a recertification once the validity has run out.

*German: Zertifikatsprogramm* · [Manual](../manual_user/area_modules/Course_Planner_Certification_Programs.md)

### Evidence of achievement

The collection of all results a person has in a course, one per assessable course element, with points, status and date.

*German: Leistungsnachweis* · [Manual](../manual_user/personal_menu/Evidence_of_Achievements.md)

### Membership (Evidence)

A person's affiliation with a certification program. Candidates take part in a linked implementation and hold no certificate yet; active members hold one; alumni have left the program.

*German: Mitgliedschaft* · [Manual](../manual_user/area_modules/Course_Planner_Certification_Programs.md)

### OpenBadges

The Open Badges standard. It describes a digital credential in a way that makes it verifiable and lets it be shown outside the issuing platform.

*German: OpenBadges* · [Manual](../manual_user/personal_menu/OpenBadges.md)

### Recertification

The renewed issue of a certificate before or after it expires. In a single course participants complete the course again for it. In a certification program it runs automatically or by hand, optionally against credit points.

*German: Rezertifizierung* · [Manual](../manual_user/learningresources/Course_Settings_Assessment_Certificate.md)

### Template (Evidence)

An image in SVG or PNG the wizard creates a badge class from. The template can hold colours and text to adapt and belongs to a category. The administration maintains the templates under e-Assessment; a default set is shipped.

*German: Vorlage* · [Manual](../manual_admin/administration/e-Assessment_openBadges.md)

### Verification

The check whether a badge is genuine and comes from this instance. Every badge class fixes the method at creation: Hosted fetches the data from the OpenOlat address, Signed checks a digital signature. The administration uploads a badge file for this.

*German: Verifizierung* · [Manual](../manual_admin/administration/e-Assessment_openBadges.md)

## Quality management and forms

How feedback is collected, analysed and turned into measures, and the form building blocks all of that rests on.

### Action to-dos

The measures that follow from the results of a data collection, kept as to-dos with a responsible person and a deadline. They close the circle from measurement to improvement.

*German: Massnahmen To-dos* · [Manual](../manual_user/area_modules/Quality_Management_To-dos.md)

### Analysis

The area where the answers of several data collections are analysed together, with filters, groupings, a heatmap and a trend.

*German: Analyse* · [Manual](../manual_user/area_modules/Quality_Management_Analysis.md)

### Black list

The list of courses or implementations a generator is to skip. It exempts single cases from an otherwise general rule.

*German: Negativliste* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collection_Generators.md)

### Coach details

A block in the form that shows details of the assessed coach of a data collection. It is meant for quality management forms.

*German: Angaben zum:r Betreuer:in*

### Data collection

A single collection run with one form, one topic, a period and a set of respondents. It is the unit of work of quality management.

*German: Datenerhebung* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collections.md)

### Data collection generator

A rule that creates data collections on its own as soon as an event occurs, for example the end of a course. It saves creating the same kind of collection over and over.

*German: Datenerhebungsgenerator* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collection_Generators.md)

### Data collection participation

The participation of a single person in a data collection. It records whether someone answered, not what they answered.

*German: Teilnahme Datenerhebung*

### Data collection previews

The overview of the upcoming data collections that generators are going to create. It is available in quality management, in the course administration and in the Course Planner and must be switched on in the administration.

*German: Datenerhebungsvorschau* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collection_Preview.md)

### Date / Time

An input field in the form for a date, optionally with a time of day.

*German: Datum / Zeit* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Form (Quality management and forms)

The generic learning resource for recorded entries, built in the content editor. It is used in six places with a different meaning each time: as an assessment rubric in the ePortfolio, in the assessment course element and in the task course element including the peer review; as a quality rubric in quality management and in the survey course element; as a form in the form course element. The meaning comes from the place that embeds it, not from the form.

*German: Formular* · [Manual](../manual_user/learningresources/Form.md)

### Heat map

The view of the analysis that shows the average values per grouping and question as coloured dots. The colour follows the quality ranges of the rubric, the size follows the number of answers. It makes problem areas visible at a glance.

*German: Heatmap* · [Manual](../manual_user/area_modules/Quality_Management_Analysis.md)

### Key figures

The statistical values the analysis summarises the answers with.

*German: Kennzahlen* · [Manual](../manual_user/area_modules/Quality_Management_Analysis.md)

### Multiple choice (Quality management and forms)

A question in the form with several answers of which more than one can be chosen.

*German: Mehrfachauswahl* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Previous survey

An earlier collection on the same topic, used as a comparison value. Without it no development over time can be shown.

*German: Erstbefragung*

### Public link

Access to a data collection without signing in. It allows people without an account to be surveyed as well, for example placement companies.

*German: Öffentlicher Zugang* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collections.md)

### Quality management

The module for assessing an institution's own offerings and processes. It plans data collections, runs them, analyses the answers and follows up the measures derived from them. It sits at the end of the education cycle and assesses the offering, not the learners.

*German: Qualitätsmanagement* · [Manual](../manual_admin/administration/Modules_Quality_Management.md)

### Reminder (Quality management and forms)

An e-mail of a data collection to the respondents: the invitation with the link to the form and up to two reminders to people who have not answered yet. The delivery date is set per data collection.

*German: Erinnerung* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collections.md)

### Report

The evaluation of a single data collection: the answers and key figures of the form. The tab appears as soon as a report exists. Who may see it is set by role in the tab Berechtigungen Report, optionally with an e-mail on completion.

*German: Report* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collections.md)

### Respondent details

A block in the form that asks for or prefills details of the respondent, such as name or e-mail, optional, mandatory or entered automatically. It appears only once per form and removes anonymity.

*German: Angaben zur befragten Person* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Rubric (Quality management and forms)

A block in the form that lets several statements be judged on the same scale. It supplies the numbers the analysis works with.

*German: Rubrik* · [Manual](../manual_user/learningresources/Form_Element_Rubric.md)

### Single choice (Quality management and forms)

A question in the form with several answers of which exactly one can be chosen.

*German: Einzelauswahl* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Suggestion for improvement

A suggestion for improvement that a person submits about a course or an offering. Unlike a data collection it starts from the person submitting it and not from a survey.

*German: Verbesserungsvorschlag* · [Manual](../manual_user/area_modules/Quality_Management_Improvement.md)

### Terms of use (Quality management and forms)

A text in the form the respondent must agree to before they can submit the form.

*German: Nutzungsbedingungen* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Text block

An input field in the form for a freely worded answer, single-line or multi-line, optionally restricted to a number or a date.

*German: Textblock* · [Manual](../manual_user/learningresources/Form_Elements.md)

### Trend details

The development of a value across several collections. It shows whether a measure has worked.

*German: Trend Detail* · [Manual](../manual_user/area_modules/Quality_Management_Analysis.md)

### Upload file (Quality management and forms)

A field in the form through which the respondent hands in a file. The author sets the permitted file types and the maximum size.

*German: Datei hochladen* · [Manual](../manual_user/learningresources/Form_Elements.md)

### White list

The list of courses or implementations a generator restricts its rule to: data collections are created only for cases the rule covers and that are on the list. It is the counterpart of the black list.

*German: Positivliste* · [Manual](../manual_user/area_modules/Quality_Management_Data_Collection_Generators.md)

## Selectus

The module for appointment procedures: the call for a professorship, the application, the committee, external expert assessments, letters of reference and the A/B/C decision.

### Abstention

A committee member's explicit refusal to judge an application.

*German: Enthaltung*

### Application

An applicant's submission for a call, made up of personal data, academic background and the uploaded documents.

*German: Bewerbung*

### Application form

The multi-step form with which a person applies for a call: personal data, academic background, project, up to four custom steps of the call, documents and attachments, data protection. The staff configures the steps and fields per call.

*German: Bewerbungsformular*

### Apply

The site for applicants. It shows the published calls and leads through the application form. Applicants reach it without an OpenOlat account through the link of a call or through the login page.

*German: Bewerben*

### Assistant professor

The professorship type for a fixed-term professorship at the start of the academic career, often with an option to become permanent.

*German: Assistenzprofessur*

### Certificate of Study

A certificate confirming a completed course of study.

*German: Studienbescheinigung*

### Clinical expertise

Evidence of an applicant's clinical experience. It is required for medical professorships.

*German: Klinische Expertise*

### Combined document

All documents of an application merged into a single PDF, for reading and printing.

*German: Kombiniertes Dokument*

### Committee

The body of a call that judges the applications and decides on them. It is made up of the head, the secretary, the committee members and the ex-officio members; every call has its own committee.

*German: Kommission*

### Committee assignment

The allocation of applications to individual committee members. It sets who has to judge which application.

*German: Kommissionszuweisung*

### Committee decision

The formal resolution of the committee on an application. It closes the rating and is the basis for the correspondence.

*German: Kommissionsentscheid*

### Committee rating

The combined rating of an application by the whole committee, as opposed to the rating of a single member.

*German: Kommissionsbeurteilung*

### Comparative assessment

An expert assessment in which several applications of the same call are compared with each other.

*German: Vergleichsgutachten*

### Covering letter

The covering letter of an application, in which the applicant sets out why they are interested in the professorship.

*German: Anschreiben*

### Curriculum vitae

An applicant's curriculum vitae with education, posts and academic career.

*German: Lebenslauf*

### Dashboard (Selectus)

The start page of applicants after signing in. It lists their own applications with status and deadline and leads to the referee management.

*German: Dashboard*

### Decision (Selectus)

The committee's result on an application, with A, B or C. A marks the strongest candidacies, C is the basis for a rejection.

*German: Entscheid*

### Decision tool

A grid of weighted rubrics with which the head and the staff record one more rating after the screening, for example on the talk. The sum of the rubrics supports the decision. Committee members have no access.

*German: Entscheidungswerkzeug*

### Degree certificates

The certificates of the academic degrees reached.

*German: Abschlusszertifikate*

### Documents and attachments

The step of the application form with all documents an application brings with it. Which documents are available and which are compulsory is set by the call.

*German: Dokumente und Anhänge*

### Email log

The table in the mail center with all e-mails of a call already sent, with recipients, template and time.

*German: E-Mail-Protokoll*

### Evaluation (Selectus)

The site where referees and experts submit their letters and where public feedback is given. It opens through a personal link without an OpenOlat account.

*German: Auswertung*

### Expert assessment

A written judgement of an application by an external specialist appointed by the committee.

*German: Gutachten*

### External funding

Evidence of the research funding raised from external funders, with the amount and the funder.

*German: Drittmittel*

### Faculty feedback

Feedback on an application collected from faculty members who do not belong to the appointment committee.

*German: Fakultätsfeedback*

### Form letter

A PDF letter produced from a template and sent together with an e-mail, for example a letter of rejection.

*German: Serienbrief*

### Full professor

The professorship type for a permanent professorship with the full scope of research, teaching and self-administration. It is the highest of the professorship types.

*German: Ordentliche Professur*

### Leadership philosophy

The document in which an applicant sets out how they intend to lead a research group or an institute.

*German: Führungsphilosophie*

### Letter of recommendation

A letter of recommendation written by a referee named by the applicant.

*German: Referenzschreiben*

### List of referees

The list of referees an applicant has named, with the state of each request.

*German: Referenzenliste*

### Mail center

The area for bulk correspondence with applicants, with one template per decision group.

*German: Mailcenter*

### Mail template

A template for the correspondence of a call, for example the request to a referee or the letter of rejection. It holds placeholders that are filled in when it is sent.

*German: E-Mail-Vorlage*

### Organisation unit

The faculty or the institute a call belongs to, which provides a sender address and an e-mail signature of its own.

*German: Organisationseinheit*

### Other applications

The list of the other calls the same person has applied for. Whether multiple applications are allowed is set in the configuration.

*German: Weitere Bewerbungen*

### Position

An advertised professorship in Selectus. It holds the text of the call, the application form, the deadlines and the appointment committee.

*German: Ausschreibung*

### Profile paper

The document that describes the profile of the advertised professorship and is available to the appointment committee.

*German: Profildokument*

### Public feedback

Feedback given through a public link without signing in, for example after a trial lecture.

*German: Öffentliche Rückmeldung*

### Public feedback link

The link the staff generates and distributes per application. Whoever opens it gives public feedback without signing in, up to the submission deadline.

*German: Link für öffentliche Rückmeldungen*

### Rating (Selectus)

The estimate of an application with A, B or C by a single committee member.

*German: Beurteilung*

### Rating policy

The rules of a call for who may see which ratings and reviews and from when. They stop committee members from influencing each other.

*German: Beurteilungsrichtlinien*

### Referee management

The area where applicants record their referees themselves and follow whether the requests have been answered.

*German: Referenzverwaltung*

### Reporting

The area in Selectus for the statistical evaluation of closed calls. A call in the status Reporting is only accessible here; the staff completes the data for the statistics and produces the Excel report of the procedure.

*German: Reporting*

### Reprints up to 5 publications

Up to five publications in full text that the applicant picks themselves as their most important.

*German: Sonderdrucke von bis zu 5 Publikationen*

### Research statement

The document in which an applicant sets out their research plans for the advertised professorship.

*German: Forschungsziel*

### Review

A structured judgement of an application by a committee member, using a questionnaire of sliders and free text.

*German: Review*

### Review discussion

Comments and replies that committee members can record on a review.

*German: Review-Diskussion*

### Review questionnaire

The configurable set of sliders and text fields committee members fill in per application.

*German: Review-Fragebogen*

### Review tool

The area where committee members record their reviews of the applications assigned to them and read the reviews of the others, as far as the visibility allows.

*German: Review-Werkzeug*

### Rubric (Selectus)

A weighted criterion in the decision tool with a name, a type and a weight. The sum of all rubrics gives the value of an application.

*German: Rubrik*

### Screening

The phase in which the appointment committee reads and judges the applications received.

*German: Screening*

### Selectus

The module for appointment procedures: calls for professorships, recording the online applications and accompanying the appointment committee up to the decision.

*German: Selectus*

### Surgical expertise

Evidence of an applicant's surgical experience, with the kind and the number of operations. It is required for surgical professorships.

*German: Chirurgische Expertise*

### Teaching assessment

Evidence of the quality of the teaching done so far, for example results of teaching evaluations.

*German: Lehrbeurteilung*

### Teaching statement

The document in which an applicant sets out their understanding of teaching and the teaching they plan to do.

*German: Lehransatz*

## Platform

Who uses the platform, in which role, in which organisation, and where the areas are that people work in.

### Accessibility

The accessibility of the interface for people with a disability. OpenOlat follows WCAG 2.1 level AA and can be operated with a keyboard and a screen reader.

*German: Barrierefreiheit* · [Manual](../manual_user/basic_concepts/Accessibility_Principals.md)

### Account

A person's access to OpenOlat, with a username, profile entries, roles and organisation membership. In German this object is called Konto and not Benutzer:in, because the gendered form becomes unreadable in running text.

*German: Konto* · [Manual](../manual_admin/usermanagement/Configure_User.md)

### Active Directory Federation Services

The connection to Active Directory Federation Services for signing in with the organisation's Windows account.

*German: Active Directory Federation Services*

### Administration

The area for configuring the system. It can only be reached through the system role System administrator.

*German: Administration* · [Manual](../manual_user/area_modules/index.md)

### API-Key

A pair of client ID and client secret a third-party system signs in to the REST API with. User management creates it under Authentication; the secret can be read only once. The administration can restrict API access to accounts with an API key.

*German: API-Key* · [Manual](../manual_admin/administration/REST_API.md)

### Authentication

The proof that a person is who they claim to be. OpenOlat supports several methods side by side, and one account can carry several of them.

*German: Authentifizierung* · [Manual](../manual_user/login_registration/Login_Concept.md)

### Authoring

The area where learning resources are created, edited, copied and managed. It is only accessible with the Author role or with an administrative role.

*German: Autorenbereich* · [Manual](../manual_user/area_modules/Authoring.md)

### Cloud login

The collective term for the sign-in methods in which a third-party provider handles the sign-in and OpenOlat only receives the confirmation. In the interface the area is called Cloud Login.

*German: Cloud Login* · [Manual](../manual_admin/administration/Login.md)

### Coaching

The area where coaches follow their learners across all courses, with progress, assessments, attendance and certificates in one place.

*German: Coaching* · [Manual](../manual_user/area_modules/Coaching.md)

### Configuration

The section of the personal menu below the User tools, with the profile, the settings and the password. The manual calls it Personal configuration.

*German: Konfiguration* · [Manual](../manual_user/personal_menu/Personal_Configuration.md)

### Confirmation code

The code OpenOlat sends to the given e-mail address at registration and at Forgot password? to confirm it. It is valid for 30 minutes; registration keys created through the REST interface are valid for 30 days.

*German: Validierungscode*

### Contact tracing

The module people use to register their presence at locations with a QR code, with an account or as a guest. The registrations are deleted after the retention period of 40 days and exported only on official request.

*German: Kontaktverfolgung* · [Manual](../manual_admin/administration/Modules_Contact_Tracing.md)

### Context help

The question mark icon on pages and in forms that opens the matching page of the OpenOlat Manual. It only works when the manual is active as a help entry.

*German: Kontexthilfe* · [Manual](../manual_user/help/index.md)

### Contexts

A usage context of a user property, for example the profile, the registration or the visiting card. Per context and property there are four switches: include, Mandatory, Admin only and User readonly.

*German: Contexts* · [Manual](../manual_admin/administration/E-Mail_Settings.md)

### Core functions

The Administration section with the basic functions of the platform: e-mail, files and folders, landing pages, REST API, WebDAV, calendar, notifications and more.

*German: Core Konfiguration* · [Manual](../manual_admin/administration/Core_functions.md)

### Course Planner (Platform)

The area for planning the educational offering: products, their elements, the implementations and the courses hanging off them. It used to be called Curriculum.

*German: Course Planner* · [Manual](../manual_user/area_modules/Course_Planner.md)

### Courses (Platform)

The overview of the courses a person is a member of, with the progress and the last access.

*German: Kurse* · [Manual](../manual_user/area_modules/Courses.md)

### COVID certificate

The module a person uses to record the validity of their COVID certificate in the personal menu, by QR scan, import or manually. Only the expiry date is stored. COVID commissioners record certificates for others in the site COVID Certificate Administration.

*German: COVID-Zertifikat* · [Manual](../manual_user/personal_menu/COVID_certificate.md)

### Customizing

The Administration section for the appearance and adaptation of the platform: Sites, Help, User Properties, Imprint, Terms of use and languages.

*German: Customizing* · [Manual](../manual_admin/administration/Customizing.md)

### Dashboard (Platform)

An overview page made of widgets a person arranges themselves: add, remove and move widgets and reset them to the system default. The Course Planner and Coaching open with a dashboard.

*German: Dashboard* · [Manual](../manual_user/area_modules/Course_Planner_Dashboard.md)

### Datenlotsen

The connection to the identity server of Datenlotsen, the maker of the campus management system CampusNet, for signing in through OpenID Connect.

*German: Datenlotsen*

### Document pool (Platform)

The area for a document collection structured by the taxonomy. The permissions are granted per taxonomy level.

*German: Dokumentenpool* · [Manual](../manual_admin/administration/Modules_Document_pool.md)

### E-mail inbox and outbox

The Administration page under Core functions, E-mail. It switches the OpenOlat inbox on and decides whether e-mails go only to the inbox or also to the personal e-mail address; plus the e-mail template.

*German: E-Mail Postfach und Versand* · [Manual](../manual_admin/administration/E-Mail_Settings.md)

### E-mail support

The help entry that opens a contact form to the support address of the installation. The administration enters the address; switched off by default.

*German: E-Mail Support* · [Manual](../manual_user/help/index.md)

### Export

A job that produces a ZIP file in the background and offers it for download for a limited time, 10 days by default. The assessment tool, the course archive, Coaching and the Course Planner use the same mechanism.

*German: Export* · [Manual](../manual_user/learningresources/Course_Archiving.md)

### Export history

The list of the exports of a course or a person, with status, progress, Available until and the download. It appears in the assessment tool under Export data, in the Authoring area, in Coaching and in the Course Planner.

*German: Exportverlauf*

### External site

A tab of the main navigation that opens an external web address, embedded as an iframe or as a link. Title and URL are set per language. There are two such sites; they only appear once configured.

*German: Externe Seite* · [Manual](../manual_admin/administration/Modules_External_Page.md)

### Facebook

The connection to Facebook for signing in with the Facebook account through OAuth 2.0.

*German: Facebook* · [Manual](../manual_admin/administration/Login.md)

### File Hub

The area that shows the files from all courses, groups and a person's own storage in one place.

*German: File Hub* · [Manual](../manual_user/personal_menu/File_Hub.md)

### Files and folders

The Administration page for the file storage of the whole system, with the tabs Overview, Configuration, Quotas, Large files and Trash. Versioning, the retention period of the trash and the default quotas are set there.

*German: Dateien und Ordner* · [Manual](../manual_admin/administration/Files_and_Folders.md)

### Full-text search

The search across the content of the whole platform, including the text of documents. It only shows what the searching person has access to.

*German: Volltextsuche* · [Manual](../manual_user/basic_concepts/Full_Text_Search.md)

### Google

The connection to Google for signing in with the Google account through OAuth 2.0. The person signs in at Google, OpenOlat receives the confirmed identity.

*German: Google* · [Manual](../manual_admin/administration/Login.md)

### Groups (Platform)

The area for groups that belong to no course. People create their own groups there or join open ones.

*German: Gruppen* · [Manual](../manual_admin/administration/Modules_Groups.md)

### Guest access

Access to OpenOlat without an account through the Guest access link on the login page. Guests only see resources explicitly released for guests, and only in conventional courses.

*German: Gastzugang* · [Manual](../manual_user/basic_concepts/guest_access.md)

### Help

The help menu in the header with links to the OpenOlat Manual, the OpenOlat Academy and the teaching session, optionally with e-mail support, a help course and three custom URLs. The administration chooses the entries under Customizing, Help.

*German: Hilfe* · [Manual](../manual_user/help/index.md)

### Home

The personal entry area of a person, with their courses, events, notifications, notes and settings.

*German: Home*

### Imprint

The legally required statement of who operates the platform. The text is set per installation.

*German: Impressum* · [Manual](../manual_admin/administration/Customizing.md)

### Info message

A message that appears on the login page, that is before signing in. It announces maintenance work, for example, or explains an outage.

*German: Info Meldung* · [Manual](../manual_admin/administration/System.md)

### Info messages

The Administration page under System where the info message for the login page and the maintenance message for all pages are set, each with an optional start and end date.

*German: Info messages* · [Manual](../manual_admin/administration/System.md)

### Info page (Platform)

A course pinned as a tab of the main navigation. The title of the tab is set per language, the course toolbar can be shown to everyone. There are four such sites, Info page n°1 to n°4.

*German: Infoseite* · [Manual](../manual_user/learningresources/General_Functions_Infopage.md)

### Invitation link

The link through which an external person without an account gets access to exactly one resource: a course, a group, a project or a portfolio binder. On first use an external account with the role Invitee is created, which expires after 180 days.

*German: Einladungslink* · [Manual](../manual_user/basic_concepts/Assign_Roles.md)

### Invitations (Platform)

The site an invited external person sees as their only navigation entry. It lists the resources their invitations lead to. Regular accounts and guests never see it.

*German: Einladungen*

### Keycloak

The connection to Keycloak, a free identity provider, through OpenID Connect.

*German: Keycloak*

### Landing page

The page a person sees after signing in. The administration sets rules by role or by value of a user property; the first matching rule applies. A person overrides them in the settings with their own landing page.

*German: Startseite* · [Manual](../manual_admin/administration/Landing_pages.md)

### LDAP

The connection to an LDAP directory. Accounts are taken from it and the sign-in is checked against the directory.

*German: LDAP*

### Library (Platform)

The area for a shared document collection of the whole system, with a release step before publication.

*German: Bibliothek* · [Manual](../manual_user/area_modules/Library.md)

### LinkedIn

The connection to LinkedIn for signing in with the LinkedIn account through OAuth 2.0.

*German: LinkedIn* · [Manual](../manual_admin/administration/Login.md)

### Local OpenOlat authentication

Signing in with a username and a password that OpenOlat manages itself. It is the basic method and works without a third-party system.

*German: Lokale OpenOlat-Authentifizierung* · [Manual](../manual_user/login_registration/Login_Concept.md)

### Login

The Administration section for sign-in and access: password and authentication, self-registration, guests and external people, security, cloud login, LDAP, Shibboleth and passkey.

*German: Login* · [Manual](../manual_admin/administration/Login.md)

### Maintenance message

A message that appears to signed-in people as a bar on every page, for example before a restart. It can be deleted automatically at the next restart.

*German: Wartungsmeldung* · [Manual](../manual_admin/administration/System.md)

### Media Center (Platform)

The personal place to store images, videos, quotations and other media that are reused in pages and portfolios.

*German: Media Center* · [Manual](../manual_admin/administration/Modules_Media_Center.md)

### Metadata (Platform)

The describing entries on a file in a folder: title, description, author, publisher, source, language, pages, URL, date of publication and license, plus the switch Locked. The additional metadata show who created the file and who last modified it.

*German: Metadaten* · [Manual](../manual_user/basic_concepts/Folder_Concept.md)

### Microsoft Azure Active Directory

The connection to Microsoft Entra ID, formerly Azure Active Directory, for signing in with the organisation's account.

*German: Microsoft Azure Active Directory*

### One time code

An eight-digit confirmation code OpenOlat sends by e-mail after the username and password have been entered. It is the second factor for accounts without a passkey and is switched off by default.

*German: One Time Code* · [Manual](../manual_user/login_registration/One_Time_Code.md)

### OpenID Connect

The OpenID Connect standard. It extends OAuth 2.0 with the proof of identity and is the method Keycloak, Microsoft Entra ID and similar providers are connected through.

*German: OpenID Connect* · [Manual](../manual_admin/administration/Login.md)

### OpenOlat Manual

The help entry that opens the manual at docs.openolat.org. The URL is configurable, for example for a manual of your own.

*German: OpenOlat Handbuch* · [Manual](../manual_user/help/index.md)

### Organisation

A unit in the structure of the platform, for example a school, an institute or a department. Organisations are hierarchical, carry the roles of their members and limit what administrative roles can reach.

*German: Organisation* · [Manual](../manual_admin/administration/Modules_Organisations.md)

### Passkey

Signing in without a password, following the WebAuthn standard. The person identifies themselves with a fingerprint, their face or a security key of the device.

*German: Passkey* · [Manual](../manual_user/login_registration/Passkey.md)

### Password syntax

The rules an OpenOlat password must meet. Default: 12 to 128 characters, at least one letter, at least one digit or special character, neither the username nor the first or last name contained, and the last 10 passwords are blocked.

*German: Passwort-Syntax* · [Manual](../manual_admin/administration/Login_Password_and_Authentication.md)

### Portal

A tab with freely arranged sections such as My courses, calendar, notes and subscriptions, which every person shows and hides themselves. Superseded since 10.0 and switched off by default.

*German: Portal* · [Manual](../manual_user/basic_concepts/Portal_configuration.md)

### Privacy

The Administration page with the system-wide privacy rules: which roles see the administrative user properties, whether the last visit is visible and which data the course element External page transmits. A person has no privacy settings of their own.

*German: Datenschutz*

### Privacy policy

The statement of which data the platform processes and for what purpose. It can be set system-wide and additionally per course.

*German: Datenschutzerklärung* · [Manual](../manual_how-to/legal_consents/legal_consents.md)

### Profile

The page in the personal menu where a person maintains their own entries: name, e-mail, address, institution, portrait and the About me text. Its tab My visiting card sets which entries others see.

*German: Profil* · [Manual](../manual_user/personal_menu/Profile.md)

### Projects

The area for project work, with events, to-dos, decisions, notes, files and a whiteboard per project.

*German: Projekte* · [Manual](../manual_admin/administration/Modules_Projects.md)

### Question bank (Platform)

The area where questions for tests are collected, tagged, released and reviewed. Questions from the question bank can be used in several tests.

*German: Fragenpool* · [Manual](../manual_user/area_modules/Question_Bank.md)

### Quota

The storage space a folder may occupy at most, in KB. Every folder type has a default quota, for example course folder, groups or personal folder; the default is 200 MB. The administration overrides it per folder.

*German: Quota* · [Manual](../manual_admin/administration/Files_and_Folders.md)

### Registration

The wizard a person uses to create their own account. The steps: language, terms of use, New here?, e-mail validation with a validation code, personal data with username and password, additional personal data.

*German: Registrierung* · [Manual](../manual_user/login_registration/index.md)

### Reports (Platform)

The Administration section with system-wide evaluations: Certificates, Questions in tests and Course memberships. It searches the whole system and delivers the results as a table or an Excel file.

*German: Reports* · [Manual](../manual_admin/administration/Reports.md)

### Security

The Administration page under Login with the security settings: HTTP headers against embedding in frames, HTTPS downgrade and content type sniffing, SameSite cookie, CSRF protection, Content Security Policy with log and the enabled media servers.

*German: Sicherheit* · [Manual](../manual_admin/administration/Login_Security.md)

### Self-registration

The module a person uses to create an account themselves on the login page, without user management creating it. The administration sets the home organisation, the permitted e-mail domains, the mandatory fields and whether the account is active at once or pending.

*German: Selbstregistrierung* · [Manual](../manual_admin/administration/Login_Self-Registration.md)

### Shibboleth

The connection to a Shibboleth federation. Signing in happens at the home institution, and OpenOlat only receives the released attributes.

*German: Shibboleth*

### Sites

The Administration page that manages the tabs of the main navigation: order, enabled, access per site and an alternative when access is denied. Plus the configuration of the info pages 1 to 4 and the external sites 1 and 2.

*German: Sites* · [Manual](../manual_admin/administration/Customizing.md)

### Storage usage

The evaluation in the course administration that shows per folder and course element how much storage a course occupies, with the filters Internal with quota, Internal without quota and External.

*German: Speicherverbrauch*

### Switch edu-ID

The connection to Switch edu-ID, the Swiss higher education identity. It stays with a person across changes of institution.

*German: Switch edu-ID*

### System

The Administration section for operations: system information, info messages, user sessions, errors, caches, locks, database ORM, Java VM infos and scheduler.

*German: System* · [Manual](../manual_admin/administration/System.md)

### System settings (area)

The page in the personal menu with the preferences of an account, in the tabs System, WebDAV, Instant Messaging, Terms of use, User data and GUI preferences.

*German: Einstellungen* · [Manual](../manual_user/personal_menu/Settings.md)

### System settings (concept)

The preferences of an account in the System tab of the settings: language, e-mail notification, character set for downloads, document editor, session resume and the personal landing page. In user management the tab of the same name shows and changes them.

*German: Systemeinstellungen* · [Manual](../manual_user/personal_menu/Settings.md)

### Tags

A freely assigned keyword on an object that lists can be filtered by. Media in the Media Center, projects, to-dos, blog and podcast entries and badges carry tags; the service behind them is the same for all.

*German: Tags*

### Terms of use (Platform)

The conditions a person has to accept before using the platform or a course. They can be set system-wide and per course.

*German: Nutzungsbedingungen* · [Manual](../manual_user/basic_concepts/Terms_Of_Use.md)

### To-do (Platform)

An open item with a due date, a responsible person and a status. To-dos come into being personally, in a course, in a project or from a measure of quality management, and they come together in one list.

*German: To-do* · [Manual](../manual_user/basic_concepts/To_Dos_Basics.md)

### Trash (Platform)

The trash of a folder. Deleted files and subfolders land there first and can be restored; after 30 days the system deletes them for good. The administration sets the period or switches the automatic deletion off.

*German: Papierkorb* · [Manual](../manual_user/basic_concepts/Folder_Concept.md)

### User (Platform)

The human behind an account. The term stands wherever the person is meant and not their technical access.

*German: Person*

### User management

The area for creating, searching, editing, importing and deleting accounts and for granting the roles.

*German: Kontoverwaltung* · [Manual](../manual_admin/usermanagement/index.md)

### User Properties

The fields of an account such as first name, e-mail or institution. The administration decides per property and per usage context whether it is used, whether it is mandatory, whether only administrators see it and whether the person may change it themselves.

*German: Benutzer:innen-Attribute* · [Manual](../manual_admin/administration/Customizing.md)

### User sessions

The Administration page under System that shows the signed-in sessions and ends them one by one or all at once. The Configuration tab holds the session timeout, the maximum number of sessions and the block on new logins.

*German: Aktive Sitzungen* · [Manual](../manual_admin/administration/System.md)

### User tools

The personal tools of a person, reachable everywhere: notes, subscriptions, settings and the like. Which of them are available is configured by the administration.

*German: Persönliche Werkzeuge* · [Manual](../manual_user/personal_menu/Personal_Tools.md)

### Versioning

The module that keeps earlier versions of a file in folders. The administration sets the number of versions, from 2 to 50 or unlimited; every version can be restored or deleted. Switched off by default.

*German: Versionierung* · [Manual](../manual_admin/administration/Files_and_Folders.md)

### Video Collection

The overview of the video learning resources a person has access to.

*German: Video Collection* · [Manual](../manual_user/area_modules/Video_Collection.md)

### Visiting card

The publicly visible page of a person with the entries they have released themselves.

*German: Visitenkarte* · [Manual](../manual_user/personal_menu/Profile.md)

### WebDAV

A separate password for file access through WebDAV. It is kept apart from the sign-in password, because WebDAV programs store the password permanently.

*German: WebDAV* · [Manual](../manual_admin/administration/WebDAV.md)

### Widget

A tile on a dashboard that shows one slice: implementations, offers, members, courses, events or to-dos. The administration sets the active widgets as the system default; every person adapts them for themselves.

*German: Widget* · [Manual](../manual_user/area_modules/Course_Planner_Dashboard.md)

### X (Twitter)

The connection to X, formerly Twitter, for signing in with the X account through OAuth.

*German: X (Twitter)* · [Manual](../manual_admin/administration/Login.md)

## Roles

Who uses the system.

### Absence manager

Organisation role. An administrative organisation role. It manages the events, attendances and absences of its own organisation and closes the events.

*German: Absenzenverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Access roles

The roles for people without a regular account: guest and invitee.

*German: Zugangsrollen*

### Administrative access

The assignment of a learning resource to one or more organisations. It decides which administrators and learning resource managers may manage the resource, regardless of who owns it.

*German: Administrative Freigabe* · [Manual](../manual_user/learningresources/Access_configuration.md)

### Administrator

Organisation role. An organisation role that unites all administrative roles of one organisation. It is the superuser of that organisation. Its reach ends at its own organisation and its sub-organisations; it does not act system-wide and does not open the system configuration.

*German: Administrator:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Applicant

Selectus role. A person who applies for a call in Selectus.

*German: Bewerber:in*

### Author

Organisation role. An organisation role. It allows learning resources to be created in the authoring area. Authors manage their own resources, not those of the organisation.

*German: Autor:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Business analyst / Supplier

A role in the project for external supply or analysis. It creates and edits objects in the project but manages no members.

*German: Business-Analyst:in / Lieferant:in* · [Manual](../manual_user/area_modules/Project_Member_Management.md)

### Certification program owner

A role in the Course Planner. Certification program owners manage a certification program: they add members, renew or revoke certificates and maintain the settings and messages.

*German: Zertifikatsprogrammbesitzer:in* · [Manual](../manual_user/area_modules/Course_Planner_Certification_Programs.md)

### Coach

Course role. A course role. Coaches accompany the participants of a course or a group, see all results and assess them. They do not change the configuration of the course.

*German: Betreuer:in* · [Manual](../manual_user/basic_concepts/coach.md)

### Committee member

Selectus role. A member of the appointment committee who judges the applications assigned to them and records reviews.

*German: Kommissionsmitglied*

### Comparative assessment expert

Selectus role. An expert who judges several applications of the same call against each other in one comparative assessment.

*German: Vergleichsgutachter:in*

### Corrector

Course role. A person who grades a particular test submission by hand in the correction workflow. They receive the job through the grading assignments and need no role in the course.

*German: Korrektor:in* · [Manual](../manual_user/area_modules/Coaching_Order_Management.md)

### Course and group roles

The roles granted in a course or in a group: owner, coach, participant. They apply in that one resource only.

*German: Kurs- und Gruppenrollen* · [Manual](../manual_user/basic_concepts/Roles.md)

### Course planner

Organisation role. An administrative organisation role. It creates products, elements and implementations in the Course Planner, manages their members and assigns courses to them.

*German: Kursplaner:in* · [Manual](../manual_user/area_modules/Course_Planner.md)

### Course Planner roles

The roles that hang on a product or an element of the Course Planner and reach from there into the courses.

*German: Course-Planner-Rollen* · [Manual](../manual_user/area_modules/Course_Planner.md)

### Education manager

Organisation role. An administrative organisation role for training responsibility. In coaching it sees the same overview as the line managers and additionally takes on administrative tasks such as checking booking orders and blocking accounts.

*German: Ausbildungsverantwortliche:r* · [Manual](../manual_user/basic_concepts/Roles.md)

### Element owner

Curriculum role. Manages a single element in the Course Planner, usually an implementation, with its members and courses. The reach ends at that element.

*German: Elementbesitzer:in* · [Manual](../manual_user/area_modules/Course_Planner.md)

### Ex-Officio

Selectus role. A person who belongs to the appointment committee by virtue of their office. The visibility of comments and reviews is configured separately for this role.

*German: Ex-Officio*

### Expert

Selectus role. An external specialist appointed by the committee who writes an expert opinion on an application.

*German: Gutachter:in*

### External expert

Selectus role. A specialist from outside the organisation who writes an expert opinion on an application. They are given access only to the applications assigned to them.

*German: Externe:r Gutachter:in*

### Faculty member

Selectus role. A member of the faculty who is asked for feedback on an application without belonging to the appointment committee.

*German: Fakultätsmitglied*

### Group manager

System role. A system role. It manages the groups of the whole system. It is a system role and not an organisation role, because groups are not assigned to an organisation so far.

*German: Gruppenverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Guest

Access role. Access without signing in, with read access to the resources explicitly released for guests. Guests have no account, do not become members and leave no assessment behind.

*German: Gast* · [Manual](../manual_user/basic_concepts/guest_access.md)

### Head of Committee

Selectus role. Leads the appointment committee, sees all applications and steers the procedure.

*German: Kommissionspräsidium*

### Home base

The organisation a person belongs to through the User role. It decides which accounts and which offers this person sees. Every account has at least one home base.

*German: Home Base*

### Inheritance

The passing on of an administrative organisation role to the sub-organisations. Whoever manages an organisation thereby manages everything below it. The User role is not inherited.

*German: Vererbung*

### Invitee

Access role. An external person who is given access to a single resource through an invitation. The account comes into being with the invitation, belongs to no organisation and expires with it.

*German: Einladung* · [Manual](../manual_user/basic_concepts/Assign_Roles.md)

### Leader

A role in the project for the lead in substance. Leaders edit the project, create objects, close them and manage the members. They do not manage external members.

*German: Leiter:in* · [Manual](../manual_user/area_modules/Project_Member_Management.md)

### Learning resource manager

Organisation role. An administrative organisation role. It manages the learning resources assigned to its organisation through the administrative access, without being an owner itself.

*German: Lernressourcenverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Line manager

Organisation role. An administrative organisation role for line responsibility. In coaching it sees the learning progress of the staff reporting to it across products, implementations and courses. It can receive a copy of their certificates if the administration switches that on.

*German: Linienvorgesetzte:r* · [Manual](../manual_user/basic_concepts/Roles.md)

### Master coach

A role in the Course Planner. Master coaches look after the participants of an implementation across all the courses it contains, even where they are not entered as coaches in the single courses.

*German: Klassenlehrer:in* · [Manual](../manual_user/area_modules/Coaching_Events_Absences.md)

### Organisation roles

The roles that hang on an organisation. Their reach ends at that organisation and its sub-organisations. All of them except User are administrative and are inherited by sub-organisations.

*German: Organisationsrollen* · [Manual](../manual_user/basic_concepts/Roles.md)

### Owner

Course role. A course role with full responsibility for a learning resource. Owners edit the content, configure the resource, publish it and grant the other course roles.

*German: Besitzer:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Participant

Course role. A course role. Participants work through the course and see their own results only.

*German: Teilnehmer:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Portfolio roles

The roles the owner of a portfolio binder grants in the sharing tab. They apply in that one binder only.

*German: Portfoliorollen*

### Principal

Organisation role. An organisation role with the same reach as Administrator, but read only. Principals see the objects of their organisation and do not change them.

*German: Principal* · [Manual](../manual_user/basic_concepts/Roles.md)

### Product owner

Curriculum role. Manages a whole product in the Course Planner with all elements and implementations below it.

*German: Produktbesitzer:in* · [Manual](../manual_user/area_modules/Course_Planner.md)

### Project manager

Organisation role. An administrative organisation role. It manages the projects of its own organisation, without being a member itself.

*German: Projektverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Project office

A role in the project for the administrative lead: events, files and minutes. It does not lead the project in substance.

*German: Projektbüro* · [Manual](../manual_user/area_modules/Project_Member_Management.md)

### Project roles

The roles inside a project.

*German: Projektrollen*

### Quality manager

Organisation role. An administrative organisation role. It plans the data collections of quality management, runs them and analyses the results.

*German: Qualitätsverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Question bank manager

System role. A system role. It manages the question bank with the questions, the collections, the shares and the review process. It is a system role and not an organisation role, because the question bank is not assigned to an organisation so far.

*German: Poolverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Referee

Selectus role. A person named by the applicant who writes a letter of reference.

*German: Referenzperson*

### Reviewer (Reviewer:in)

Course role. A participant who reviews the work of another in the peer review.

*German: Reviewer:in* · [Manual](../manual_how-to/peer_review/peer_review.md)

### Reviewer (Gutachter:in)

Portfolio role. A person the owner of a portfolio binder gives read and comment rights on the binder, a section or an entry. They read and comment but do not assess; that sets them apart from the coach role in the sharing tab.

*German: Gutachter:in*

### Roles manager

Organisation role. An administrative organisation role. It grants and withdraws roles on the accounts of its own organisation.

*German: Rollenverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### Secretary

Selectus role. Supports the appointment committee administratively and prepares the correspondence.

*German: Sekretariat*

### Selection roles

The roles in the appointment procedure of Selectus, from the administrative staff through the committee to the external experts.

*German: Rollen im Auswahlverfahren*

### Selectus manager

Organisation role. An administrative organisation role. It manages the appointment procedures in Selectus: calls, committees and templates of its own organisation.

*German: Selectusverwalter:in*

### Sponsor / Client

A role in the project for the commissioning party. It reads the state of the project but has no access to the objects in it.

*German: Sponsor:in / Auftraggeber:in* · [Manual](../manual_user/area_modules/Project_Member_Management.md)

### Staff

Selectus role. The administrative body that creates calls, manages the applications and handles the correspondence.

*German: Sachbearbeitung*

### Steering committee

A role in the project for oversight. It reads the state of the project but has no access to the objects in it and does not work in it.

*German: Lenkungsausschuss* · [Manual](../manual_user/area_modules/Project_Member_Management.md)

### System administrator

System role. A system role. It opens the Administration area and thereby the system configuration. It grants no rights on objects: without an additional organisation role a system administrator sees neither courses nor accounts.

*German: Systemadministrator:in* · [Manual](../manual_user/basic_concepts/Roles.md)

### System roles

The three roles that apply to the whole system and belong to no organisation: system administrator, group manager, question bank manager. The last two only because groups and the question bank are not assigned to an organisation so far.

*German: Systemrollen*

### Teacher

Course role. A person who holds an event. They record the attendance and close the event. The role belongs to the event and not to the course.

*German: Dozent:in* · [Manual](../manual_user/learningresources/Events_and_absences.md)

### User (Roles)

Organisation role. The base role of every account, also called the home base. It sets what a person sees at all: the accounts of their home base and the courses with an offer for their home base. It is not administrative and is not inherited by sub-organisations.

*German: Benutzer:in* · [Manual](../manual_user/basic_concepts/User_Types.md)

### User manager

Organisation role. An administrative organisation role. It manages the accounts of its own organisation: create, edit, import, block and delete.

*German: Benutzerverwalter:in* · [Manual](../manual_user/basic_concepts/Roles.md)

## Integrations and standards

Third-party systems and open standards.

### Adobe Connect (Integrations and standards)

The connection to the web conferencing system Adobe Connect.

*German: Adobe Connect* · [Manual](../manual_user/learningresources/Course_Element_Adobe_Connect.md)

### Analytics module

The module that embeds an external service for analysing usage behaviour: where people spend their time, which browsers and devices they use. Google Analytics and Matomo are available. The operator must inform people about the service.

*German: Analytics Modul* · [Manual](../manual_admin/administration/Analytics_module.md)

### BigBlueButton (Integrations and standards)

The connection to the free web conferencing system BigBlueButton. Coaches create online meetings in the course element, the course, the group, the appointment scheduling and the coach chat. OpenOlat balances the load across several BigBlueButton servers and controls the rooms through room templates. Recordings are kept on the BigBlueButton server or in Opencast.

*German: BigBlueButton* · [Manual](../manual_user/learningresources/bigbluebutton/index.md)

### card2brain

The connection to the flashcard platform card2brain for learning with online flashcards.

*German: card2brain* · [Manual](../manual_user/learningresources/Course_Element_card2brain_Flashcards.md)

### Deep Linking

A service of LTI 1.3 with which authors pick a specific content of the external tool in the course element LTI page instead of entering only its start address. Administration enables it per tool; the button "Select content" then opens the tool's content picker.

*German: Deep Linking* · [Manual](../manual_admin/administration/LTI_Deeplinking.md)

### Deployment

The configured connection to an LTI tool or an LTI platform, with keys, addresses and the statement of which data is transferred. A deployment applies to a single course or group (local) or to the whole system (global, with shared deployment).

*German: Deployment* · [Manual](../manual_admin/administration/LTI_External_tools.md)

### Document editor

An embedded editor with which files in the folders of OpenOlat are opened and edited in the browser. Administration enables the editors one by one and can restrict their use to roles.

*German: Dokumenteneditor* · [Manual](../manual_admin/administration/External_Tools_-_Administration.md)

### draw.io

The connection to the diagram editor draw.io. It provides the whiteboard in the Projects module and the diagram editor in the file areas.

*German: draw.io* · [Manual](../manual_admin/administration/External_Tools_-_Administration.md)

### Edubase (Integrations and standards)

The connection to the textbook platform Edubase. Participants open the licensed e-books straight from the course.

*German: Edubase* · [Manual](../manual_user/learningresources/Course_Element_Edubase.md)

### edu-sharing (Integrations and standards)

The connection to the edu-sharing repository. Content stays in the education cloud and is referenced in the course.

*German: edu-sharing* · [Manual](../manual_user/learningresources/Course_Element_edu_Sharing.md)

### Google Analytics

The connection to Google Analytics through a tracking ID. The analysis is held by Google.

*German: Google Analytics* · [Manual](../manual_admin/administration/Analytics_module.md)

### GoToMeeting (Integrations and standards)

The connection to GoToMeeting and GoToTraining for virtual sessions.

*German: GoToMeeting* · [Manual](../manual_user/learningresources/Course_Element_GoToMeeting.md)

### JupyterHub (Integrations and standards)

The connection to JupyterHub through LTI 1.3. Participants get their own Jupyter environment for interactive computing from inside the course; the course element sets which image the hub starts.

*German: JupyterHub* · [Manual](../manual_user/learningresources/Course_Element_JupyterHub.md)

### LTI

The Learning Tools Interoperability standard. It connects a learning platform with an external application: the signed-in person needs no second sign-in there, and the application can report points back. OpenOlat is the platform when it embeds a tool in the course, and the tool when it provides a course or a group to another platform.

*German: LTI* · [Manual](../manual_admin/administration/LTI_Integrations.md)

### LTI 1.3 access configuration

The section in the release tab of a course or a group in which OpenOlat is released as a tool for an external platform. One deployment is created per platform; people of the other platform are created as LTI accounts on launch and enter the course as participants or coaches.

*German: LTI 1.3 Zugangskonfiguration* · [Manual](../manual_user/learningresources/LTI_Share_courses.md)

### Matomo (Piwik)

The connection to Matomo through a site ID and a Matomo URL. Matomo runs on the institution's own server, and the analytics data stays in its own infrastructure. OpenOlat adds the Matomo URL to the content security policy.

*German: Matomo (Piwik)* · [Manual](../manual_admin/administration/Analytics_module.md)

### Mediasite

The connection to the video platform Mediasite for lecture recording, video management and captioning. Content is embedded in the course as a single presentation or a channel; the connection runs through LTI 1.1 or LTI 1.3.

*German: Mediasite* · [Manual](../manual_user/learningresources/Course_Element_Mediasite.md)

### Microsoft SharePoint / OneDrive

The connection to Microsoft SharePoint and OneDrive as file storage. In the file hub and the media center files can be copied from SharePoint sites and OneDrive and written back there. Signing in through Microsoft Entra ID is a prerequisite; both services can be enabled separately.

*German: Microsoft SharePoint / OneDrive* · [Manual](../manual_admin/administration/SharePoint_OneDrive.md)

### Microsoft Teams (Integrations and standards)

The connection to Microsoft Teams for online meetings. OpenOlat creates the meeting through the Microsoft Graph API on behalf of the signed-in person; signing in with the organisation's Microsoft account is a prerequisite. Participants join from OpenOlat, and Teams assigns the roles organizer, presenter and attendee.

*German: Microsoft Teams* · [Manual](../manual_user/learningresources/Course_Element_Microsoft_Teams.md)

### OAI-PMH

The Open Archives Initiative Protocol for Metadata Harvesting standard. External catalogues use it to collect the metadata of the published learning resources.

*German: OAI-PMH* · [Manual](../manual_admin/administration/Modules_OAI.md)

### Online meeting (Integrations and standards)

A scheduled session in BigBlueButton or Microsoft Teams with a name, a date, lead and follow-up time, a main presenter and a room template. It is created in the course element, the course, the group or the appointment scheduling; participants join from OpenOlat. A permanent reservation is an online meeting without a date.

*German: Online-Termin* · [Manual](../manual_user/learningresources/bigbluebutton/index.md)

### ONLYOFFICE

The connection to ONLYOFFICE. It allows Office documents to be edited in the browser, by several people at the same time as well.

*German: ONLYOFFICE* · [Manual](../manual_user/area_modules/Project_Files.md)

### Opencast (Integrations and standards)

The connection to the free video management system Opencast. Recordings and series stay on the Opencast server and are only displayed in the course, not copied. Opencast can also take in the recordings of BigBlueButton.

*German: Opencast* · [Manual](../manual_user/learningresources/Course_Element_Opencast.md)

### OpenMeetings (Integrations and standards)

The connection to the free web conferencing system Apache OpenMeetings. Every course element and every group with the group tool gets its own room on the OpenMeetings server.

*German: OpenMeetings* · [Manual](../manual_user/learningresources/Course_Element_OpenMeetings.md)

### Platform

The system that embeds an LTI content and passes the sign-in along, in LTI terminology. In the tab "External platforms" OpenOlat records the foreign systems for which it is the tool itself.

*German: Plattform* · [Manual](../manual_admin/administration/LTI_External_platforms.md)

### QTI 2.1

The Question and Test Interoperability standard, version 2.1. It describes questions, tests and results in a way that lets them be exchanged between systems. OpenOlat uses it for the test, the self-test, the questionnaire and the question pool.

*German: QTI 2.1* · [Manual](../manual_user/learningresources/Test.md)

### REST API

A programming interface following the REST pattern. Third-party systems use it to create accounts, courses and enrolments without going through the interface.

*German: REST API* · [Manual](../manual_admin/administration/REST_API.md)

### Role mapping

The mapping of the OpenOlat course roles onto the roles of the LTI tool. It decides who may assess in the external tool and who may only work in it.

*German: Rollen-Mapping* · [Manual](../manual_admin/administration/LTI_Role_Mapping.md)

### Room template

A system-wide template for BigBlueButton rooms that is chosen when an online meeting is created. It sets the functions and presets in the room, the number of participants, the duration, the number of simultaneous rooms and the roles that may use it.

*German: Raumvorlage* · [Manual](../manual_admin/administration/BigBlueButton_module.md)

### SCORM

The Sharable Content Object Reference Model standard. It packages learning content so that it runs in any learning system and reports progress and points back.

*German: SCORM* · [Manual](../manual_user/learningresources/Course_Element_SCORM_Learning_Content.md)

### Tool

The external application connected through LTI.

*German: Tool* · [Manual](../manual_admin/administration/LTI_External_tools.md)

### Virtual classroom

A room for a session in real time, with video, audio, a shared screen and a recording. OpenOlat does not provide it itself but embeds a third-party system.

*German: Virtuelles Klassenzimmer* · [Manual](../manual_user/basic_concepts/Virtual_classrooms.md)

### vitero (Integrations and standards)

The connection to the web conferencing system vitero with booked team rooms.

*German: vitero* · [Manual](../manual_user/learningresources/Course_Element_vitero.md)

### YouTube API

The connection to the YouTube programming interface through an API key. When a YouTube video is embedded it fetches the title, the description, the licence, the duration and the thumbnail.

*German: YouTube API* · [Manual](../manual_admin/administration/External_Tools_-_Administration.md)

### Zoom (Integrations and standards)

The connection to Zoom through LTI 1.3 and the Zoom LTI Pro app. Zoom meetings are available as a course element, a course tool and a group tool; the connection to the Zoom account is a Zoom profile. A Zoom Education or Enterprise licence is a prerequisite.

*German: Zoom* · [Manual](../manual_admin/administration/Zoom.md)

### Zoom profile

The connection from OpenOlat to a Zoom account through a Zoom LTI Pro credential. A profile carries the LTI key from Zoom; OpenOlat produces the client ID and the access token for it, which are entered in Zoom. Several profiles are possible.

*German: Zoom-Profil* · [Manual](../manual_admin/administration/Zoom.md)

## Artificial intelligence

The AI module and the features on top of it.

### AI call

A single request from OpenOlat to an AI model, triggered by an AI feature. Every call is recorded as a row in the usage log, with the feature, provider, model, duration, tokens and the status Success or Failed.

*German: KI-Aufruf* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### AI Feature

One place of use of AI in the product, for example the MC question generator. Every feature is switched on individually and is given a provider, a model, an upper limit for input and output, and a timeout.

*German: KI Funktion* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### AI feedback

The formative feedback learners fetch on their free text answer in the quiz of a page. It consists of the assessment, an overall assessment, the reliability and the sections "What went well", "What is missing", "Next step" and "Language". It awards no points. In the question editor the tab that holds the grading kit carries the same name.

*German: KI-Feedback* · [Manual](../manual_user/basic_concepts/Content_Editor.md)

### AI module

The module that manages the connection to AI services: which providers are available, which features are active, which model each feature uses and how many calls may run at the same time. It provides no feature for learners itself but serves the features of other modules.

*German: KI Modul* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### AI processing pool

The quota of simultaneous AI calls per server node. The AI module keeps two pools apart, so that one long job does not block the calls someone is waiting for.

*German: KI-Verarbeitungs-Pool* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### AI Provider

The service whose models an AI feature uses. Several providers can be set up at the same time, and each feature picks one of them. A provider is only ready for use once its API key has been checked.

*German: KI Anbieter* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Anthropic Claude

The AI provider Anthropic Claude, connected through an API key. Using it produces costs on the operator's account.

*German: Anthropic Claude* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Embedding model

A model that turns text into a vector of numbers, so that closeness in meaning can be computed. Taxonomy matching uses it to assign a text to the right taxonomy level. It produces no text.

*German: Einbettungsmodell* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Essay Grading

The AI feature that produces formative feedback on the free text answers of learners. It supplies hints on the answer, no grade and no status. It works only in the quiz of a page, not in the course elements test and self-test. The assessment stays with the coaches.

*German: Essay Bewertung* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Essay Question Generator

The AI feature that produces free text questions together with grading criteria from a source text or an uploaded file. The criteria are the basis essay grading later produces feedback from.

*German: Essay Fragen Generator* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Generic AI Provider

An AI provider connected through an OpenAI-compatible interface, for example vLLM, Ollama or LiteLLM. It allows a model to be run in the institution's own data centre, so that no data leaves the house. Every installation carries such a provider under the fixed identifier Generic_0.

*German: Generischer KI Anbieter* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Grading kit (reference + model answer)

What essay grading measures an answer against: learning objective, reference excerpt, model answer, key points, rubric criteria and common misconceptions. The essay question generator fills it in, the author maintains it in the tab "AI feedback" of the question. Without the kit the AI has no yardstick.

*German: Bewertungs-Kit (Referenz + Musterantwort)* · [Manual](../manual_user/area_modules/Question_Bank_Create_Questions.md)

### Image Description Generator

The AI feature that produces a title, a description, alt text and keywords for uploaded images. The alt text is the part that counts for accessibility. In the media center it starts from a button, on Markdown import into the content editor it runs in the background. It is not available for SVG images.

*German: Bildbeschreibungs-Generator* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Language model

The model of a provider that an AI feature calls. A separate model is chosen per feature, so that expensive models only run where they are needed.

*German: Sprachmodell* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### MC Question Generator

The AI feature that produces suggestions for multiple choice questions from a source text or an uploaded file, in the question pool and in the quiz of a page. The generation runs in the background. The suggestions are drafts: generated questions get the status Review, and every question must be checked for correctness one by one.

*German: MC Fragen Generator* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### ONNX embedding model

An embedding model in the ONNX format that OpenOlat loads from a model directory on its own server. It supplies embeddings for taxonomy matching only and no language model. It needs no API key, and no text leaves the server.

*German: ONNX Einbettungsmodell*

### OpenAI

The AI provider OpenAI, connected through an API key. Using it produces costs on the operator's account.

*German: OpenAI* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Pool "Batch" (threads)

The pool for long-running AI jobs such as generating questions from page content. Such a job can take several minutes.

*German: Pool "Batch" (Threads)* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Pool "Interactive" (threads)

The pool for AI tasks a person is actively waiting for, for example the feedback on a free text answer. It must be large enough to serve a learning group submitting at the same time.

*German: Pool "Interaktiv" (Threads)* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Taxonomy Matching (Embeddings)

The AI feature that assigns a text to the right taxonomy level using an embedding model. It suggests a placement instead of leaving it to be searched for by hand.

*German: Taxonomie-Zuordnung (Embeddings)* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Usage log

The record of all AI calls of an installation with the feature, provider, model, status, duration and tokens. It is the basis for cost control and for answering what the AI was used for. It can be analysed by time range and exported as an Excel file.

*German: Nutzungsprotokoll* · [Manual](../manual_admin/administration/External_Tools_AI.md)

### Vision model

A model that can read images. The image description generator needs it, because a pure language model does not see an image.

*German: Vision Modell* · [Manual](../manual_admin/administration/External_Tools_AI.md)
