# Course Element "Document" {: #document}

## Profile

Name | Document
---------|----------
Icon | ![Document Icon](assets/course_element_document_icon.png){ class=size24 }
Available since | Release 15.3
Functional group | Knowledge Transfer
Purpose | Provision of various documents, also for joint editing
Assessable | no
Specialty / Note | For office documents, appropriate licenses are required for editing


By means of the course element "Document" different document formats can be integrated directly into the course. This course element is especially suitable for Office documents, PDF or the display of graphic files. It is possible to access already existing files or to upload or create new files. Word processing documents and PDF are directly displayed by using the integrated Document Viewer.

Files that are located in the course's storage folder or uploaded as separate learning resource can be used. Which file formats can be newly created depends on the settings in the administration of the respective OpenOlat instance.

The integrated documents can later be edited, exchanged or saved as a separate learning resource. Depending on the file type, other options such as editing metadata are also possible. Editing of text documents is also possible when the corresponding licenses are activated in the OpenOlat Administration, the editor then opens in a separate window.

Furthermore you can set user rights for your course element in the course editor and thus define which roles are allowed to edit and download the respective document (if possible). The height of the display area can also be defined.

After downloading a corresponding document, the metadata shows who edited the document last.

!!! warning "Note"

    For video files the course element "Video" should be used and for HTML pages the course element "Single page" instead of "Document".

As of Release 18.1, OpenOlat uses an integrated PDF viewer (pdf.js) :octicons-tag-16:{ title="since Release 18.1 (OO-6996)" } which provides significantly better rendering than the previous OnlyOffice view. Large PDF files are loaded progressively if the file supports this. The PDF viewer is read-only — a separate editor is required for editing.

draw.io diagrams :octicons-tag-16:{ title="since Release 18.1 (OO-7090)" } support simultaneous editing by multiple users :octicons-tag-16:{ title="since Release 18.1 (OO-7091)" }. Multiple participants can open and edit a diagram at the same time — changes are synchronized in real time. This makes the Document course element with draw.io suitable for collaborative group work. To create a diagram, select **"Create document" → "Show more formats" → "Diagram"** or **"Whiteboard"**.

!!! warning "Note"

    Under heavy simultaneous use, synchronization may be briefly interrupted. Reloading the document restores the connection.

### Configure preview height :octicons-tag-16:{ title="since Release 15.4 (OO-5116)" }

In the "Document" tab of the course editor, the height of the document preview can be set. By default, **"Automatic"** is selected — the document uses the available page space. For certain formats (e.g. PowerPoint) this may result in black borders. A fixed height allows for precise adjustment of the display.

### Document display in Lightbox mode :octicons-tag-16:{ title="since Release 18.1 (OO-6957)" }

As of Release 18.1, documents, images and videos are displayed by default in **Lightbox mode** — as an overlay on the current page, without opening a new browser window. When switching to editing mode, the document continues to open in a separate window.