# Session Timeout and Logout [:octicons-tag-16:{ title="from Release 19.0 (OO-7672)" }](https://track.frentix.com/issue/OO-7672) {: #session_timeout_logout}

OpenOlat manages a session for every logged-in user. Each click (for example opening a question in a test) restarts the session time of the session. The system administrators can set the session time as required. If you do not click anywhere in OpenOlat within the session time, the session expires.

The expiry of the session is not announced in advance. On the next click after the expiry, the message "You have been logged out" appears. "Log in again" takes you to the login page. All unsaved data is lost when you log in again. With "Back to page" you can first copy unsaved input to the clipboard. Therefore, save your work regularly.

You can log out of OpenOlat at any time via "Log out" in the [personal menu](../personal_menu/index.md) at the top right. This takes you back to the [login page](../login_registration/Login_Page.md). If you do not log out but close the browser window or the browser, your session continues until the session timeout.

If you use OpenOlat at public workstations, it is important that you log out after working with OpenOlat and do not just close the browser window. As long as your session is running, another person could work in OpenOlat with your login data on the same computer.

## Further information {: #further_information}

[Personal menu and general components >](../personal_menu/index.md)<br>
[Login Page >](../login_registration/Login_Page.md)<br>
[Login Concept >](../login_registration/Login_Concept.md)<br>
[System >](../../manual_admin/administration/System.md)

[To the top of the page ^](#session_timeout_logout)
