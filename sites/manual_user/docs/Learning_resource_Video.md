#  [Learning resource: Video](Learning+resource%EF%B9%95+Video.html)

![](../../download/attachments/590936/video_settings.png)

![](../../download/attachments/590039/video_64_0_434343_none.png)

A video learning resource is created in authoring with the feature
"[Import](Actions+in+the+'Authoring'+section.html)" or "Import URL".

Therefore you select the desired video-file in the upload window and click on
"Import". In the following step the form opens on info page.

Warning

To be recognized in OpenOlat as a video learning resource a video file
[prepared](Video+Upload.html) for the import needs to be in the .mp4 form.

If a description is indicated on the [info
page](https://confluence.openolat.org/display/OO161EN/Info+Page%3A+Add+Meta+Data)
after the import, it can be shown as course description when embedding into
the course.

If YouTube videos are imported via "Import URL" YouTube, metadata of the
YouTube file, such as the title or a start image, are also imported.

  

  * 1 Learning resource: Video 
    *       * 1.1.1Video settings
        * 1.1.1.1Metadata
        * 1.1.1.2Replace poster
        * 1.1.1.3Chapter
        * 1.1.1.4Annotations
        * 1.1.1.5Quiz
        * 1.1.1.6 Subtitle configuration
        * 1.1.1.7 Video quality
      * 1.1.2Download
    * 1.2Embed videos in courses
    * 1.3 Video Collection

### Video settings

You can now further configure your video in the tabs of the "Settings" menu.
The "Info", "Share" and "Catalog" tabs are analogous to other learning
resources. For general information about the Settings menu, click
[here](Course+Settings.html).

#### Metadata

In the tab "Metadata" you find general information like creation date and size
of video file. Furthermore, as in other learning resources, you have the
option to store information on authors, subject areas, main language, time
required and license.

#### Replace poster

In the tab "Replace poster" you determine the picture which should indicate
the video in the course area, in the catalog, on the Video Collection page, in
the authoring as well as in the course. With the help of "Replace poster"
button you can chose between 8 freeze frames of the videos. If you prefer an
own picture, chose the button "Upload poster". If no poster is added, the
freeze frame from the beginning of the video appears.

Please consider that such a pictures needs the same pixel size than the
original video. The corresponding data can be found in the tab "Metadata".

  

#### Chapter

To group a video, chapters can be added. This simplifies especially the
navigation in the video. A chapter is added with the button "Add chapter". The
name of the chapter can be inserted. Additionally the begin of the chapter
needs to be defined.

Alternatively the video can be stopped at the place, where the new chapter
should start. Click the button "Add chapter". The begin is taken over
automatically and only the name of the chapter needs to inserted.

Chapters can be edited and deleted.

  

![](../../download/attachments/590936/chapters.png)

#### Annotations

In addition to the chapter markers, further annotations and comments can also
be stored at any point in the video, e.g. to highlight particularly important
points or to supplement certain aspects.

Select the place where the annotation should be added and define the further
settings, such as the duration, the position where the annotation should
appear and of course the text to be displayed.

![](../../download/attachments/108600738/VideoLR_Marker_EN.png)

#### Quiz

Here you can add individual quiz questions to the video, which are either
created directly or imported from the question pool. There are currently 11
different question types to choose from. The question can then be further
configured. In the tab "Configuration" you can define the time at which the
question should appear, if there is a time limit or if it is allowed to skip
the question or if another attempt is allowed. In the tab "Selection" the
concrete question as well as the answers are deposited. The tab "Score"
defines the type of points to be awarded. In the tab "Feedback" feedbacks
based on different criteria can be added.

Further information on the general settings of quiz and tests can be found in
the chapter "Configuring test questions". For more information on the
different question types, see the "[Test Question
Types](Test+question+types.html)" chapter.

  

![](../../download/attachments/108600738/VideoLR_Quiz_EN.png)

####  Subtitle configuration

A video can be assigned with subtitles in any amount of languages. In OpenOlat
subtitles are uploaded in the [WebVTT format](https://w3c.github.io/webvtt/)
([Wikipedia article](https://en.wikipedia.org/wiki/WebVTT)). The uploaded
files need the ending .srt. Files with the ending .vtt are not supported.
Subtitles can be created easily by your own. This format ist supported by most
of the video player software. For every indicated subtitle line a time
specification is needed in the following format:

h:m:s.msec  example: 00:00:20.396 (time specification 0 hours, 0 minutes,
20.396 seconds)

Milliseconds need to be indicated to the 3rd position after decimal point.

To consider

The separators of the time specification need to be double point and point (as
the example). Commas are not allowed

Inside the document, the first line needs to be WEBVTT.

 **Adding subtitles**

  1. To add subtitles to a video 
  2. navigate to the tab "Subtitle configuration" and 
  3. click the button "Add subtitle".
  4. In the new window chose the language in which you want upload the subtitles and 
  5. select the corresponding file.
  6. Click "Upload".

Already created subtitles are listed in the table and can be deleted there as
well.

 **Displaying subtitles**

By default the videos in OpenOlat are played without subtitles. As soon as
subtitles are available, the following icon will be shown in the video player:
![](../../download/thumbnails/590039/closed_caption_64_0_434343_none%EF%B9%96version=1&modificationDate=1471940738000&api=v2.png).
CC stands for the american expression "[Closed
captions](https://en.wikipedia.org/wiki/Closed_captioning)" (Wikipedia), and
means that subtitles are invisible until they get activated by the user. In
OpenOlat it looks like the following:

![](../../download/attachments/26874220/video_subtitle.png)

As soon as you move the cursor over the icon the list with the existing
subtitles expands. The current selection is dyed.

####  Video quality

In the tab "Video quality" the resolution of the video is shown. As soon as a
video is uploaded, videos in different resolutions will be created. This
process can take a long time. The available resolutions are dependent on the
settings in the administration area. Pending videos can be transcoded and not
used resolutions can be deleted. In the video player the desired resolution
can be chosen by the "Source Chooser".

![](../../download/attachments/590936/videoquality_EN.png)

![](../../download/attachments/590936/resolution_EN.png)

For videos uploaded to OpenOlat there is another tab "Video qualities"
available. For videos added via "Import URL", the settings cannot be made.

### Download

In the Download tab you can set whether the users are allowed to download the
video or not.

## Embed videos in courses

The course element "[Video](Knowledge+Transfer.html#KnowledgeTransfer-
_video_kursbausteinVideoCourseElement:Video)" allows the author to embed
videos directly into a course. The video is either chosen out of the list of
available videos in the authoring, or directly imported. Compared to videos
embedded as a course element "Single page" - videos embedded like this allow:

  * playback with subtitles
  * playback in different resolutions (especially relevant for mobile, or without WiFi-access) 
  * comments
  * assessment
  * landing picture by desire
  * Combination with certain completion criteria in learning path courses

##  Video Collection

Use the "Video Collection" page to browse through all videos that are
available in your instance. In order for a video to be displayed in the "Video
Collection", the publication status "Published" must be set. In combination
with the access setting "Open" it will automatically be accessible for all
registered users. The description of the info page is automatically displayed
in the individual view of a video, as well as the rating and comment function.
If you miss a video, check the settings in the video settings under "Access
configuration".

  

If you cannot find the "Video Collection" entry in the main navigation of your
OpenOlat instance, either the administrator has hidden it or you do not have
the required rights.

