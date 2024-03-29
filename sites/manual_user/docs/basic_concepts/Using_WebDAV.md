# Using WebDAV

WebDAV means "Web-based Distributed Authoring and Versioning"; it is an open
standard to transfer files online. OpenOlat supports this protocol and thus
helps you to easily transfer files from your computer to OpenOlat folders.

!!! info "Advantages of WebDAV"

    Without WebDAV it is only possible to upload files in OpenOlat by means of
    ordinary upload forms. You can either select each single file separately or
    several zipped files at once. With WebDAV you can use "Drag&Drop" on your
    computer (e.g. via the Windows Explorer) to copy single files as well as
    entire directories into OpenOlat folders.

## WebDAV Compatible OpenOlat Folders

Via WebDAV you can access the following OpenOlat folders. Thereby the structure of how the elements are generated in OpenOlat is taken automatically:

  * [Personal folder](../personal_menu/Personal_folders.md) (every user)  
  * [Folders of groups](../groups/Using_Group_Tools.md)
  * [Folder - course element](../learningresources/Course_Element_Folder.md)
  * [Storage folders](../learningresources/Storage_folder.md) of courses (course owners only)
  * [Resource folders](../learningresources/index.md#resource-folder) (only Learning Resource Owner)

Who is allowed to upload files via WebDAV in the respective folders depends on the respective configuration.

## Requirements

Microsoft Windows, Mac OSX, iOS, Android and Linux usually support WebDAV for
drag&drop file transfer. In addition, several software packages have WebDAV
implemented directly into the software (e.g. Microsoft Office).

In order to get access to a folder in OpenOlat via WebDAV you need:

  * WebDAV link: WebDAV address of OpenOlat server as indicated below WebDAV compatible folders, or in your personal menu under Settings / WebDAV
  * Your OpenOlat username or e-mail adress
  * Your OpenOlat/WebDAV password

If you access OpenOlat via Shibboleth or another Cloud Login you can set your WebDAV password on your homepage, section "Settings." Just select the link "Settings" before
clicking on the button "Set password" in the tab "WebDAV." If you already have an OpenOlat password, you can use this one to access WebDAV.

## Troubleshooting

In case of problems, go through the following points:

!!! warning "To consider"

    * Depending on the operation system (especially Windows) documents bigger than 50 MB cannot be opened with WebDAV
    * The storage volume of WebDAV-Folders is limited
    * Check if the quota has been exceeded (especially if several files have been uploaded together)
    * File names are limited to 100 characters
    * File names may not include several spaces after each other
    * If mutated vowels are used in folder names, subfolders and contained documents may not be displayed

## WebDAV Connection Setup

??? abstract "Windows 10 (also 7 + 8)"

    1. Start the Windows Explorer
    2. Click on "Computer" in the start menu.
    3. In the new window click on "Connect to network drive" in the upper menu bar. Click on the double arrow in the menu bar if "Connect to network drive" is not visible, then click on it.
    4. Choose a drive letter for the connection.
    5. At the bottom select the option "Establish connection with a website."
    6. Click on "Next."
    7. Choose the option "Select user-defined network resource."
    8. Click on "Next."
    9. Indicate your WebDAV link as Internet or network address.
    10. Click on "Next."
    11. Now provide your OpenOlat username or the stored email address and password.
    12. Click on "Finish."

??? abstract "Windows Vista"

    1. Click on "Computer" in the start menu.
    2. Click on "Assign network drive" in the menu bar (via "Further commands").
    3. Select at the bottom the option "Connecting to website."
    4. Click on "Next."
    5. Check the option "Select user defined network source."
    6. Click on "Next."
    7. Indicate your WebDAV link as internet or network address.
    8. Click on "Next."
    9. Indicate your OpenOlat username or the stored email address and password.
    10. You can then insert a name for your WebDAV connection.
    11. Click on "Finish."

??? abstract "Mac"

    1. Open the menu "Go to" in the Finder and then "Connecting to server..." Indicate your WebDAV link.
    2. Provide your OpenOlat username or the stored email address and password.
    3. Click on "OK."

??? abstract "Linux"

    There are three possibilities for Linux users:

    1. KDE Plasma: in Dolphin insert in the path webdavs:// + WebDAV-link. You will be asked for username and password. If the path is not shown, it can be activated with F6 any time. Example: <webdavs://www.olat.uzh.ch/olat/webdav/>.
    2. Gnome: `davs:// + username or email address + @` \+ WebDAV link. Example: `davs://jdoe@www.olat.uzh.ch/olat/webdav/`.
    3. FUSE: WebDAV directories can be mounted directly into the file system (also compatible to OSX; for more information please go to the [FUSE website](http://fuse.sourceforge.net "FUSE website").

??? abstract "Alternative"

    Beside the described methods in "WebDAV Connection Setup" a WebDAV client can
    be used alternatively. Depending on the setting, especially for Windows in
    connection to Citrix, such a client can be work more stable than the direct
    WebDAV connection. In the following some examples for WebDAV clients:

      * Windows: Cyberduck, WinSCP
      * Mac: Cyberduck, Commander One

## Folder Structure

If you have setup the connection successfully a directory will be opened on your computer containing the following sub-directories:

  *  **coursefolders**: Here you have access to the [storage folders](../learningresources/Storage_folder.md) of all courses you own or are a member of. A WebDAV folder is automatically created for each course. Click on the WebDAV folder of a course and you will see the files and the structure of the respective storage folder and you can upload, delete, modify files, etc. In addition to the files and folders you create, OpenOlat automatically creates specific folders depending on them. You can also access these via WebDAV. The storage folder is most and for all only visible to users holding author rights. All other users will find here course folders.
    * _other_: This folder only appears if in the administration semester terms are activated. In this folder all courses which are added to a term can be found. 
    * _finished_: This folder only appears if in the administration semester terms are not activated. In this folder all courses can be found, which have been set to finished in the course life-cycle. These are the courses which appear in the menu Courses in the tab "Finished".

  *  **groupfolders** : all groups you are enrolled in and have access to corresponding folders.
  *  **home** : both of your personal folders (along with the sub-folders "private" and "public").
  *  **sharedfolders** : All resource folders you own or have otherwise access to due to membership rights. Owners and coaches may read and write, and participants may read but not write.
