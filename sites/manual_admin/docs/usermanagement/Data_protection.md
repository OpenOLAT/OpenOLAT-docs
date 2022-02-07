#  [Data protection](Data+protection.html)

The EU General Data Protection Regulation (GDPR), which has been in force
since 25 May 2018, regulates the basic principles of user data protection. To
meet the requirements of the GDPR OpenOlat offers on the one hand the
possibility to export user data and on the other hand the deletion of users
and their data.

### Deleting users and user data

Deleting OpenOlat users has the following effect:

  * For users without a system role, all user data is deleted.
  * For users with administrative roles, all user data except first and last name is deleted to ensure a transparent and consistent display of administrative actions in the log files (e.g. of courses). If required, the data can also be deleted in the [user management](User+management.html#Usermanagement-Table_Deleted_Users) via the “Clear” action in the “Deleted Users” table.
  * Personal data is deleted from the log tables. The user name is deleted and replaced by an ID in the log tables.
  * Personal data is deleted from the log file. Instead of the user name, only one ID is written into the log file.
  * The user’s portfolio is deleted.
  * The user’s personal chat messages are deleted.
  * Personal forum posts and comments will be anonymized after the deletion of the user and identified as “unknown user”.
  * Comments and ratings of the user are deleted. Replies of the deleted user to comments are replaced by “User has been deleted”.
  * The user’s visiting card is no longer displayed in OpenOlat (e.g. in the forum or for comments).

  

### Export of user data

The user data stored in OpenOlat can be exported for each user.

The export must be requested from the respective user administrator. The user
administrator can perform the export via the user management. The export is
then available for download in the personal settings of the user who requested
the export in the "User data" tab. In addition, a download link is generated,
which can be made available to the user by the user administrator.

The exported user data can only be viewed by the user who requested the
export. Other users and the user administrator who executed the export do not
have access to the exported data.

The export serves solely to inform the user which data is stored and processed
on OpenOlat. It is not possible to restore a deleted user.

**Data that can be exported:**

  * User profile data (incl. invisible data) as well as personal settings
  * Published image (profile picture)
  * Personal notes
  * Documents in private and public folders
  * Information on terms of use and when they were accepted
  * Entries of the personal calendar (iCal)
  * Subscriptions
  * Course bookings
  * Evidences of achievement
  * Membership to couses
  * Membership to groups
  * Emails
  * Chat messages
  * Forum posts
  * Comments and ratings
  * Blog and Podcast posts
  * Personal documents from course tasks
  * Personal documents from course file dialog
  * Personal documents from course participant folder
  * Log
  * ePortfolio
  * Certifications

 **  
**

![](assets/Export1_EN.png)

  

### Further data protection options

 **Printing the Terms of Use**

The terms of use can be printed both during the login process in the "Terms of
Use" dialog and in the personal settings in the "Terms of Use" tab.

![](assets/Nutzungsbedingungen_drucken2_EN-2.png)
![](assets/Nutzungsbedingungen_drucken1_EN-2.png)

  

 **Visibility of e-mail addresses in OpenOlat**

E-mail addresses of other users are only visible in OpenOlat for
administrative users, not for normal users.

 