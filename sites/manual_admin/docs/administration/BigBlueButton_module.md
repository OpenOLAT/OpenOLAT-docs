#  [BigBlueButton module](BigBlueButton+module.html)

In the administration the virtual classroom BigBlueButton can be activated.
This article describes the configuration of multiple BigBlueButton servers,
load balancing and setting up system-wide room templates.

Instructions on how to configure individual online dates are described in the
chapter [Course Element BigBlueButton](Course+element+BigBlueButton.html).

 **Table of contents**

  * 1 BigBlueButton module 
    * 1.1Server
    * 1.2Configuration
    * 1.3Add BigBlueButton-Server
    * 1.4Load balancing
    * 1.5Room templates
    * 1.6Calendar

In the administration the tabs Server, Room templates, Online appointments and
Calendar are available.

## Server

The available BigBlueButton servers per OpenOlat instance are displayed here.

 Configuration

## Configuration

  *  **Module "BigBlueButton":**  Activation of the functionality

  *  **Activate for courses/groups:**  Activate functionality for courses/groups

  *  **Online-Meetings without date:**  Additional option to activate "permanent room reservations" in addition to online-meetings

  *  **Servers:**  In the configuration the available BigBlueButton servers per OpenOlat instance are entered.

Online-Meetings without date

Online-Meetings without a date (permanent room reservations) are not visible
in the calendar and count as booked at all times towards the limits of the
room template.

  

![](assets/configuration-overview.png)

## Add BigBlueButton-Server

  *  **BigBlueButton API URL** : URL of the BBB-Server

  *  **Shared secret** : API Key of the BBB-Server

  *  **Capacity factor** : Server weighting in load balancing

  *  **Activate server** : Server is available for load balancing

![](assets/add-server.png)

## Load balancing

The goal is to distribute the generated load of simultaneous online meetings
to the available BigBlueButton server by considering a set of performance
parameters (such as number of videos and number of participants in the
meetings). OpenOlat has an integrated load-balancing for this purpose. At the
initial start of the online-meeting (depending on the configuration by the
moderator or the first participant) the server with the lowest load is
selected for the meeting. The load is calculated from the different
measurement factors and weights the result with the capacity factor. Using the
filter above the list, the server key figures can be displayed over the entire
BBB server or only the sessions of the current OpenOlat server.

Capacity factor

The capacity factor is recorded with a value between 1 and 100 per server. The
calculated number of users* on the server is multiplied by the capacity
factor. In this way, a server with stronger performance (RAM/CPU/disk) adapts
to a weaker one.  
  
 _*  Weighting when counting users from high to low: video users, audio users,
viewer_

  

![](assets/image2020-4-14_14-21-13.png)

## Room templates

The room templates are available for selection when creating a new online-
meeting. Templates control the following characteristics:

  * The available functions and standard settings in the online-meeting

  * The number of possible simultaneous users per room

  * Limits regarding duration and number of online rooms available

 **Configuration of a room template**

  *  **Room name:** Name of the room template

  *  **Description:**  Description of the room template (e.g. learning scenario, field of application)

  *  **Number of participants:**  Maximum number of participants

  *  **Duration (minutes):**  Maximum length of online-meeting

  *  **Enable room-template  :** Activated room templates are available in courses/groups for new online appointments and can be chosen by course owners

  *  **Number of rooms:**  Maximum number of concurrent rooms of the template

  *  **Open for external users:** A direct link is automatically generated for external users so that they can enter the BigBlueButton room without having to call OpenOlat first. The link is then displayed in the room configuration and can also be changed by the course owner or coach if necessary, as well as passed on to guests.

  *  **Room-template activated for <Role>:** Determines which roles can use the room template for new online-meetings. If the "Group member" option is activated, the template can also be used and further configured in OpenOlat groups.

  

![](assets/bbb_room_template.png)

  

 **Default settings of the room template**

![](assets/edit-room-template-2.png)

 **Default settings for locked participants**

![](assets/edit-room-template-3.png)

Online-Meetings

Overview of configured online-meetings with the possibility to switch directly
to the course/group (context) and/or delete this online-meeting.

![](assets/bbb_administration_online-meetings.png)

## Calendar

Calendar overview of configured online-meetings to check times with high
occupancy and graphically display overlaps. This gives you a quick overview of
the scheduled synchronous meetings of the entire OpenOlat instance and, if
necessary, you can quickly select an alternative date.

![](assets/bbb_administration_calendar.png)

  

