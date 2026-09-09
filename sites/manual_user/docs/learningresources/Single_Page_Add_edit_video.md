# Single Page: Add / edit video


Another way to embed videos in OpenOlat courses is to use the "**Single
Page**" course element.

In the course element "Single Page", an editor is available that you can
also use to embed videos in an HTML page. In the tab "Page content", you can
open the editor and access the "Add / edit video" button.


For playback, the tool uses the media player integrated into OpenOlat, which
has several advantages.
1. The player detects the format itself, as long as the video and audio data
are encoded correctly.
1. The player detects whether users access the video with an HTML5-capable
and codec-compatible mobile browser. If so, the movies receive an HTML5 tag
and can be viewed without difficulty on an iPad or similar devices.

!!! tip "Tip"

    You can also add a start image (preview) to your media file.

Below you will find the most important information on using the "Add / edit
video" TinyMCE plugin used in single pages (Supports FLV, MP4 coded with
h264, AAC).

## Recommended format

In practice, the **mp4** (or MPEG-4) container with the H.264 video codec for
video and the **mp3** audio codec for audio has become established. Current
versions of Firefox, Chrome and Safari can play such videos.



These are the options available to you:

| Option | Description |
|---|---|
| Video | Embed a video with specific encoding. |
| Sound | Embed an audio file without video. |
| YouTube / Vimeo / Nanoo.tv | Embed a YouTube, Vimeo or Nanoo.tv video. |
| http | Streaming with a flash file from a web server. |
| rtmp | Streaming with a flash file from a specific streaming server. |

### Video (.FLV, .F4V, .MP4 and .M4V - h264 coded, .AAC and .M4A)

This setting is best suited for integrating videos in OpenOlat. The
following container formats, i.e. the formats that can be uploaded, are
suitable:

| Format container | Container name | Description |
|---|---|---|
| .FLV | Flash container | Flash videos with video and audio, defined by Adobe (Note: Flash Player must be enabled) |
| .F4V | | Not a container, but a pure video format without audio, defined by Adobe |
| .MP4 | MPEG-4 | MP4 video and audio format, defined by the MPEG group, various codecs |
| .M4V | MPEG-4 | MP4 video format with H.264 video codec and MP3 or AAC audio codec; format for iTunes |

You can either enter the link to the video directly in the address field or
upload the file.

!!! tip "Tip"

    To ensure optimum compatibility, use an MPEG-4 container with H.264 encoding for video and AAC or MP3 encoding for audio.

    This gives you the file extensions .mp4 or .m4v, although .m4v cannot be played on all devices.

    Flash movies are not recommended, as they generally cannot be played on many mobile devices such as the iPad.

### Sound (.MP3)

Embedding pure audio files only provides limited functions in the player.
You can start, stop and see a progress bar, but functions such as full
screen are missing.

In the "Address" field, you can either enter a link to an mp3 file or upload
a file to OpenOlat.

!!! info "Important"

    Playback of mp3 audio files works **on all** common browsers without any problem.

### YouTube

YouTube movies are linked directly, i.e. the upload selection box is not
needed here. Videos can be **directly embedded** with this configuration.

Use a direct link to the video as the "Address", available under the
"Share" link.

### Vimeo

Vimeo videos are also linked directly in OpenOlat. Under "Address", enter
the link of the desired video.

You can find a direct link to the Vimeo video under the "**Share**" link.

### Nanoo.tv

Videos from the [Nanoo.tv](https://portal.nanoo.tv/) platform can be linked
directly. A Nanoo.tv account is required to use and display the videos.

The URL can be used - independently of the browser - to control whether the
video starts automatically or not. For this, the URL after /link/ must be
adjusted accordingly.

  * start automatically with "n": https://www.nanoo.tv/link/ **n** /sdxpLoaC
  * start manually with "v": https://www.nanoo.tv/link/ **v** /sdxpLoaC

The settings in the "Advanced" tab do not work here.

#### http (pseudo) streaming server (only .FLV)

This function allows **flash movies** in **.flv** format to be integrated.
If the movies are correctly exported at their origin, they contain an
index. This table of contents allows you to jump quickly to any point
within the movie without the movie having to load completely first. This
is not real streaming, as that would also require appropriate streaming
software to be installed on the server.

Enter the address of the server in the "Streaming server" field. Under
"Address", enter the address of the actual movie.

!!! warning "Attention"

    Since the content of this embedding method cannot be viewed on the iPad and most other mobile devices, this method is **not recommended**.

### rtmp streaming server

This function allows you to use a flash streaming server. It uses a
special protocol: RTMP - Real Time Messaging Protocol. Various products
can be used as streaming servers, e.g. the Akamai network.

This protocol, developed by Adobe, enables the transmission of the video
from the server to the flash player. This variant often causes problems
with port settings and firewalls.

!!! warning "Attention"

    Since the content of this embedding method cannot be viewed on the iPad and most other mobile devices, this method is **not recommended**.

    Since Flash is no longer supported, or only supported to a very limited extent, by most browsers, the use of flash-based videos should generally be avoided.

### HTML5 video

OpenOlat also supports HTML5 videos embedded in an HTML page using external
tools. In this case, you as the author must ensure that the HTML tags
specify different alternative video formats (e.g. m4v and ogg) and, if
applicable, that these are also stored in OpenOlat in different
resolutions.

In this case, OpenOlat supports pseudo-streaming via progressive download
or range requests.
