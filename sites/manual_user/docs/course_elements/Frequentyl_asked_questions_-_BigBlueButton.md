# Frequently asked questions - BigBlueButton

!!! note "Open Source Solution BigBlueButton"

    BigBlueButton is an open source solution for virtual conference, meeting and classroom scenarios. The official documentation and help can be found at the links below. The compilation of frequently asked questions (FAQ) on this page are not exhaustive and refer to the use of BigBlueButton in combination with OpenOlat.
    
    * [Help Videos from BigBlueButton](https://bigbluebutton.org/html5/){target=_blank}
    * [FAQ BigBlueButton](https://docs.bigbluebutton.org/support/faq.html){target=_blank}
    * [More FAQ BigBlueButton](https://support.blindsidenetworks.com/hc/en-us/categories/360000379651-BigBlueButton-HTML5){target=_blank}


## :material-devices: Devices, Internet Browsers & Error Messages

**Which browsers are supported by BigBlueButton?**

BigBlueButton is a browser-based software and can be used without any additional plugins or software installations. BigBlueButton's technology requires that a modern and up-to-date browser is used.

_For participants:_ We recommend the use of Google Chrome. For participants, a current version of Firefox or Microsoft Edge (with Chromium) is also suitable. On mobile devices, participation is also possible with Safari (iOS) and Chrome (Android).

_For presenters/lecturers:_ We recommend the use of Google Chrome - only with Google Chrome all functionalities such as screensharing are optimally supported. Other browsers can be used - however, it is recommended to check your own setup before the first presentation/class.

**Which devices can be used to participate in BigBlueButton meetings?**

All devices that meet the browser requirements (see above) are suitable. Mobile devices such as smartphones and tablets are also supported - sometimes they do not offer the full range of functions (e.g. for moderators/lecturers).

**Can I use the BigBlueButton whiteboard with my tablet (e.g. iPad)?**

Yes - this setup is possible. For this, the meeting should have an external guest link. To do this, log in to the meeting with your normal supervisor account and additionally log in with the tablet via the guest link. We recommend a username like "Peter Meier - iPad". Via right click on the tablet user you can upgrade him to presenter and afterwards you can control the presentation on the tablet and use the whiteboard function (Tip: You can upload the presentation with the normal user at the beginning).

**One of the following error messages is displayed:**

Error code| Error description / reason  
---|---  
1020| Video error (see "I can't activate my camera" below)  
1002| Your firewall is blocking access or the BigBlueButton server is unreachable  
1001| The Internet connection has been lost - reconnect to the Internet  
1003| The selected internet browser is not supported (you may be using an outdated version of the browser)  
1005| The session setup (joining the meeting) was successful but ends suddenly - restart your browser and your device if necessary  
1006| Session timeout (no response) - so far only occurred occasionally with Firefox  
1007| Your firewall blocks access or the BigBlueButton server is not reachable  
  

**Which ports are used by BigBlueButton?**  

If you are unable to access the BigBlueButton, this may be due to a setting in your firewall. You can test this by accessing the online meeting with your device from another network (guest WLAN etc.) or via hotspot using your mobile phone. If this works, you should check the following ports/shares on your firewall (in a business environment by your IT service/support):

Ports| Description  
---|---  
80 (TCP/IP)| HTTP  
443 (TCP/IP) | HTTPS  
16384-32768 (UDP) | Encrypted WebRTC audio, video and screensharing  

## :material-cast-audio: Audio problems

**Why can't I hear anything in the BigBlueButton meeting?**

The following options are available to troubleshoot the problem:

  * Make sure you can hear other audio sources (ex. YouTube video).
  * Do you have another conference tool open like Microsoft Teams, Skype, other browser windows with similar features, Wire etc.?
  * Click on the audio icon in BigBlueButton and connect again
  * Select an alternative audio source in your control panel or use a different headset
  * Restart your internet browser or use an alternative browser
  * Restart your PC or notebook

**Other participants do not hear me well or cannot understand me. What is the reason?**

  * Make sure your headset is plugged in correctly.
  * When you entered the meeting, did you allow access to your microphone in your browser (when using BigBlueButton for the first time)?
  * Click on the audio icon in BigBlueButton and reconnect and check your audio in the Echo Test.
  * Is the correct microphone enabled in your system settings (e.g. is the notebook entered instead of the headset?)
  * Is the volume setting in the system settings correct and configured high enough?
  * Do you have the possibility to use a network cable instead of WLAN or a hotspot via cell phone?


## :material-video-box: Video problems

**I cannot activate my camera. What is the reason?**

* In some setups, only moderators are able to activate the camera - but not the participants (but the moderator can temporarily upgrade you to co-moderator).
* When entering a BigBlueButton meeting for the first time, you have to allow access to the webcam in your browser (usually there is a camera icon at the top of the address bar - click on it to learn more about access to camera/microphone).
* Do you have another video conferencing tool open like Microsoft Teams, Skype, other browser windows with similar functions, Wire etc.?
* Restart your internet browser or use an alternative browser
* Restart your PC or notebook

  
**The presentation is too small and the videos of the participants and presenters are very large. How can I change this?**

Between the videos and the presentation/screensharing, you can use the mouse to increase and decrease the ratio of the two areas. In addition, the presentation/screensharing can be displayed full screen at any time (click on the icon in the upper right corner of the presentation).


## :material-projector-screen-outline: Presenters/Presenters

**Which files can I show as a presentation via BigBlueButton?**

BigBlueButton supports common office formats (Word, PowerPoint) as well as PDF when uploading. We recommend to use PDF files whenever possible - they provide the best quality for the participants. Other formats will be converted after the upload - this can lead to altered representations. Animations are not supported during upload. If animations are needed, the presentation can alternatively be shared via screensharing or as a Youtube/Vimeo video.  

**How can I share audio files via BigBlueButton?**

BigBlueButton does not support direct playback of audio files.
However, you can check the following variations in your personal setup:

* Playing the audio in combination with a video on Youtube or Vimeo.
* When using Google Chrome on Mac OSX, the audio is also transferred during screensharing
* You make the audio files available for the participants on OpenOlat in a folder

**Can I show videos via screensharing?**

For playing videos, the separate function "Share external video" is suitable - for this you have to provide the video via YouTube or Vimeo in advance.  
In Google Chrome on Mac OSX, the video with audio can also be shown in screensharing.

**Why can't I select a single window when screensharing?**

The dialog to select a specific window/application or a second monitor is only shown in Google Chrome. Screensharing can be partially enabled in other internet browsers, but it directly and exclusively shares the screen with the current BigBlueButton meeting window.

## :material-record: Recordings.

**Which areas are recorded when recording?**

When recording in BigBlueButton, all activities are recorded and are subsequently available in an interactive viewer.  

_The recording includes:_ All audio, all activated cameras, presentations/screensharing, notes on slides (whiteboard activities) common chat.

**From when is the recording available in the OpenOlat course?**

Any recordings will be available in OpenOlat a few minutes after the meeting has concluded/ended. Under "expired online appointments" you can control the publication.