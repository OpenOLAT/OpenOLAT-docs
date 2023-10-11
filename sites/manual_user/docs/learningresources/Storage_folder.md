# Storage folder

The "Storage folder" of a course serves the course creator as a repository for the files used in the course. This includes e.g. all HTML pages, graphics and files used that are made available via the course element "Folder". The files are, so to speak, ready to hand in the background and can be made available at any time via the corresponding course elements.

Course participants have no direct but only indirect access to files of the storage folder. In order to access the files, they must be linked via corresponding [Course Elements](Course_Elements.md). A storage folder is always course specific.

![Course storage folder](assets/Storagefolder_01.png){ class="shadow lightbox" }

In the storage folder files can be uploaded, deleted, moved, searched for, zipped, un-zipped or created. By default, HTML documents can be created in OpenOlat. If additional document editors are activated in the administration, further file formats can be created. For example, if Only Office is used, Word, Excel or PowerPoint files can also be created.

When uploading a file, the file size limit as well as the folder space limit has to be taken into consideration. Also those limits apply when uploading files via [WebDAV](../basic_concepts/Using_WebDAV.md) to the storage folder.

![File upload](assets/upload_file.png){ class="shadow lightbox" }

Furthermore, the storage folder can be usefully provided with further subfolders and thus a systematic structuring of course-related files can be implemented.

Additionally, OpenOlat automatically generates the folders "**_courseelementdata**" or "**_sharedfolder**", if the course contains at least one [course element "Folder"](../learningresources/Knowledge_Transfer.md#course-element-folder--folder) or if the course is connected to a resource folder.

In the subfolder **"_courseelementdata"** you can find all course elements "[folder](../learningresources/Course_Element_Folder.md)" and "[Participant folder](../learningresources//Course_Elements.md) of a course. The corresponding folders appear here automatically after they have been created in the course editor and can be edited here as well.

Via the subfolder „ **_sharedfolder** “ you can view the linked [resource folder](../learningresources/index.md) of the course, but you can not edit it by default. Editing can be enabled in the course options by deactivating the option "read only" for the selected resource folder.

### Link course element "Single page" to storage folder

Single web specific pages (e.g. html, pdf), which are stored in the storage folder, can be made visible in the course with the course element "Single page".Additionally, the checkbox "Allow links in the entire storage folder" can be selected. Thus it becomes possible to link html-files, which can be found in the storage folder, directly. This is helpful to show linked charts of a html-page or other linked files.

As soon as the checkbox is activated, the path for other files of the storage folder is visible. Thus it becomes possible, to call up files, which are determined in the storage folder but aren't published in the course itself.
