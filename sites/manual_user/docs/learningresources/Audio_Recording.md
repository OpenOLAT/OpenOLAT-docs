# Audio recording

## Requirements {: #requirements}

* If audio is to be recorded in OpenOlat, a microphone must first be available. It must always be activated in the device.

* The microphone must be enabled for OpenOlat so that it can also be used for recordings in OpenOlat.

* *Only macOS:* In browsers other than Safari, the general permission to use the microphone must be granted. Set this permission on the Mac for the browsers you use for OpenOlat:<br>
  `System Settings > Privacy & Security > Microphone`

* On the other side, the **possibility to record audio** must have been activated in OpenOlat by the administrator in the system administration:<br>
  `Administration > Modules > Audio/video recording`

## Where can audios be recorded in OpenOlat? :octicons-tag-16:{ title="from Release 17.1 (OO-6327)" } {: #audios_recording}

### Recordings in the Media Center

Open the **personal menu** by clicking on the small image or the triangle at the top right.
Open the Media Center there.

Among the possibilities to add new media files, there is also the possibility to **"Record audio"**.

![Add media file menu in the Media Center with the highlighted entry Record audio](assets/audio_recording_mediacenter_v3_de.png){ class="shadow lightbox" }

### Recordings in the course element page

Audio can also be inserted within a layout element in the course element "Page".

![Add content menu in the course element Page with the highlighted element Audio](assets/audio_recording_page_v3_de.png){ class="shadow lightbox" }

Once you have decided on this, a pop-up appears to select an existing audio. The pop-up also contains a button for recording your own audio.

![Select audio dialog with the highlighted Record audio button](assets/audio_recording_page_add_v3_de.png){ class="shadow lightbox" }

### Recordings in the course element "HTML page"

The HTML editor (Tiny) used in OpenOlat is also used for inserting and recording audio. The option to record audio is located under the tools that are also used to insert existing media.

![HTML editor with the highlighted microphone icon for recording an audio](assets/audio_recording_html_editor_v3_de.png){ class="shadow lightbox" }

!!! note "Note"

    In principle, audio recordings are possible in the HTML editor, but in some places not all editing options are offered when the editor is called up for various reasons. It is therefore possible that the option to record audio is offered when the HTML editor is called up, but not when it is called up from another location.

### Recordings in the course element "Task"

The option to record audio in a task is embedded in the workflow. You will find the recording function in the step where the audio is to be inserted as a task or sample solution.

![Task tab in the course element Task with the highlighted entry Record audio](assets/audio_recording_task_create_task_v3_de.png){ class="shadow lightbox" }

![Sample solution tab in the course element Task with the highlighted entry Record audio](assets/audio_recording_task_create_solution_v3_de.png){ class="shadow lightbox" }

For audio recordings that are recorded in the course element "Task", there is currently no option for saving and linking in the Media Center.

### Recordings in the course element "Group task"

The audio recording in the course element "Group task" works in the same way as in the course element "Task".

## Where are the audio recordings saved? {: #save_audio_recordings}

**Audio recorded within a course element** is also saved with this course element.
The recordings are not listed in the author area, storage folder or in the Media Center (exception: course element page).

![Manage tab in the course element Task with the recorded audio file audio01.m4a in the list](assets/audio_recording_task_storage_v3_de.png){ class="shadow lightbox" }

However, if the **audio recording in the Media Center** is started, the audio is also saved in the Media Center.

## In what format and quality are recordings saved? {: #audio_format_quality}

Audio recordings made in OpenOlat are always saved as **m4a files**. This is due to the fact that only the m4a format is supported by all browsers.

The recording quality is preset (mono, 44 kHz).

Administrators can activate local audio conversion under<br>
  `Administration > Modules > Audio/video recording > Tab Recording configuration`<br>
(See also the [article in the administration manual](../../manual_admin/administration/Modules_Audio_Video_Recording.md#enable-audio-recording).)

## How much storage space is available for my audios? {: #audio_storage}

E.g.: Media Center<br>
In the lower left corner, you can see the available storage space (for the entire Media Center) and how much of it is already occupied. The available space can be determined by the administrators.

![Display of occupied and available storage space in the lower left corner of the Media Center](assets/audio_recording_space_v3_de.png){ class="shadow lightbox" }

## How can audio recordings be exported? {: #audio_export}

### Download from the course element Task and Group task

Both audio recordings from the task and audio recordings in the sample solution can be downloaded directly in the course element. To do this, use the option under the three dots at the end of a line.

![Steps for downloading an audio recording in the Manage tab of the course element Task via the menu with the 3 dots](assets/audio_recording_task_download_v3_de.png){ class="shadow lightbox" }

### Download from Media Center

Select and open the desired audio in the Media Center. Under the button with the 3 dots you will find the option to download.

![Detail view of an audio file in the Media Center with the highlighted menu item Download](assets/audio_recording_mediacenter_download_v3_de.png){ class="shadow lightbox" }

!!! note "Note"

    An audio that was recorded within a course element is **not** stored in the course storage folder.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Module Audio/Video Recording](../../manual_admin/administration/Modules_Audio_Video_Recording.md)

[To the top of the page ^](#audio-recording)