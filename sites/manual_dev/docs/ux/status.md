# Status

## Label types

### Regular

### Light

### Mega

## Characteristics
### Green

Range of application

1. Ready for use / Everything in order / Normal operation
2. Available
3. Success / Completed
4. Approval / Release
6. Active connection

Ampel logic: No dangers or safety concerns 

| Type    | Font      | Background | Border    | Label                                                              |
| ------- | --------- | ---------- | --------- | ------------------------------------------------------------------ |
| Regular | #FFFFFF | #1B652C  | #0D591B | ![Regular green](assets/green-regular.png){ class="thumbnail-sm" } |
| Light   | #1B652C | #FFFFFF  | #0D591B | ![Light green](assets/green-light.png){ class="thumbnail-sm" }     |
| Mega    | #1B652C | #e6eee2  | #e6eee2 | ![Mega green](assets/green-mega.png){ class="thumbnail" }          |

| Component  | Context               | icon                               | State       | Range of application |
| ---------- | --------------------- | ---------------------------------- | ----------- | -------------------- |
| Course     |                       | :fontawesome-solid-check:          | Published   | 2.                   |
| Course     | Assessment mode       | :fontawesome-solid-spinner:        | In progress | 1.                   |
| Course     | Assessment inspection | :fontawesome-solid-check:          | Carried out | 3.                   |
| Catalog    |                       | :fontawesome-solid-cart-shopping:  | Bookable    | 2.                   |
| Catalog    | Offer period          | :fontawesome-solid-hourglass-half: | Ongoing     | 1.                   |
| Curriculum | Curriculum element    | :fontawesome-solid-check:          | Confirmed   | 4.                   |
| Curriculum | Curriculum element    | :fontawesome-solid-check:          | Active      | 1.                   |

### Yellow

Range of application

1. Warning / Caution
2. Check required
3. Reduced performance / Limitations
4. Intermediate state

Ampel logic: Attention required

| Type    | Font      | Background | Border    |  Label                                                              |
| ------- | --------- | ---------- | --------- | ------------------------------------------------------------------- |
| Full    | #574000 | #fbd774  | #fcca46 | ![Regular green](assets/yellow-regular.png){ class="thumbnail-sm" } |
| Light   | #574000 | #FFFFFF  | #fcca46 | ![Light green](assets/yellow-light.png){ class="thumbnail-sm" }     |
| Mega    | #805e00 | #fbe6a7  | #fbe6a7 | ![Mega green](assets/yellow-mega.png){ class="thumbnail" }          |

| Component  | Context               | icon                                     | State            | Range of application |
| ---------- | --------------------- | ---------------------------------------- | ---------------- | -------------------- |
| Course     |                       | :fontawesome-regular-star:               | Review           | 2./4.                |
| Course     | Assessment mode       | :fontawesome-solid-hourglass-half:       | Preparation time | 3./4.                |
| Course     | Assessment inspection | :fontawesome-solid-user-slash:           | No-show          | -                    |
| Catalog    |                       | :fontawesome-solid-triangle-exclamation: | Fully booked     | 2.                   |
| Curriculum | Curriculum element    | :fontawesome-solid-hourglass-half:       | Provisional      | 4.                   |

### Blue

Range of application

1. Waiting state
2. Draft
3. Security / Confidentiality
4. Neutral
5. Stable states

Ampel logic: No action needed

| Type    | Font      | Background | Border    | Label |
| ------- | --------- | ---------- | --------- | ----- |
| Full    | #FFFFFF | #3F5873  | #384E66 |       |
| Light   | #3F5873 | #FFFFFF  | #384E66 |       |
| Mega    |           |            |           |       |

| Component  | Context               | icon                       | State       | Range of application |
| ---------- | --------------------- | -------------------------- | ----------- | -------------------- |
| Course     |                       | :fontawesome-solid-pencil: | Preparation | 2.                   |
| Course     | Assessment mode       | :fontawesome-solid-clock:  | Scheduled   | 1.                   |
| Course     | Assessment inspection | :fontawesome-solid-clock:  | Scheduled   | 1.                   |
| Catalog    | Offer period          | :fontawesome-solid-clock:  | Planned     | 1.                   |
| Curriculum | Curriculum element	 | :fontawesome-solid-pencil: |	Preparation | 2.                   |

#### Orange

Range of application

1. Increased warning level / Urgent attention required
2. Limited functionality / Severe restrictions
3. Transition to a critical state

Ampel logic: Increased warning, intervention urgently required, but not yet critical.

| Type    | Font      | Background | Border    | Label |
| ------- | --------- | ---------- | --------- | ----- |
| Full    | #522D00 | #FFC685  | #ff8c00 |       |
| Light   | #522D00 | #FFFFFF  | #ff8c00 |       |
| Mega    |           |            |           |       |

