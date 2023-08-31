# Local installation of ffmpeg

When a user makes an audio recording, the audio is saved directly in OpenOlat in the format that the web browser happens to produce.

Not all browsers are able to produce audio files that are fully supported by the audio player of the browser itself and of other browsers. We have found that the **m4a** format with the **aac** codec is fully supported for playback on all browsers. For this reason we convert audio files recorded in OpenOlat to this format.

We use ffmpeg to perfom the conversion from files such as **ogg** to **m4a**.

When using a hosting package of OpenOlat, your installation is managed, and you have to contact your OpenOlat hosting partner to activate the audio conversion using ffmpeg.

When you host OpenOlat yourself, you can set up and use a local installation of ffmpeg.

## Get ffmpeg

You can install ffmpeg on a Ubuntu or Debian server running OpenOlat. As root, execute:

```
apt-get update
apt install ffmpeg
```

You can also download ffmpeg from the supplier of the tool:

[ffmpeg Download](https://ffmpeg.org/download.html)

## Configure local conversion

Open `Administration > Modules > Audio/video recording`. If you host and manage OpenOlat yourself, you can check the box `Enable local audio conversion`.

If OpenOlat can't find ffmpeg in its path, you can try to set the ffmpeg executable in the `olat.local.properties` file:

```
av.ffmpeg.path=/usr/bin/ffmpeg
```

You need to restart the OpenOlat server after making this change to the `olat.local.properties` file.
