# Library {: #library}


## Concept {: #concept}

* The library can be activated/deactivated separately as required for the entire instance.
* There is only one library per OpenOlat instance.
* It usually appears as a menu item in the top navigation bar.
* Technically speaking, the library is a linked resource folder that can be edited in the authoring area.
* Documents in the library can be commented on by users, downloaded or sent directly by email.

[To the top of the page ^](#library)

---

## Set up the structure of the library {: #structure}

If administrators activate the module, an associated resource folder must be specified.
To set up the structure of the library, owners can edit this assigned resource folder in the authoring area.

[To the top of the page ^](#library)

---

## Upload documents {: #upload}

**Who can upload documents to the library?**<br>

If administrators have allowed uploading, all users can upload documents to the library. The setting is located in the system administration under:<br>
`Administration > Modules > Library`<br>
However, the documents are only added to the library after a check has taken place.

**What can be uploaded?**<br>

A variety of file formats can be uploaded:

* Office documents, such as docx, xlsx, pdf, etc.
* Image files, such as jpg, png, etc.
* Video files (mp4)
* ...

[To the top of the page ^](#library)

---

## Upload check {: #upload_check}

After uploading a document, it is first checked by default before it is displayed in the library.

Owners of the resource folder linked to the library are informed of a new upload and must approve the document.

Alternatively, another person can be designated for the check. To do this, administrators enter an email address in the system administration under `Administration > Modules > Library`. If no address is entered there, the owners of the learning resource receive the check request.

Administrators can also deactivate this check process under `Administration > Modules > Library`. However, if you deactivate the check, you should be aware that anyone who has access to the library can upload documents there unchecked. [:octicons-tag-16:{ title="from Release 19.1 (OO-8309)" }](https://track.frentix.com/issue/OO-8309)


[To the top of the page ^](#library)
