# Course Element "Practice" {: #course_element_uebung}


## Profile {: #profile}

Name | Task
---------|----------
Icon | ![Practice Icon](assets/course_element_practice_icon.png){ class=size24 }
Available since | Release 17
Functional group | Assessment
Purpose | Knowledge transfer and self-examination. A defined number of questions must be answered. Questions that are not answered correctly are asked again and repeated according to the flashcard principle. 
Assessable | no
Specialty / Note | Exercise questions can be managed in the question pool

---

## Operating principle {: #operating_principle}

The course element "Practice" works according to the principle of a flashcard. The subjects correspond to levels.

![course_element_practice_flashcardfile_v1_de.png](assets/course_element_practice_flashcardfile_v1_de.png){ class="shadow lightbox" }

!!! info "Info"

    All questions must be automatically correctable. Therefore, no question types are allowed that require mandatory manual assessment, such as "free text entry" or "drawing".

---

### Level {: #level}

In order to be able to assess one's own performance even without evaluation (points), a learning level is displayed for each question. A level indicates how successfully a question was answered.

**Downgrading**<br>
For example, if a question was answered correctly 3 times in a row, it is in level 3. If it is then not answered correctly once, it drops back to level 2.

**System wide availability**<br>
The results (personal level for a question) are stored with the respective participant. They are thus available globally throughout the system. Even if the participant takes part in another course.

This means, for example, that if a question has already been answered correctly twice and is therefore classified in level 2, OpenOlat remembers: Learner A has question y in level 2. If this question comes up again in another course element exercise or in a completely different course, Learner A does not start there from 0, but builds on his/her already achieved level.

This can even mean that someone enters a course for the first time and discovers there in the learning status display of a course element exercise that a certain percentage has already been reached.

---

### Exercise series {: #exercise_series}

Questions are always asked in exercise series of, for example, 10 questions. The number of questions can be set per exercise series.

For the exercise series questions can be compiled

* from several learning resources (different test learning resources) 
* or from shares (freely given questions of a question pool) 


The learning resources and shares that should be available for the creation of the exercise series have to be specified by the author in the configuration of the course element.

It is also possible for participants to compile their own series of questions. Learners can thus focus individually on specific subject areas and filter out questions relevant to them on the basis of the taxonomy.

---

### Challenges {: #challenge}

Several series of exercises make up a challenge. A challenge is an intermediate goal that can be reached by completing a certain number of series.

The total number of challenges can be set.

After completion of a challenge, detailed statistics on the learning status as well as a summary overview are available in addition to the ranking.

---

## Configuration {: #configuration}

As with all course elements, the author selects the course element Exercise in the course menu for configuration. Especially in the **tab "Configuration"** you will find the setting options and settings.

![course_element_practice_konfig_v1_de.png](assets/course_element_practice_konfig_v1_de.png){ class="shadow lightbox" }


### Ressources {: #resources}

In contrast to most other course elements, the course element Practice allows you to integrate **several learning resources**. The questions used in the course element practice come from the question pool or test learning resources.

Currently there are 2 ways to insert questions into the Course element Practice:

* On the one hand, you can include a **learning resource Test**, as you do in the course elements Test and Self-Test. Then the questions from the tests can be practiced.

* On the other hand, questions can be inserted via **Share**. Shares are shared question packages from the question pool (lists, shares, group shares).

Later modification or addition of questions is possible.


### Criteria {: #criteria}
  By defining criteria for taxonomy and metadata, the desired questions can be specifically filtered out.


### Practice settings {: #practice_settings}

In the practice settings, the author determines:

* Number of levels 
* Number of questions per series
* Number of series per challenge
* Number of challenges required as completion criteria

All available questions are displayed in an overview (grouped by subject/taxonomy).


!!! info "Please note:"

    These are links of the questions. No copies of the questions are stored in the course element. So if a question is changed or deleted, it is also changed or gone accordingly in the course element Practice.


---

## Practice practically {: #practice_practically}

### Given practices {: #given_practices}

In the configuration of the course element, coaches can control which questions are included in the automatically assembled series of exercises.

![course_element_practice_ueben1_v1_de.png](assets/course_element_practice_ueben1_v1_de.png){ class="shadow lightbox" }

The filtering is done by the author in the course editor through the settings in the "Criteria" section:

* Selection of the appropriate learning resources
* Confinement to a specific taxonomy
* Do not include questions without subject area
* further narrowing down to specific contained metadata

In addition, the participants can also practice by subject area, which will be offered according to the pre-selection of the authors.

![course_element_practice_ueben_fachbereich_v1_de.png](assets/course_element_practice_ueben_fachbereich_v1_de.png){ class="shadow lightbox" }


### Self compiled exercises {: #self_compiled_exercises}

Learners can also compose their own question series from the included question set or use a predefined selection, an individual practice series.

From the second round onwards, the learner can then decide whether to work only on completely new questions or on those that were answered incorrectly. 


For individual practice according to their own needs, participants can therefore choose between 3 different modes:

**New questions**: Practice with questions that the participant has never answered before.

**My mistakes**: Practice with questions that have already been answered incorrectly by the participant.

**Own series**: Practice with a series of questions you put together yourself

![course_element_individual_practice_v1_de.png](assets/course_element_individual_practice_v1_de.png){ class="shadow lightbox" }


### Feedbacks {: #feedbacks}

Feedback to the learner on whether he or she answered a question correctly or incorrectly is provided immediately following the completion of a question.

For the entire practice, the learner can, for example, retrieve information about his learning time.

Rankings are also possible, if desired.

When selecting a course element, coaches can see from a list which participants have already started practicing or how far they are in practicing.

Since no manual evaluations are carried out by coaches, no feedbacks by coaches are available.

---

## Comparison: Test - Self-test - Practice {: #comparison}


Course element Test | Course element Self-test | Course element Practice
---------|----------|----------
 ![course_element_practice_icon_test](assets/course_element_practice_icon_test.png){ class=size24  } | ![course_element_practice_icon_test](assets/course_element_practice_icon_test.png){ class=size24  } | ![Aufgabe Icon](assets/course_element_practice_icon.png){ class=size24  }
with score | with score  | without score 
viewable for coaches|  not visible for coaches | einsehbare Level<br>Learning level per level<br> Emphasis by participant:in
1 test learning resource | 1 test learning resource | multiple learning resources<br>Shares/Shares from the question pool<br>filter with use of taxonomy
