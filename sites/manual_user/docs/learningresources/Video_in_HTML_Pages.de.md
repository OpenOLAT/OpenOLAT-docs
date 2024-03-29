# Videos im Kursbaustein "HTML-Seite"

![video.png](assets/add_video.png)

Videos, die in den Kursbaustein "HTML-Seite " eingebunden werden, sind **direkt eingebundene** Videos.<br> (Siehe [Übersicht zu Videos](Video.de.md))

Es können in die OpenOlat-Datenbank **hochgeladene** Videos sein oder **Links**, z.B. auf Youtube-Videos.<br> 
(Bei Videos in HTML-Seiten handelt sich also nicht um Video-Lernressourcen, d.h. sie sind ohne Annotationen, Quiz, usw.)

Die direkt eingebundenen Videos im Kursbaustein "HTML-Seite" sind **im Ablageordner des Kurses abgelegt**. Von dort werden sie in den Kursbaustein verlinkt. So eingebettete Videos stehen nur im jeweiligen Kurs zur Verfügung.


##  Anzeige der Videos in einer HTML-Seite

Für die Anzeige greift das Tool auf den in OpenOlat integrierten **Mediaplayer** zurück, was einige Vorteile hat.  

1. Der Player erkennt das Format selbst, solange die Video- und Audio-Daten richtig codiert sind.  
2. Der Player erkennt, ob ein Benutzer mit einem HTML5-fähigen und Codec-kompatiblen Mobile-Browser auf das Video zugreift. In dem Fall werden die Filme mit einem HTML5-Tag versehen und können problemlos auch auf iPad o.ä. angezeigt werden.  

OpenOlat unterstützt neben mp4 auch HTML5-Videos, welche in einer HTML-Seite mit externen Werkzeugen eingebunden wurden. In diesem Fall müssen Sie als Autor:in selbst dafür sorgen, dass in den HTML-Tags verschiedene alternative Videoformate angegeben wurden (z.B. m4v und ogg) und dass diese allenfalls auch in unterschiedlichen Auflösungen in OpenOlat abgelegt werden.

OpenOlat unterstützt in diesem Fall das Pseudo-Streaming mittels Progressive Download bzw. Range-Requests.  



##  Video hinzufügen / editieren

Im Kursbaustein "HTML-Seite" steht Ihnen ein HTML-Editor zur Verfügung, über den Sie auch Videos in eine HTML-Seite einbinden können. Im Tab "Seiteninhalt" können Sie den Editor öffnen und gelangen zum Button "Video hinzufügen / editieren".

![video_button.png](assets/video_button.png){ class=" shadow lightbox" }  

!!! tip "Tipp"

    Sie können Ihrer Mediendatei auch noch ein Startbild hinzufügen.
    (Upload eines Bildes unter "Vorschau".)

Im Folgenden finden Sie die wichtigsten Informationen zur Nutzung des in HTML-Seiten verwendeten TinyMCE Plugins "Video hinzufügen / editieren" (Unterstützt FLV, MP4 mit h264 codiert, AAC).


### Empfohlenes Format

In der Praxis hat sich der **mp4** (oder MPEG-4) Container mit dem H.264 Video-Codec für Video und dem **mp3** Audio-Codec für Audio etabliert. Aktuelle Versionen von Firefox, Chrome und Safari können solche Videos abspielen.

Die folgenden Optionen stehen Ihnen zur Verfügung:

![video_typen.png](assets/Video_Audio_Typen_DE.png){ class=" shadow lightbox" }

| Option |  Beschreibung  |
---|---  
Video | Einbindung eines Videos mit spezifischer Codierung.  
Musik | Einbindung eines Audio-Files ohne Video.  
YouTube / Vimeo / Nanoo.tv | Einbindung eines YouTube / Vimeo / Nanoo.tv - Videos  
http | Streaming mit Flash-Datei von einem Webserver.  
rtmp | Streaming mit Flash-Datei von einem speziellen Streaming-Server.  
  
#### Video (.FLV, .F4V, .MP4 und .M4V - h264 kodiert, .AAC sowie .M4A)

Diese Einstellung eignet sich für die Integration von Videos auf OpenOlat am Besten. Als Container-Formate, d.h. die Formate die hochgeladen werden können, eignen sich die folgenden Kennzeichnungen:

| Format Container | Bezeichnung des Containers | Beschreibung  |
| ---|---|---  |
| .FLV | Flash Container | Flash-Videos mit Video und Audio, von Adobe definiert (Achtung: Flash Player
muss aktiviert sein)  
  .F4V | | Kein Container, sondern reines Video-Format ohne Audio, von Adobe definiert  
  .MP4| MPEG-4|MP4 Video- und Audioformat, von MPEG-Verbund definiert, verschiedene Codecs  
  .M4V|MPEG-4|MP4 Videoformat mit H.264 Videocodec und MP3 oder AAC Audiocodec; Format für iTunes  
  