| Object  | Context               | icon                        | State       | Range of application |
| ------- | --------------------- | --------------------------- | ----------- | -------------------- |
| Course  | Assessment inspection | :fontawesome-solid-spinner: | In progress | -                    |

#### Red

Range of application
1. Flagged as deleted
2. 

| Type    | Font      | Background | Border    | Label                                                              |
| ------- | --------- | ---------- | --------- | ------------------------------------------------------------------ |
| Regular | #FFFFFF | #b30018  | #a80016 | ![Regular green](assets/green-regular.png){ class="thumbnail-sm" } |
| Light   | #b30018 | #FFFFFF  | #a80016 | ![Light green](assets/green-light.png){ class="thumbnail-sm" }     |
| Mega    | #d6001c | #fff8f6  | #fff8f6 | ![Mega green](assets/green-mega.png){ class="thumbnail" }          |

Ampel logic: Danger and critical, intervention required

### Brown

Range of application

1. Completed processes but available
2. Read-only / Limitations 

| Type    | Font      | Background | Border    | Label |
| ------- | --------- | ---------- | --------- | ----- |
| Full    | #FFFFFF | #804A33  | #6D3F2C |       |
| Light   | #804A33 | #FFFFFF  | #6D3F2C |       |
| Mega    |           |            |           |       |

| Object     | Context               | icon                             | State     | Range of application |
| ---------- | --------------------- | -------------------------------- | --------- | -------------------- |
| Course     |                       | :fontawesome-solid-ban:          | Finished  | 1./2.                |
| Course     | Assessment mode       | :fontawesome-solid-ban:          | Follow-up | 1./2.                |
| Course     | Assessment inspection | :fontawesome-solid-circle-xmark: | Cancelled | -                    |
| Curriculum | Curriculum element    | :fontawesome-solid-ban:          | Finished  | 1./2.                |

### Grey

Range of application

1. Deactivated status / offline
2. Completed processes
3. Currently not available

Ampel logic: Inactive or not relevant

| Type    | Font      | Background | Border    | Label                                                            |
| ------- | --------- | ---------- | --------- | -----------------------------------------------------------------|
| Full    | #FFFFFF | #595959  | #454545 | ![Regular grey](assets/grey-regular.png){ class="thumbnail-sm" } |
| Light   | #595959 | #FFFFFF  | #454545 | ![Light grey](assets/grey-light.png){ class="thumbnail-sm" }     |
| Mega    | #342c24 | #F6F6F6  | #F6F6F6 | ![Mega grey](assets/grey-mega.png){ class="thumbnail" }          |

| Object     | Context               | icon                             | State         | Range of application |  
| ---------- | --------------------- | -------------------------------- | ------------- | -------------------- |
| Course     | Assessment mode       | :fontawesome-solid-circle-minus: | End           | 2.                   |
| Course     | Assessment inspection | :fontawesome-solid-ban:          | Withdrawn     | 2.                   |
| Catalog    |                       | :fontawesome-solid-eye-slash:    | Not available | 3.                   |
| Catalog    | Offer period          | :fontawesome-solid-ban:          | Ended         | 2./3.                |
| Curriculum | Curriculum element    | :fontawesome-solid-circle-xmark: | Cancelled     | 2./3.                |


## By object
### Global Status

* Note
* Info
* Warning
* Error

#### Object Status (Life Cycle)

* Active
* Inactive
* Deleted (Trash)

### User

#### User Status

* active
* active and not deletable
* pending
* inactive
* Login denied

#### User Chat Status

* available
* please do not disturb
* not available

### Learning Ressource

#### LR Publish Status

* Preparation
* Review
* Access for coach
* Published
* Finished

#### LR Success status colors

* Passed
* not passed
* undefined

#### LR Release status

* released
* not released

### Course Element

#### Course element status / LR Learning-path progress

* not ready
* not started
* started
* to review
* assessed

#### Course element visited status

* visited
* partly visited
* not visited

### e-portfolio

#### Pages status

* draft
* published
* in revision
* closed
* deleted

#### Sections status

* assignment
* not started
* in progress
* closed

### Quality Management

#### Datenerhebungen

* Preparation
* Prepared
* Durchführung
* Abgeschlossen

### Question Bank

#### Question status

* draft
* review
* revision
* final
* end of life

### Curriculum

#### Curriculum element status

* active
* inactive
* deleted

### Lection

#### Lection block status

* aktiv
* autoerledigt
* erledigt

#### Lection Participant status

* anwesend
* entschuldigt
* unentschuldligt

### Coaching Tool

#### Grading assignments

* unassigned
* open
* first reminder
* second reminder
* deadline missed
* closed (done)

#### Corrector status

* active
* inactive
* removed