# Videos in course element "HTML-Page"

![video.png](assets/add_video.png)

Videos that are integrated into the course element "HTML page " are **directly integrated** videos.<br> (See [Videos: Overview](Video.md))

These videos can be **uploaded** into the OpenOlat database or function as **links**, e.g. to YouTube videos.<br>
(Videos in HTML pages are not video learning resources, i.e. they are without annotations, quizzes, etc.)

The directly integrated videos in the course element "HTML page" are **stored in the course storage folder**. From there, they are linked to the course element. Videos embedded in this way are only available in the respective course.


## Display of videos in an HTML page

The tool uses the **Media Player** integrated in OpenOlat for the display, which has several advantages.

1. The player recognizes the format itself as long as the video and audio data are encoded correctly.
2. The player recognizes whether a user is accessing the video with an HTML5-capable and codec-compatible mobile browser. In this case, the films are provided with an HTML5 tag and can also be displayed on an iPad or similar without any problems.

In addition to mp4, OpenOlat also supports HTML5 videos that have been integrated into an HTML page with external tools. In this case, you as the author must ensure that different alternative video formats have been specified in the HTML tags (e.g. m4v and ogg) and that these are also stored in different resolutions in OpenOlat.

In this case, OpenOlat supports pseudo-streaming by means of progressive download or range requests.


## Add / edit videos

The "HTML page" course element provides you with an HTML editor that you can use to integrate videos into an HTML page. In the "Page content" tab, you can open the editor and access the "Add / edit video" button.

![video_button.png](assets/video_button.png){ class=" shadow lightbox" }  

!!! tip "Hint"

    You can add a thumbnail to your media file.
    (Upload of an image under "Preview".)

Below you will find the most important information on using the TinyMCE plugin "Add / edit video" used in HTML pages (Supports FLV, MP4 coded with h264, AAC).


### Recommended format

Below, you will find the most important information on using the TinyMCE plugin "Add / edit video" used in HTML pages. Current versions of Firefox, Chrome and Safari can play such videos.

The following options are available to you:

![video_typen.png](assets/Video_Audio_Typen_DE.png){ class=" shadow lightbox" }

| Option |  Description  |
---|---  
Video | Integration of a video with specific coding.  
Music | Integration of an audio file without video.  
YouTube / Vimeo / Nanoo.tv | Integration of a YouTube / Vimeo / Nanoo.tv - video 
http | Streaming with Flash file of a webserver.  
rtmp | Streaming with Flash file of a special streaming server.

#### Video (.FLV, .F4V, .MP4 and .M4V - h264 coded, .AAC as well as .M4A)

This setting is best suited for the integration of videos on OpenOlat. The following labels are suitable as container formats, i.e. the formats that can be uploaded:

| Format container | Name of the container | Description  |
| ---|---|---  |
| .FLV | Flash container | Flash videos with video and audio, defined by Adobe (Attention: Flash player needs to be activated)  
  .F4V | | No container, but pure video format without audio, defined by Adobe  
  .MP4| MPEG-4|MP4 Video- and audio format, defined by the MPEG compound, various Codecs  
  .M4V|MPEG-4|MP4 Video format with H.264 video codec and MP3 or AAC audio codec; format for iTunes  

  You can either enter the link to the video directly in the address field or upload the file accordingly.

  !!! tip "Hint"

    To ensure optimum compatibility, an MPEG-4 container with H.264 encoding for video and AAC or MP3 encoding for audio should be used.

    This means that .mp4 or .m4v are available as file extensions, although .m4v cannot be played by all devices.

    Flash movies are not recommended, as they cannot be played on many mobile devices such as the iPad.



#### YouTube

YouTube videos are linked directly, i.e. the selection box for uploading a file is not required here.

![einbinden_youtube.png](assets/youtube_embed_DE.png){ class=" shadow lightbox" } 

Use as "address" a direct link to the video, available under the link "**Share**".

![teilen_youtube.png](assets/youtube_share.png){ class=" shadow lightbox" } 

#### Vimeo

Vimeo videos are also linked directly in OpenOlat. Enter the link of the desired video under "Address".

![einbinden_vimeo.png](assets/vimeo_embed_DE.png){ class=" shadow lightbox" } 

You will find a direct link to the Vimeo video under the link "**Share**".

![teilen_vimeo.png](assets/vimeo_share_DE.png){ class=" shadow lightbox" }

#### Nanoo.tv

Videos from the platform [Nanoo.tv](https://portal.nanoo.tv/) can be linked directly. A Nanoo.tv account is required to use and view the videos.

![nanootv.png](assets/Nanoo_tv_DE.png){ class=" shadow lightbox" } 

The URL can be used to control - independently of the browser - whether the video starts automatically or not. To do this, the URL behind /link/ must be adapted accordingly.

* start automatically with "n": https://www.nanoo.tv/link/ **n** /sdxpLoaC
* start manually with "v": https://www.nanoo.tv/link/ **v** /sdxpLoaC

The settings in the "Advanced" tab do not work here.

##### http (pseudo) Streaming server (only .flv)

This function can be used to integrate **Flash movies** in **.flv** format. If the films are exported correctly at the point of origin, they will contain an index. With the help of this table of contents, you can also quickly jump to any point within the movie; the movie does not have to be loaded completely first. This is not a real streaming, for this a corresponding streaming software must also be installed on the server.

The address of the server must be entered in the "Streaming server" field. The address of the actual movie is entered under "Address".

!!! warning "Attention"

    As the content cannot be viewed on the iPad and most other mobile devices with this variant of embedding, this procedure is **not recommended**.

#### rtmp Streaming server

A Flash streaming server can be used with this function. A special protocol is used for this: RTMP - Real Time Messaging Protocol. Various products can be used as streaming servers, e.g. the Akamai network.

This protocol developed by Adobe enables the video to be transferred from the server to the Flash Player. However, this variant often causes problems with port settings and firewalls.

!!! warning "Attention"

    As the content cannot be viewed on the iPad and most other mobile devices with this variant of embedding, this procedure is **not recommended**.

    As Flash is no longer supported by most browsers, or only to a very limited extent, the use of Flash-based videos should generally be avoided.