# WebDAV

**Module configuration**

The WebDAV module can be enabled/disabled system wide. The following
parameters can be configured

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

The Digest Authentication method does not use strong encryption and can be
cracked with enough computing effort. To meet very high security demands users
should always use HTTPS with SSL encryption. When using Windows this will make
it necessary to manually import certificates or to use a dedicated WebDAV
client.

* * *

  *  **Group courses by semester terms**  
Enable this flag to list the available semester terms first and within a
semester term only the courses from this term. This greatly improves usability
with many courses.

  *  **Group courses by curriculum elements**  
Activate this option to create subfolders for curriculum groups containing all
courses of this curriculum group.

  *  **Group Managed Course**
  *  **Prepend external course reference to title**  
Decide whether the course [reference](Set+up+info+page.html) should prepend
the course title in order to be able to distinguish between similar course
titles.  

* * *

  * **Enable access for courses where user is participant or coach**  
Enable this option to allow students and coaches to access course folders via
WebDAV. Only folder course element folders will be displayed.

  *  **Enable access for courses that users marked as favorite**  
Enable this option to allow students and coaches to access course folders via
WebDAV that are marked as favorite, without being a member of that course.
Access configuration must be set correspondingly. Only folder course element
folders will be displayed.

 **Usage**

More information about WebDAV usage in OpenOlat: [Using
WebDAV](Using+WebDAV.html)

