# Blog Configuration {: #blog_configuration}

The configuration of a blog takes place in two places: **in the course element** and **in the learning resource**.

## Configuration in the "Blog" course element {: #blog_configuration_course_element}

After you have inserted a course element "Blog" in the course editor, you will find the configurations for the learning resource and authorizations in the **"Blog learning content"** tab of the course element.

Depending on the course type, the display settings are possible in the tabs "Visibility" and "Access" (conventional courses) or "Layout" and "Learning path" (learning path courses).

!["Blog learning content" tab of the course element "Blog", where the blog learning resource is selected, its metadata is adopted, and the permissions for moderation and post creation are defined](assets/blog_configuration_tab_content_v1_de.png){ class="shadow lightbox" }



### ![1](assets/1_green_24.png) Select blog

If no blog learning resource has been added yet, you can choose between

* Selecting an existing blog learning resource in the authoring area
* Creating a new blog learning resource
* Linking an external blog
* Importing an existing blog as a file

Once a learning resource has been inserted, the "Replace" button is displayed so that the learning resource can be replaced. You can also edit the blog learning resource directly from here.

![Button "Replace" with the options "Create", "Import" and "Embed via URL", plus the link "Edit learning resource" in the "Select blog" section](assets/blog_configuration_replace_v1_de.png){ class="shadow lightbox" }


!!! info "Important"

    You can choose an existing blog if you already run a blog independently of OpenOlat or if you want to integrate a well-known blog into your OpenOlat course as content or a basis for discussion. In this case, you cannot create your own blog posts, but the external posts can be starred and commented on.

    If you have decided on a type of blog (create entries yourself or integrate an external blog), you can no longer change this later.


### ![2](assets/2_green_24.png) Metadata configuration

Here you can determine whether the information entered in the blog **learning resource** under `Administration > Settings > Info tab` is adopted and displayed.


### ![3](assets/3_green_24.png) Permissions

**Moderator**<br>
At course element level, you can determine whether coaches can take on the [moderator role](../learningresources/Blog_Blogging.md#blog_blogging_moderate) in addition to the course owner. Since the same learning resource can be used in different courses and course elements, the learning resource can be configured with moderator rights for coaches in one course and without moderator rights for coaches in another course.

If you activate the toggle button "Show advanced configuration", you have the option of limiting the moderator role to certain time periods. You can also designate specific individuals (regardless of their role) as moderators.

![Advanced configuration of the moderator role with start and end date per entry, here for the coach role, in the Permissions section](assets/blog_configuration_tab_content_moderator_v1_de.png){ class="shadow lightbox" }

**Create posts**<br>

This defines which groups of people in the course are allowed to create blog posts. In addition to the course owners, this can be all coaches and all participants.

!!! info "Important"

    If an external blog is integrated, you cannot influence who can create entries in OpenOlat. The authorization options for "Create posts" are therefore not displayed in this case.

If you activate the "Show advanced configuration" toggle button, you also have the option of limiting the right to create posts to certain time periods.

![Advanced configuration for creating posts with start and end date per role, here for coaches and participants, in the Permissions section](assets/blog_configuration_tab_content_rights_v1_de.png){ class="shadow lightbox" }


## Configuration of the "Blog" learning resource {: #blog_configuration_learningresource}

To configure the blog learning resource, you can

* select the learning resource in the authoring area or
* Click on "Edit learning resource" directly from the blog course element in the "Blog learning content" tab.

Then select `Administration > Settings`. Configure the blog learning resource in the tabs displayed here. The settings made here are applied to all courses or course elements in which you integrate the blog learning resource.

![Info, Metadata, Sharing, Quota and Options tabs for configuring the blog learning resource in the Administration, Settings section](assets/blog_configuration_resource_tabs_v1_de.png){ class="shadow lightbox" }

**Info**<br>
Here you enter the title, description or cover image of the blog learning resource.

**Metadata**<br>
Optionally, enter additional information on the classification of the learning resource, such as subject area or language.

**Sharing**<br>
The release settings correspond to those of other learning resources:

* Intended use (default: integration in the course, alternative: stand-alone learning resource)
* Direct link (for direct access to the learning resource)
* Administrative release (in which organizational units is the resource available)
* Usage rights for other authors (referencing, copying, exporting)
* Indexing for OER catalogs and search engines
* as well as a release overview (who has which rights to this learning resource)

**Quota**<br>
Here you can set the limits for the maximum storage space the learning resource may use.

**Options**<br>
You can allow or prevent blog posts from being commented on and rated here.


## Further information {: #further_information}

**Mentioned on this page**<br>
[Blogging >](../learningresources/Blog_Blogging.md)<br>
[Create a blog >](../learningresources/Blog_Create.md)<br>
[How do I create a blog? >](../../manual_how-to/blog/blog.md)<br>
[Course Element "Blog" >](../learningresources/Course_Element_Blog.md)

**Further**<br>
[Blog: Overview >](../learningresources/Blog.md)<br>
[Access configuration >](../learningresources/Access_configuration.md)<br>
[Members management >](../learningresources/Members_management.md)

[To the top of the page ^](#blog_configuration)