# Course Element "External Page" {: #external_page}

## Profile

Name | External page
---------|----------
Icon | :o_icon_o_tu_icon:
Available since | New edition with release 18
Functional group | Other
Purpose | Display external web content within an OpenOlat course and integration in the course navigation
Assessable | no
Specialty / Note | Has to be switched on by the administration. frentix does not recommend its use.

With the help of the course element "External page" you can call up an external website. Simply enter the desired URL in the configuration in the tab "Page content" to integrate the external page into your course navigation. For the display of the linked page, the variants

  * "Embedded (source hidden)",
  * "Embedded (source visible)" and
  * "New browser window (source visible)"

are offered.

For pages that require authentication and whose source is hidden, you can activate "Page password controlled" and enter the required access data.

Typical use cases are pages containing database queries, for example a literature research tool or online exercises from the web. It is only possible to link external pages via HTTP or HTTPS protocols.

!!! warning "frentix recommends keeping domains separate"

    The course element "External Page" displays content of a foreign domain
    inside your OpenOlat domain. Based on modern security considerations,
    frentix recommends not to mix different domains and therefore advises
    against the use of this course element.

    A domain is the internet address under which a page is delivered: your
    OpenOlat instance runs under its own address, the embedded page under a
    different one.

Instead, refer to the page with the [Link list](Course_Element_Link_List.md). If the course element is not available in your instance, your administration has not switched it on.

## Tab "Page content" configuration

**URL:** You have to fill in this field. Here you indicate the site on which the desired external learning contents can be found (e.g._https://www.server.com/page.html_).

**Configure display:** You can choose between three options:

*  _Embedded (source hidden):_ OpenOlat calls up the external page and displays it in a so-called «iframe» in the course window. The external page's Internet address will not be visible to participants. For the page to be displayed completely this way, the embedded HTML pages may only address resources such as images, videos or links with **relative paths**. Content behind absolute paths such as "https://..." or relative absolute paths such as "/public" is loaded by the participants' browser directly from the external page; its address becomes visible in the process.

*  _Embedded (source visible):_ The participants' browser calls up the external page directly and also displays it in an «iframe». The source code of the OpenOlat page will show you the external page's Internet address.

*  _New browser window (source visible):_ The course element displays a button that opens the external page in its own browser tab.

**Page password controlled:** This option is only available with the display "Embedded (source hidden)". The access data applies to all participants jointly. It is stored unencrypted in the configuration of the course element and is therefore contained in every course copy and every course export. Do not enter personal access data here.

Embedded frames («iframe») resemble single browser windows, however, they are part of the initial window's HTML page.

Advantage of using an «iframe»: you can show any content in OpenOlat (e.g. complex web pages in nested frames, mathML etc.).

Disadvantage of using an «iframe»: your content might appear along with its own scroll bar.

!!! tip "Choose the variant by display and risk"

    The three variants do not only differ in how the page is displayed. With
    "Embedded (source hidden)" OpenOlat calls up the page; the external page
    learns nothing about your participants. With the other two variants the
    participants' browser connects directly to the external page. Weigh both
    against each other and test the display options one after the other until the
    linked page is displayed as desired.
