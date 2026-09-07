# Video Recording

## Requirements

* If videos are to be recorded in OpenOlat, a camera must first be available. It must be activated on the device.

* The camera must be enabled for OpenOlat so that it can also be used for recordings in OpenOlat.

* *Only macOS:* In browsers other than Safari, the general permission to use the microphone and the camera must be granted. Set these permissions on the Mac for the browsers you use for OpenOlat:<br>
  `System Settings > Privacy & Security > Microphone` and<br>
  `System Settings > Privacy & Security > Camera`

* On the other side, the **option for video recordings** must be activated in OpenOlat by the administrator in the system administration:<br>
`Administration > Modules > Audio/video recording`

* The settings for the **transcoding** of the recordings (settings for file size and image quality) are also made in the system administration under:<br>
`Administration > Modules > Audio/video recording`


## Where can videos be recorded in OpenOlat?

### Recording in the Media Center

Open the **personal menu** by clicking on the small picture or triangle at the top right.
Then open the Media Center.

The options for adding new media files also include **"Record video"**.

![Entry Record video in the menu of the Add media file button, in the Media Center](assets/video_recording_mediacenter_v1_de.png){ class=" shadow lightbox" }


### Recording in the course element Page

A video can also be inserted within a layout element in the course element Page.

![Content type Video in the Add content selection of a layout element, in the course element Page](assets/video_recording_page_v1_de.png){ class=" shadow lightbox" }

Once you have decided on this, a pop-up appears to select an existing video. The pop-up also contains a button for recording your own video.

![Buttons Record video and Add video in the Select video dialog, in the course element Page](assets/video_recording_page_add_v1_de.png){ class=" shadow lightbox" }


### Recording in the course element HTML page

The HTML editor (Tiny) used in OpenOlat is also used for inserting and recording videos. The option to record a video is located under the tools that are also used to insert existing media.

![Icon for inserting media in the toolbar of the HTML editor, in the course element HTML page](assets/video_recording_html_editor_v1_de.png){ class=" shadow lightbox" }


!!! note "Note"

    In principle, video recordings are possible in the HTML editor, but in some places not all editing options are offered when the editor is called up for various reasons. It is therefore possible that the option to record a video is offered when the HTML editor is called up, but not when it is called up from another location.



### Recording in the course element Task

The option to record videos in a task is embedded in the workflow. You will find the recording function in the step where the video is to be inserted as an assignment or sample solution.

![Entry Record video in the menu of the Create assignment button, tab Assignment of the course element Task in the course editor](assets/video_recording_task_create_task_v1_de.png){ class=" shadow lightbox" }

![Entry Record video in the menu of the Create sample solution button, tab Sample solution of the course element Task in the course editor](assets/video_recording_task_create_solution_v1_de.png){ class=" shadow lightbox" }

For video recordings that are recorded in the course element "Task", there is currently no option for saving and linking in the Media Center.


### Recording in the course element Group task

The video recording in the "Group task" course element works in the same way as in the "Task" course element.



## Where are the video recordings stored?

**Videos recorded within a course element** are also saved for this course element.
The recordings are not listed in the authoring area, storage folder or in the Media Center (exception: course element Page).

![Recorded mp4 file in the File column of the assignment list, tab Manage in the course element Task](assets/video_recording_task_storage_v1_de.png){ class=" shadow lightbox" }

However, if the **video recording is started in the Media Center**, the video is also saved in the Media Center.


## In what format and quality are recordings saved?

Video recordings made in OpenOlat are always saved as **mp4 files**. This is due to the fact that only the mp4 format is supported by all browsers.

For pure audio it is the m4a format.

The **image size** in which a video is recorded depends primarily on the browser and camera. The size is displayed in the top left of the recording window.

In order to control the memory consumption by videos of the participants, the **resolution** for the video recordings can only be set by the course owners in the course element "Task", for example. The participants then make all recordings in this standard quality.

!!! tip "Recommendation"

    If possible, use a medium resolution.<br>
    A large resolution generates significantly larger files and consumes corresponding storage space.
    Although the file size is optimized at a low resolution, the quality of the image may be insufficient. Always take into account the motif you have captured. A higher resolution is justified if details need to be reproduced sharply. With large uniform areas in the image, a low resolution hardly reduces the quality at all.


![Selection of the recording quality with the levels Lower, Standard and Higher quality, Record video window with the image size 640 x 480 at the top left](assets/video_recording_quality_v1_en.png){ class=" shadow lightbox" }

After a video has been recorded, OpenOlat adjusts the image size, resolution and quality to the preset standards. This **transcoding** is carried out automatically by OpenOlat and the videos are then saved according to the default settings. This ensures that the videos are displayed in a suitable aspect ratio and that the file size is optimized for storage.


## How much storage space is available for my videos?

Example: Media Center<br>
In the bottom left-hand corner, you can see the available storage space (for the entire Media Center) and how much of it is already occupied. The available space can be determined by the administrators.

![Display 0 B of 102.4 MB used in the bottom left-hand corner, in the Media Center](assets/video_recording_space_v1_de.png){ class=" shadow lightbox" }


## How can video recordings be exported?


### Download from the course element Task and Group task

Both video recordings from the assignment and video recordings in the sample solution can be downloaded directly in the course element. To do this, use the option under the 3 dots at the end of a line.

![Entry Download file in the three-dot menu of an assignment row, tab Manage in the course element Task](assets/video_recording_task_download_v1_de.png){ class=" shadow lightbox" }


### Download from the Media Center

Select and open the desired video in the Media Center. Under the button with the 3 dots you will find the option to download.

![Entry Download in the three-dot menu of the detail view of a video, in the Media Center](assets/video_recording_mediacenter_download_v1_de.png){ class=" shadow lightbox" }

!!! info "Important"

    A video that was recorded within a course element is **not** stored in the storage folder of the course.
