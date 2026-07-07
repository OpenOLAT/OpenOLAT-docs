# Course Element "Document" {: #document}

## Profile

Name | Document
---------|----------
Icon | :fontawesome-regular-file:
Available since | Release 15.3
Functional group | Knowledge Transfer
Purpose | Provision of various documents, also for joint editing
Assessable | no
Specialty / Note | For office documents, appropriate licenses are required for editing


By means of the course element "Document" different document formats can be integrated into the course. Documents in this course element are typically displayed *directly* to users.

### For which file types is the course element intended? [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

The course element is well suited for displaying PDF, JPG and PNG files. In addition, if activated by the OpenOlat administrator, Office documents (Word, Excel, PowerPoint) and draw.io diagrams [:octicons-tag-16:{ title="since Release 18.1 (OO-7090)" }](https://track.frentix.com/issue/OO-7090){:target="_blank"} can also be integrated.

OpenOlat uses an integrated PDF viewer (pdf.js) [:octicons-tag-16:{ title="since Release 18.1 (OO-6996)" }](https://track.frentix.com/issue/OO-6996){:target="_blank"} which provides clear rendering. Large PDF files are loaded progressively if the file supports this. The PDF viewer is read-only: a separate editor is required for editing.

!!! note "Note"

    For video files the course element ["Video"](../learningresources/Course_Element_Video.md) should be used, and for HTML pages the course element ["Single page"](../learningresources/Course_Element_HTML_Page.md), instead of the course element "Document".

### How do files get into the course element? [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

Configuration takes place in the "Document" tab of the course editor. There are many ways for files to get into the course element. Files can generally be uploaded, linked, or newly created.

![Integrate files into the Document course element](assets/KB_Dokument.png){ class="lightbox" }


#### Upload a file [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

You can ...

* **"Transfer from local computer"** a file. Select "Choose file" or drag and drop the file.
* upload a file as a learning resource and import it into the course: → **"From learning resource management" → "Import file"**.

#### Link a file [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

You can ...

* select a file already placed in the course's storage folder beforehand: → **"From storage folder"**.
* select a file already uploaded as a learning resource: → **"From learning resource management"**

#### Create a file [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

To newly create a file for the course element, select **"Create document"** and choose the desired file format.

![Create document](assets/Dokument_erstellen.png){ class="lightbox" }

Alternatively, a new file can also be created as a learning resource. To do this, select: **"From learning resource management" → "Create"**.

If **draw.io diagrams** [:octicons-tag-16:{ title="since Release 18.1 (OO-7090)" }](https://track.frentix.com/issue/OO-7090){:target="_blank"} have been activated by the OpenOlat administrators, draw.io diagrams can also be created in the Document course element and made available to users. To do this, select the option "Create document" → "Show more formats" → "Diagram" or "Whiteboard".

draw.io diagrams support simultaneous editing by multiple users [:octicons-tag-16:{ title="since Release 18.1 (OO-7091)" }](https://track.frentix.com/issue/OO-7091){:target="_blank"}. Multiple participants can open and edit a diagram at the same time. Changes are synchronized in real time. This makes the Document course element with draw.io suitable for collaborative group work.

!!! info "Important"

    Under heavy simultaneous use, synchronization may be briefly interrupted. Reloading the document restores the connection.

### Configure preview height [:octicons-tag-16:{ title="since Release 15.4 (OO-5116)" }](https://track.frentix.com/issue/OO-5116){:target="_blank"}

In the "Document" tab of the course editor, the height of the document preview can be set. By default, **"Automatic"** is selected — the document uses the available page space. For certain formats (e.g. PowerPoint) this may result in black borders. A fixed height allows for precise adjustment of the display.

### Document display in Lightbox mode [:octicons-tag-16:{ title="since Release 18.1 (OO-6957)" }](https://track.frentix.com/issue/OO-6957){:target="_blank"}

Documents, images and videos are displayed by default in **Lightbox mode**: as an overlay on the current page, without opening a new browser window. When switching to editing mode, the document continues to open in a separate window.

### Make changes [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

Integrated documents can also be edited later if needed, and their metadata can be changed. It is also possible to replace the document completely. What exactly is possible depends on the file type.

![Edit document](assets/Dokument_bearbeiten.png){ class="lightbox" }


### Configure permissions [:octicons-tag-16:{ title="since Release 15.3 (OO-4801)" }](https://track.frentix.com/issue/OO-4801){:target="_blank"}

After a document has been linked to the course element, it can be defined which user roles are allowed to edit or download the document. After downloading a corresponding document, the metadata shows who last edited the document.

These permissions allow various scenarios to be implemented with the course element, including collaborative ones.

!!! info "Important"

    If downloading is not permitted for a role, printing is automatically disabled for that role as well: the Print button and the menu entry in the PDF viewer are no longer displayed [:octicons-tag-16:{ title="from Release 20.3.4 (OO-9530)" }](https://track.frentix.com/issue/OO-9530){:target="_blank"}.