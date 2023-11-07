# Course Element "External Page" {: #external_page}

## Profile

Name | External page
---------|----------
Icon | ![External Page Icon](assets/external_page.png){ class=size24 }
Available since | New edition with release 18
Functional group | Knowledge transfer
Purpose | Display external web content within an OpenOlat course and integration in the course navigation
Assessable | no
Specialty / Note |

With the help of the course element "External page" you can call up an external website. Simply enter the desired URL in the configuration in the tab "Page content" to integrate the external page into your course navigation. For the display of the linked page, the variants

  * "Embedded" (source hidden),
  * "Embedded" (source visible),
  * "New browser window" (source visible) and
  * "Integrated completely" (source hidden)

are offered.

For pages that require authentication and whose source is hidden, you can activate "Page password controlled" and enter the corresponding values in the "User" and "Password" fields.

It is recommended to use this course element when planning to include pages containing database queries (e.g. research tools, online exercises, etc.). It is only possible to link external pages via HTTP or HTTPS protocols.

## External page: configuration

**URL:** You have to fill in this field. Here you indicate the site on which the desired external learning contents can be found (e.g._http://www.server.com/page.html_).

**Configure display:** You can choose between four options:

*  _Integrated completely (source hidden):_ The external HTML page will be parsed and integrated in your OLAT page completely. HTML pages may only contain resources such as images, Flash, videos or links with **relative paths**. Absolute relative paths such as "/public" (relative to a bsic URI) or absolute paths such as "http://..." are not allowed.

*  _Embedded (source hidden):_ The external HTML page will be included in a so-called «iframe« The external page's Internet address will not be visible. HTML pages may only contain resources such as images, Flash, videos or links with **relative paths**. Absolute relative paths such as "/public" (relative to a bsic URI) or absolute paths such as "http://..." are not allowed.

*  _Embedded (source visible):_ This also means including your external HTML page in a «iframe« The source code of the OLAT page will show you the external page's Internet address.

*  _New browser window (source visible):_ Another option is the possibility to display your external page in its own browser window.

Embedded frames («iframe«) resemble single browser windows, however, they are part of the initial window's HTML page.

Advantage of using an «iframe«: you can show any content in OLAT (e.g.complex web pages in nested frames, mathML etc.).

Disadvantage of using an «iframe«: your content might appear along with its own scroll bar.

!!! info "Info"

    If you are not sure which variant is the right one for your case, start with the option "Integrated completely" and test the other display options until the linked page is displayed as desired.