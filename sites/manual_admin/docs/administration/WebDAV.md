# WebDAV

## Module configuration

The WebDAV module can be enabled/disabled system wide. The following
parameters can be configured:

  *  **WebDAV access**  
	Enable or disable the WebDAV access. When enabled, all system users can access
	their OpenOlat folder using WebDAV (recommended).

  *  **Show WebDAV links**  
	Decide if the WebDAV URL is displayed in the folder component or not. This is
	independent of the the WebDAV access. When disabled, WebDAV can still be used
	but the WebDAV link must be known by users as it is not displayed in the web
	interface.

  *  **Digest Authentication for HTTP access**  
	To use WebDAV on Windows operating systems without manually importing
	certificates it is mandatory to operate the WebDAV interface using HTTP and no
	SSL. In that case files will be transfered without encryption. To still
	transmit the password encrypted, the Digest Authentication method must be used
	to support Windows.
	
	!!! attention "Security note"
		The Digest Authentication method does not use strong encryption and can be
		cracked with enough computing effort. To meet very high security demands users
		should always use HTTPS with SSL encryption. When using Windows this will make
		it necessary to manually import certificates or to use a dedicated WebDAV
		client.

  * **WebDAV Client exclusion**  
	Turn exclusion of specific user WebDAV clients on or off. 

  * **List of User-Agents (comma as separator)**  
	Not allowed user-agents.
	
* * *

  *  **Group courses by semester terms**  
	Activate this option to create a subfolder for each semester containing all courses of this semester. This option increases the usability for many courses. If this option is activated, no "_finished" folder is created for the finished courses. If this option is not activated, all completed courses can be found in the "_completed" folder in WebDAV.

  *  **Group courses by curriculum elements**  
	Activate this option to create subfolders for curriculum groups containing all courses of this curriculum group.

  *  **Group Managed Course**
  *  **Prepend external course reference to title**  
	Decide whether the course [reference](../../manual_user/learningresources/Set_up_info_page.md) should prepend
	the course title in order to be able to distinguish between similar course
	titles.  

* * *

  * **Enable access for courses where user is participant or coach**  
	Activate this option to also allow students and coaches to access their course folders. Only the folders of the corresponding folder course elements are displayed, as well as any integrated resource folders.

  *  **Enable access for courses that users marked as favorite**  
	Activate this option to also allow students and coaches to access course folders of courses that are in their favorites list but of which they are not members. This is only possible with the corresponding settings in the access configuration. Only the folders of the corresponding folder course elements are displayed, as well as any integrated resource folder.

## Usage

More information about WebDAV usage in OpenOlat: [Using WebDAV](../../manual_user/basic_concepts/Using_WebDAV.md)