In das Adressfeld können Sie entweder den Link auf das Video direkt eingeben oder die Datei entsprechend hochladen.

!!! tip "Tipp"

    Um optimale Kompatibilität sicherzustellen sollte ein MPEG-4 Container mit H.264 Kodierung für Video und AAC oder MP3 Kodierung für Audio verwendet werden. 
    
    Als Dateiendung stehen somit .mp4 oder .m4v zur Verfügung, wobei .m4v nicht von allen Geräten abgespielt werden kann. 
    
    Von Flash Filmen wird abgeraten, da diese auf vielen mobilen Geräten wie z.B. das iPad grundsätzlich nicht abspielbar sind.



#### YouTube  

YouTube Videos werden direkt verlinkt, d.h. die Auswahlbox für das Hochladen einer Datei wird hier nicht benötigt. Videos können mit dieser Konfiguration **direkt integriert** werden.

![einbinden_youtube.png](assets/youtube_embed_DE.png){ class=" shadow lightbox" }   

Benutzen Sie als "Adresse" einen direkten Link zu dem Video, erhältlich unter dem Link "**Teilen**".

![teilen_youtube.png](assets/youtube_share.png){ class=" shadow lightbox" } 

#### Vimeo  

Vimeo Videos werden in OpenOlat ebenfalls direkt verlinkt. Unter "Adresse" geben Sie den Link des gewünschten Videos ein.

![einbinden_vimeo.png](assets/vimeo_embed_DE.png){ class=" shadow lightbox" }   

Einen direkten Link zum Vimeo-Video finden Sie unter dem Link "**Share**".  

![teilen_vimeo.png](assets/vimeo_share_DE.png){ class=" shadow lightbox" } 

#### Nanoo.tv

Videos von der Plattform [Nanoo.tv](https://portal.nanoo.tv/) können direkt verlinkt werden. Für die Nutzung und Anzeige der Videos ist ein Nanoo.tv-Account notwendig.

![nanootv.png](assets/Nanoo_tv_DE.png){ class=" shadow lightbox" } 

Über die URL kann - unabhängig vom Browser - gesteuert werden, ob das Video sofort automatisch startet oder nicht. Dafür muss die URL hinter /link/ entsprechend angepasst werden.

  * automatisch starten mit "n": https://www.nanoo.tv/link/ **n** /sdxpLoaC
  * manuell starten mit "v": https://www.nanoo.tv/link/ **v** /sdxpLoaC

Die Einstellungen im Tab "Erweitert" funktionieren hier nicht.

##### http (pseudo) Streamingserver (nur .FLV)

Mit dieser Funktion können **Flash-Filme** im Format **.flv** integriert werden. Wenn die Filme am Ursprungsort richtig exportiert werden, enthalten sie eine Indexierung. Mit Hilfe dieses Inhaltsverzeichnisses kann man auch innerhalb des Films schnell an eine beliebige Stelle springen, der Film muss nicht erst komplett geladen werden. Es handelt sich dabei nicht um ein richtiges Streaming, bei diesem muss auch auf dem Server eine entsprechende Streaming- Software installiert sein muss.

In das Feld "Streamingserver" muss die Adresse des Servers eingegeben werden. Unter "Adresse" wird die Adresse des eigentlichen Films eingegeben.

!!! warning "Achtung"

    Da mit dieser Variante der Einbettung die Inhalte nicht auf dem iPad und den meisten anderen mobilen Geräten angesehen werden können wird dieses Vorgehen **nicht empfohlen**.

#### rtmp Streamingserver

Mit dieser Funktion kann ein Flash Streaming-Server genutzt werden. Dabei wird ein spezielles Protokoll verwendet: RTMP - Real Time Messaging Protocol. Als Streaming-Server können verschiedene Produkte verwendet werden, z.B. das Akamai Netzwerk.

Dieses von Adobe entwickelte Protokoll ermöglicht die Übertragung des Videos vom Server zum Flash Player. Häufig kommt es bei dieser Variante aber zu Problemen mit Port-Einstellungen und Firewalls.

!!! warning "Achtung"

    Da mit dieser Variante der Einbettung die Inhalte nicht auf dem iPad und den meisten anderen mobilen Geräten angesehen werden können wird dieses Vorgehen **nicht empfohlen**.

    Da Flash von den meisten Browsern nicht mehr oder nur sehr eingeschränkt unterstützt wird, sollte generell auf den Einsatz von flashbasierten Videos verzichtet werden.


