# The Portfolio Editor {: #portfolio_editor}

Different layouts and content elements can be added to each portfolio entry. You can also continue to fill older entries using these layouts. The configuration is carried out via three controls: the layout menu, the block menu and the inspector.

## Controls Overview

The Portfolio Editor includes various menu areas for configuration:

![Portfolio Editor with its controls: layout menu in the header of a layout, block menu with gear and handle above a content element, on the right the inspector of the selected image](assets/content-editor-gui.jpg){ class="shadow lightbox" }

* **Layout menu**: A layout is a higher-level block that allows you to structure the content in different ways using columns and rows. In the layout menu, you can select a single or multi-column layout, move layout areas or add new layouts. If you delete or change layouts, existing blocks are moved into the existing columns. The following layout templates are currently available:
![Nine layout templates with one to three columns, rows and mixed divisions](assets/layoutblock-template.jpg){ class="shadow lightbox" }
* **Block menu**: Menu of an individual content element within a layout. A content element can be moved, added or deleted via the block menu. The inspector with further settings for a content element can also be activated via the gear wheel :o_icon_o_icon_inspect:.
* **Inspector**: Used to configure individual content elements. It contains all settings that change the functionality as well as the appearance of the respective element, e.g. the alignment of images. By clicking on the title bar of the inspector window, you can also move the configuration menu itself. When you select a new block, the inspector jumps back to the default position.

**Alert box in the inspector**

Another interesting feature is the option to add an alert box to the content elements. This option is available for almost all content elements except for title and HTML text code.

![Inspector of a text element with the alert box switched on, type Important, own title and the options With icon and Collapsible; on the left the text as a highlighted box with icon and title](assets/Hinweis-Box.png){ class="shadow lightbox" }

Individual content elements can be highlighted and marked as Info, Tip, Important, etc. It is also possible to assign your own title. In addition, the alert boxes can be provided with an icon and it can be defined whether the alert box is collapsible or not. For user-defined alert types, an icon can also be selected from the list and the color can be adjusted. For predefined types, these things are predefined.

## Content blocks - add content

The specific content elements such as texts, images or other media are added via "Add content". The following content elements are available:

![Dialog Add content with the content elements in the groups Content and Layout](assets/add_content_portfolio_en.png){ class="shadow lightbox" }

### Title

Use this element to add a heading quickly and easily.

In the inspector, a size from h1 to h6 can be set, where h1 corresponds to "Heading 1" and is therefore the largest and h6 corresponds to "Heading 6" and is therefore the smallest. In the "Layout" tab, as with most content elements, the distance to the text can also be defined.

![Title element with opened inspector, tab Style, selection list Size with the value h3](assets/Titel_Portfolio.png){ class="shadow lightbox" }

### Text

Use this element to insert any text passages. The text can be formatted appropriately using the editor, e.g. for bold print, links, font color etc.

### Table

Use this content element if you want to add a table to your portfolio. Define the number of rows and columns of a table and add a header row. Then fill in the respective table fields. In the inspector, you also define the header column and header row, the options "Striped" and "Bordered" and the color; a table caption is optional.

![Table element with title, header column and caption field; in the inspector the fields Row and Column, the options header column, header row, Striped and Bordered and the color selection](assets/Editor_Tabelle_Portfolio.png){ class="shadow lightbox" }

### Math formula

Click in the editing field and you will be given access to a special formula editor. You can either enter the formula in the graphical editor or in the LaTeX editor.

![Formula element with the formula 7 squared and the graphical formula editor with keypad for numbers, functions, symbols and Greek letters](assets/Mathe_Formeln_Portfolio.png){ class="shadow lightbox" }

### Code example

Element for inserting programming code. The content is displayed as code and is not executed. Various code languages are available for selection. Line numbers can also be displayed for better overview.

![Code example with HTML source code and line numbers; in the inspector the code language HTML, XML, the switch for line numbers and the number of lines to display](assets/Code-Beispiel_Editor_19.png){ class="shadow lightbox" }

### Citation

Here you can create new citations (Add citation) or use citations already stored in the Media Center and integrate them. Various information can be added to a new citation, e.g. source, language, author, URL.

