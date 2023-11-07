# Security

## System wide security settings

Requirements towards security can vary greatly depending on the institution.
Use the security settings to configure the necessary security level while
taking the associated risk into account.

**Force file download in folders** : Select this security setting to always
dowload files from folders and never open them directly in the browser. This
prevents possible Cross-Site-Scripting attacks (XSS). When this feature is
enabled all documents are downloaded as files and will not be displayed in the
browser directly, including HTML documents. This behavior does not apply to
the course element "HTML page".

**Prevent embedding in frames** : Select this security feature to prevent
OpenOlat from being loaded in a HTML frame or iFrame. By doing this possible
Cross-Frame-Scripting attacks (XFS) will be prevented. If you enable this
feature it is no longer possible to embedd OpenOlat in an existing website
using frames.

