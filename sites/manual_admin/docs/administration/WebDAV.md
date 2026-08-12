# WebDAV

## Module configuration

The WebDAV module can be enabled/disabled system wide. You find the settings in the system administration under:<br>
`Administration > Core functions > WebDAV`

The following parameters can be configured:

  *  **WebDAV access**<br>
	Enable or disable the WebDAV access. When enabled, all system users can access
	their OpenOlat folder using WebDAV (recommended).

  *  **Show WebDAV links**<br>
	Decide if the WebDAV URL is displayed in the folder component or not. This is
	independent of the the WebDAV access. When disabled, WebDAV can still be used
	but the WebDAV link must be known by users as it is not displayed in the web
	interface.

  *  **Digest Authentication**
	
	!!! warning "Security note"
		The Digest Authentication method does not use strong encryption and can be cracked with enough computing effort. To meet very high security demands users should always use HTTPS with SSL encryption.

  * **WebDAV Client exclusion**<br>
	Turn exclusion of specific user WebDAV clients on or off.

  * **List of User-Agents (comma as separator)**<br>
	Not allowed user-agents.
	
* * *

  *  **Group courses by semester terms**<br>
	Activate this option to create a subfolder for each semester containing all courses of this semester. This option increases the usability for many courses. If this option is activated, no "_finished" folder is created for the finished courses. If this option is not activated, all completed courses can be found in the "_completed" folder in WebDAV.

  *  **Group courses by CPL elements**<br>
	Activate this option to create subfolders for curriculum groups containing all courses of this curriculum group.

  *  **Group "managed" courses**
  *  **Prepend external course reference to title**<br>
	Decide whether the course [reference](../../manual_user/learningresources/Course_Settings_Info.md) should prepend
	the course title in order to be able to distinguish between similar course
	titles.  

* * *

  * **Enable access for courses where user is participant or coach**<br>
	Activate this option to also allow students and coaches to access their course folders. Only the folders of the corresponding folder course elements are displayed, as well as any integrated resource folders.

  *  **Enable access for courses that users marked as favorite**<br>
	Activate this option to also allow students and coaches to access course folders of courses that are in their favorites list but of which they are not members. This is only possible with the corresponding settings in the access configuration. Only the folders of the corresponding folder course elements are displayed, as well as any integrated resource folder.

## Usage

More information about WebDAV usage in OpenOlat: [Using WebDAV](../../manual_user/basic_concepts/Using_WebDAV.md)