### Image

Add image elements by uploading a graphic file or accessing a graphic from your Media Center. You can then configure the file further, e.g. place a title or subtitle and also define the size, placement or border. Use the inspector for this.

!!! tip "Tip"

    To optimize the positioning of a graphic, it is best to use a suitable, e.g. multi-column layout. Depending on the type of graphics, this tip also applies to the "Gallery" content element.

### Gallery [:octicons-tag-16:{ title="from Release 19.0.0 (OO-7142)" }](https://track.frentix.com/issue/OO-7142){:target="_blank"}

With the content element "Gallery" you add a picture gallery. Clicking on the "Add" button opens the Media Center, in which several images can be selected. The display type (preview, grid or slideshow) can be defined in the inspector. The example shown presents a gallery with preview from the perspective of the readers.

![Gallery element in the display type preview: large image with title, arrows for browsing and three thumbnails below](assets/Editor_Galerie_Portfolio.png){ class="shadow lightbox" }

### Image comparison [:octicons-tag-16:{ title="from Release 19.0.0 (OO-7143)" }](https://track.frentix.com/issue/OO-7143){:target="_blank"}

With the content element "Image comparison" you place 2 images from the Media Center next to each other, e.g. two versions of the same image. The images are selected via the inspector. In addition to the standard type, the image comparison can also be used to compare a correct and an incorrect image.

![Image comparison with two images side by side, slider in the middle and the labels Icon Vorschlag 1 and Icon Vorschlag 2; on the left the inspector with the settings for image 2](assets/Editor_Bildervergleich_Portfolio.png){ class="shadow lightbox" }

Readers can adjust the viewing area of the images using a slider.

### Video

You have the following options for loading a video into the editor and providing it:

* Add video: Upload an mp4 video file
* Add video via URL
* Record video: Create a video recording with the webcam
* Select and add a video file that is located in the Media Center.

![Dialog Select video in the Media Center with the button Add video and the opened menu Add video via URL and Record video, below it the tabs, filters and existing videos](assets/Video_Portfolio_Editor19.png){ class="shadow lightbox" }

### Audio

You have the following options for loading an audio into the editor and providing it:

* Use the integrated audio editor and create a sound recording (Record audio)
* Upload an audio file (Add audio)
* Connect an audio file from your Media Center (selection from the list).

![Dialog Select audio with the buttons Record audio and Add audio, the tabs from All to Search, the filters and an existing test recording](assets/Audio_Portfolio_19.jpg){ class="shadow lightbox" }

### Document

You have the following options for loading a document into the editor and providing it:

* Create a new document according to the specified file types (Create document)
* Upload a new document (Add document) or
* Connect a document from your Media Center (selection from the list).

If an external document editor is activated and the files are in a format that is supported by it, the files can also be edited directly online in OpenOlat.

!!! info "Important"

    The contents of the files are not displayed directly here, but must be opened by clicking on the link.

### Diagram

You can create a new draw.io diagram or add an existing draw.io diagram from your Media Center. The actual design of the diagram is done by clicking on the "Edit" link in the entry.

![Diagram element with a draw.io diagram and the link Edit; on the right the inspector in the tab Title with the fields Title, Where with the value Above image and Title style](assets/Editor_Diagramm_Portfolio.png){ class="shadow lightbox" }

When creating a diagram, you can also define whether or who is allowed to edit the diagram.

### Separator

Adding a separator line.

### HTML text code

A similar but slightly extended text editor appears here as for the "Text" content element.

### Media Center

Instead of selecting a specific content element, you can also switch directly to your [Media Center](../personal_menu/Media_Center.md) and select elements stored there or upload or add media files.

The search and filter options help you to find the desired file(s) quickly.

![Dialog My Media Center with the button Add media file and the menu for document, draw.io diagram, text, video via URL, video and audio recording and citation, below it the media list](assets/Medien_Center_Portfolio.png){ class="shadow lightbox" }

## Further information {: #further_information}

[Personal tools: Media Center >](../personal_menu/Media_Center.md)

[To the top of the page ^](#portfolio_editor)
