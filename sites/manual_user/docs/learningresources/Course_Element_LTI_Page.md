# Course Element "LTI Page" {: #lti}


## Profile

Name | LTI Page
---------|----------
Icon | ![LTI Page Icon](assets/basiclti.png){ class=size24  }
Available since |  Release 15.5 (beta)
Functional group | Others
Purpose | Integration of external learning applications
Assessable | yes
Specialty / Note |



By means of the course element "LTI page" it is possible to integrate externa learning applications in your course before having their content displayed in an OpenOlat window. LTI means "Learning Tool Interoperability" and is an IMS standard to embed external learning applications such as e.g. a chat, a media Wiki, a test editor, or a virtual lab. More information about LTI can be found on the LTI project page: [http://www.imsglobal.org/lti/](http://www.imsglobal.org/lti/)

## Process

* Indicate the URL to be referenced in the tab "Page content" along with its key
and password.
* When a user selects the LTI page in the course navigation, he or she must first agree to the data transfer for data protection reasons before the user data and course information as well as the key are transferred to the embedded learning application in the background in a protected manner.
* Your learning application will check access rights and grant access with a valid key.
* A new query for data transfer only occurs again later if the configuration of the device changes with regard to the transmitted data.
* When the user selects the LTI page in the navigation, the integrated learning application appears in the OLAT course.


## Configure LTI page

!!! info "Note"

    The prerequisite is the activation and general setup of LTI by an administrator.


The following parameters can be configured:

![course_element_lti_page_content_v1_de.png](assets/course_element_lti_page_content_v1_de.png){ class="shadow lightbox" }

**LTI-Version:** We recommend the current version LTI 1.3 However, for compatibility reasons, the older version can also be selected.

If your administrator has set up deep links, you can select preconfigured deep links under this item. Some of the following entries are then already made automatically.

**URL:** In this input field, enter the address of the external learning application. <br> The format is for example "https://tools.< Firma xyz >.com/lti_quiz/lti_quizwand.php".

**Key:** Please indicate the key provided by the supplier of your external learning application (in the example above this would be "lti_quiz").

**Password:** Please indicate the corresponding password to your key provided by the supplier of your external learning application (in the example above this would be "weeHoo1w").

**Skip launch page:**  If this option is activated, the connected application is displayed directly, without the "Display LTI Learning Content" intermediate page. The administrator can disable this option.

* * *

**Transmit firstname/name:** By checking this box a user's first and last name will be transferred to your external learning application. Otherwise users will be able to use this application anonymously.

**Transmit e-mail address:** By checking this box a user's e-mail address will be transferred to your external learning application.

**Additional attributes:** You can add additional parameters inside this input box that should be transferred to a learning application. You can e.g. tell this learning application to transfer a query from the learning platform OLAT. (External learning applications have to be able to process such transferred information; therefore it is necessary to have an agreement with your provider.) You have the choice between text attributes (identical values for each user) and additional dynamic user attributes (different for each user). You can add as many attributes as you wish, but note that the LTI resource must know which attributes are sent as this is not specified in the standard.

* * *

**OpenOlat roles:** Here you can configure which role the user will have when launching the LTI resource. The three OpenOlat roles Author, Coach and Participant are supported. For each role the mapping can be defined to a corresponding role on the LTI resource. The following LTI roles are available: Learner, Instructor, Administrator, Teaching assistant, Content developer and Mentor.

**Transfer score:** Select this checkbox when the LTI resource is generating a score value that can be transmitted to OpenOlat using the LTI 1.1 standard. This is optional. The submitted score will appear on the users start screen of the LTI course element as well as in the efficiency statement of this course. Please be aware that according to the LTI standard only values between 0 and 1 are allowed.

!!! info "Info"

    If the option "transfer score" is activated, the LTI page can be added as an assessable course element to the course, which then appears in the assessment tool. In addition to that, the score also appears on the homepage of the LTI course element.

 **Scaling factor:** With the scaling factor the LTI results, which must have a value between 0 and 1 according to the LTI specification, can be scaled to a more practical value for the OpenOlat course. For example, if you want an LTI exam to have a maximum of 10 points in OpenOlat, you must specify a scaling factor of "10". If you want the transmitted score to be unmodified, use the factor "1".

 **Score needed to pass:** Here you can configure an optional cut value to define when the LTI course element is considered as being passed. The cut value relates to the score value after scaling and not to the raw value transmitted by LTI. In the example above a cut value of "5" is equivalent to "50%".

* * *

 **Display:** Select the option "Embedded in course (iFrame)" to embed the LTI resource within the course layout. The option "Display only module, hide LMS (iFrame)" completely hides OpenOlat while the LTI module is active. With the option "Open in new window" the LTI resource is opened in a separate window. This can be useful in case the resource needs a lot of space or has to be used in parallel with other course elements.

 **Display height:** Select "automatic" or an explicit size in case the automatic feature does not work properly.

 **Display width:** Select "automatic" or an explicit size in case the automatic feature does not work properly.

* * *

 **Show all information transmitted on launch (Debug):** By checking this box, other users will be able to see the information sent. This information includes parameters such as user identification, course title, course element, etc.By clicking on "Launch Endpoint with BasicLTI Data" in the course view on top of your display of the data sent you will get to the homepage of your learning application.