# Using WebDAV {: #using_webdav}

WebDAV stands for "Web-based Distributed Authoring and Versioning" and is an open standard for transferring files over the Internet. OpenOlat supports this protocol and thus enables a simple file transfer from your computer to OpenOlat folders.

!!! info "Advantages of WebDAV"

    Without WebDAV, files can only be uploaded to OpenOlat via conventional upload forms. You either select each file individually or several zipped files. With WebDAV, however, you can conveniently copy several files or complete folder structures from your computer into OpenOlat folders, e.g. into the storage folder of a course.

## WebDAV-compatible OpenOlat folders

Via WebDAV you can access the following OpenOlat folders. The structure is created automatically as soon as the elements are created in OpenOlat:

  * [Personal files](../personal_menu/File_Hub.md#personal_files) of the File Hub (all users)
  * Folders of [groups](../groups/Using_Group_Tools.md)
  * [Storage folders of courses](../learningresources/Storage_folder.md) (course owners only)
  * [Course element "Folder"](../learningresources/Course_Element_Folder.md)
  * [Resource folders](../learningresources/index.md#resource_folder) (owners of the learning resource only)
  * [Course archives](../learningresources/Course_Archiving.md) (authors, learning resource managers and administrators only) [:octicons-tag-16:{ title="from Release 19.0 (OO-7504)" }](https://track.frentix.com/issue/OO-7504)

Who is allowed to upload files via WebDAV in the respective folders depends on the specific configuration.

## Requirements

Microsoft Windows, macOS, iOS, Android and Linux support WebDAV for file transfer via drag & drop by default. Various applications (e.g. Microsoft Office) also offer WebDAV functionality.

To access a folder on OpenOlat via WebDAV, you need:

  * WebDAV link: You find this link below WebDAV-compatible folders or in the [settings](../personal_menu/Settings.md#tab_webdav) of your personal menu under:<br>`Personal menu > Settings > Tab "WebDAV"`
  * Your OpenOlat username or, alternatively, the stored email address
  * Your OpenOlat/WebDAV password

If you access OpenOlat via Shibboleth or a cloud login, you can set up your WebDAV password in the settings of your personal menu. To do so, select the link "Settings" and then click the button "Set password" in the tab "WebDAV". If you already have an OpenOlat password, use it for WebDAV access.

## Troubleshooting

In case of problems, go through the following points:

!!! warning "To consider"

    * Depending on the operating system (especially Windows), documents larger than 50 MB cannot be opened via WebDAV
    * The storage volume of the WebDAV folder is limited
    * Check whether the quota has been exceeded (especially if several files were uploaded together)
    * File names are limited to 100 characters
    * File names must not contain several consecutive spaces
    * If folder names contain umlauts, subfolders and the documents they contain may not be displayed

## Setting up the WebDAV connection

??? abstract "Windows 11 (also 7, 8 and 10)"

    1. Start the Windows Explorer.
    2. Right-click "This PC".
    3. Select "Map network drive".
    4. Choose a letter for the drive.
    5. At the bottom, select the option "Connect to a Web site that you can use to store your documents and pictures".
    6. Click "Next".
    7. Select "Choose a custom network location".
    8. Click "Next".
    9. Enter the WebDAV link.
    10. Click "Next".
    11. Now enter your OpenOlat username or the stored email address and your password.
    12. Click "Finish".

??? abstract "Windows Vista"

    1. Click "Computer" in the start menu.
    2. In the following window, click "Map network drive" in the menu bar at the top (under "More commands").
    3. At the bottom, select the option "Connect to a Web site".
    4. Click "Next".
    5. Select "Choose a custom network location".
    6. Click "Next".
    7. Enter the WebDAV link as the Internet or network address.
    8. Click "Next".
    9. Now enter your OpenOlat username or the stored email address and your password.
    10. You can enter a name for the WebDAV connection.
    11. Click "Finish".

??? abstract "Mac"

    1. In the Finder, open the menu "Go" and then "Connect to Server" and enter the WebDAV link there.
    2. Now enter your OpenOlat username or the stored email address and your password.
    3. Click "OK".

??? abstract "Linux"

    There are three options for Linux users:

    1. KDE Plasma: In Dolphin, enter `webdavs://` + WebDAV link in the location bar. You are asked for username and password. If the location bar is not displayed, you can activate it at any time with the F6 key. Example: `webdavs://www.olat.uzh.ch/olat/webdav/`.
    2. Gnome: Enter `davs://` + username or email address + `@` + WebDAV link. Example: `davs://pmuster@www.olat.uzh.ch/olat/webdav/`.
    3. FUSE: WebDAV directories can be mounted directly into the file system (also works on macOS, more on the [FUSE website](http://fuse.sourceforge.net "FUSE website")).

??? abstract "Alternative"

    Besides the methods described under "Setting up the WebDAV connection", a WebDAV client can be used alternatively. Depending on the environment, especially Windows in combination with Citrix, such a client can work more stably than the direct WebDAV connection. Some examples of WebDAV clients:

    * Windows: Cyberduck, WinSCP
    * Mac: Cyberduck, Commander One

## Folder structure

Once you have set up the connection successfully, a directory opens on your computer that contains the following subdirectories:

  * **coursefolders**: Here you have access to the [storage folders](../learningresources/Storage_folder.md) of all courses you own. A WebDAV folder is created automatically for each course. Click the WebDAV folder of a course and you see the files and the structure of the respective storage folder and can upload, delete, modify files, etc. In addition to the files and folders you create, OpenOlat automatically creates further folders depending on the configuration. You can also access these via WebDAV. Only the owners of a course see the storage folder. Coaches and participants only find the folders of the course elements "Folder" and embedded resource folders here, provided the system administration has enabled this access (see [WebDAV (Administration)](../../manual_admin/administration/WebDAV.md)).

    * _other_: This folder only appears if the courses are grouped by semester terms or CPL elements in the system administration. This folder contains all courses that are _not_ assigned to a term or element.
    * _finished_: This folder only appears if the courses are not grouped. This folder contains all courses with the status "Finished".

  * **groupfolders**: Here you find all groups you are a member of and whose folders you have access to.
  * **home**: Your personal files with the subfolders "private" and "public".
  * **sharedfolders**: All resource folders you own or have access to based on a membership. Owners and coaches receive read and write permissions, participants read permissions only.
  * **mycoursearchives**: All [course archives](../learningresources/Course_Archiving.md) you have created. This folder only appears for authors, learning resource managers and administrators.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Personal tools: File Hub >](../personal_menu/File_Hub.md)<br>
[Using Group Tools >](../groups/Using_Group_Tools.md)<br>
[Storage folder >](../learningresources/Storage_folder.md)<br>
[Course Element "Folder" >](../learningresources/Course_Element_Folder.md)<br>
[Various Types of Learning Resources >](../learningresources/index.md)<br>
[Course administration - Archiving & Reports >](../learningresources/Course_Archiving.md)<br>
[Personal Configuration: Settings >](../personal_menu/Settings.md)<br>
[FUSE website >](http://fuse.sourceforge.net)<br>
[WebDAV (Administration) >](../../manual_admin/administration/WebDAV.md)

[To the top of the page ^](#using_webdav)
