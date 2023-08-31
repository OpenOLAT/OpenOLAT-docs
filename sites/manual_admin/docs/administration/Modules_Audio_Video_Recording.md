# Modules: Audio/Video Recording

## Recording configuration

### Enable video recording
  
When you enable the video recording feature, users can record their own video in many places where video is used, such as in tasks or group tasks.

### Enable audio recording

When you enable the audio recording feature, users can record their own audio in many places where audio is used, such as in tasks or group tasks.

### Enable local video conversion

Video files recorded in web browsers are often not in a format that can be used on other browsers. This requires the conversion of videos from the original format to a format that works on all browsers. **mp4** using the **h264** codec for video and the **aac** codec for audio is a format that satisfies this requirement.

It is possible to perform this conversion directly on the server running OpenOlat using the tool **HandBrakeCLI**. You can only enable this option if HandBrakeCLI is installed on the server and available via the default path.

For information on how to install HandBrakeCLI locally, see the chapter [HandBrakeCLI](../installation/handBrakeCli.md).

### Enable local audio conversion

Audio files recorded in web browsers are often not in a format that can be used on other browsers. This requires the conversion of audio files from the original format to a format that works on all browsers. **m4a** using the **aac** codec is a format that satisfies this requirement.

It is possible to perform this conversion directly on the server running OpenOlat using the tool **ffmpeg**. You can only enable this option if ffmpeg is installed on the server and available via the default path.

For information on how to install ffmpeg locally, see the chapter [ffmpeg](../installation/ffmpeg.md).

## Conversion jobs

This section contains audio and video files that are waiting to be converted or that failed to be converted successfully.
