#  [General Information on Tests](General+Information+on+Tests.html)

OpenOlat tests are available in the standardized document format QTI 2.1. QTI
stands for "Question & Test Interoperability" and is a defined, standardized
data format used to design online tests. The advantage is that these
standardized tests can be used in various LMS and other systems that support
the standard. [IMS](http://www.imsglobal.org/) strives to develop such open
standards for e-learning.

In OpenOlat tests are part of the "learning resources". Learning resources are
created separately and can be integrated into online courses. For example, the
same learning resource "Test (QTI 2.1)" can be used in several courses.

## What is a test?

Tests are used to monitor performance, to check the current state of knowledge
or as an online exam. They can be used at the beginning, during or at the end
of a course or independently of courses.

Formative tests are about capturing an intermediate learning stage and
achieving a learning improvement based on automated or manual feedback.

Summative tests are only used at the end of a learning process or event. This
checks whether the planned learning goals have been achieved. An example of
this are sharp exams or online exams.

Tests are created using the [OpenOlat test editor](Test+editor+QTI+2.1.html)
as a QTI 2.1 test. The length of the test, the [question
types](Test+question+types.html) and a number of other configurations can be
determined.

Test participants cannot read in the source code of the test or self-test
which solutions are right and which are wrong, since the answers are sent to
the OpenOlat server and only evaluated there.

If you include a test in your [course](Tests+at+course+level.html), you can
decide whether you want to use it as a self-test, i.e. for practice purposes,
or as a test ("sharp" test). In the first case you use the course element
"Self-test" when integrating the test into the course, in the second case you
use the course element "Test". Self-test results are stored anonymously,
examination test results personalized. In self-tests, the teacher is unable to
trace the results achieved by a particular learner.

Depending on the teaching scenario, it may also make sense to use normal
"tests" rather than "self-tests" for practice purposes, i.e. whenever the
teacher wants to know how individual learners are developing or when it is a
question of recognising and specifically supporting weaker course members. In
this respect, it should always be checked individually which course element is
the most suitable.

## How do the questions get into a test?

Questions can either be created directly in the test learning resource or
created in the question pool and then integrated into the test. In the chapter
"[Four steps to your test or self-test](Four+Steps+to+Your+Test+or+Self-
test.html)" you will learn how to create a test.

Information on how to use the question pool can be found
[here](Question+Bank.html).

When you import a question from the question pool into a test, a copy of the
question is made at that time. The question in the test is therefore
independent of the original question in the question pool. If the original
question is modified in the question pool, this does not affect the imported
question in the test. This remains unchanged.

The questions imported in tests from the question pool cannot be edited in the
editor!

If a question is to be edited, a copy of the question can be created and
edited via "Create and edit copy". The question then gets a new ID of its own.
However, you can still access the original imported question in the question
pool via the master ID.

  

You may already have exported a test file in IMS-QTI format from another LMS
and want to import it into OpenOlat. In the chapter "Actions in the Author's
Area" you will find information on how to proceed under
"[Import](Actions+in+the+'Authoring'+section.html#Actionsinthe'Authoring'section-
section-_import)".

  
