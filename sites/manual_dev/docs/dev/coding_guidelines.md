# Coding Guidelines

## Development process

!!! info "The main principles are:"
	- The Jira issues always reflect the actual status of the code in the repository, during and after development in regard of
	    - Estimated, actually used and remaining effort
	    - Description and requirements
	    - Involved people (UX/requirements engineer, developer, tester)
	    - Patched files (automatic using Fisheye)
	- All commits to the master or a maintenance branch must be complete (code, documentation) and tested
	- All commits must have a corresponding Jira issue that is added to all related commit messages
	- Development and release management is done using SCRUM sprints with short iteration cycles 

### Reporting issues or feature requests

- User stories, new features, improvements and bugs are reported to the [frentix team](https://www.frentix.com)
- Large user stories or features are broken down into manageable sizes
- Feasible stories / issues are added to the product managmenet backlog and scheduled for internal discussion

### Discussions, details and priorization

- The frentix product management team analyses and prioritizes the issues on a weekly based and initiates further actions such as estimates, prototypes, UX/requirements engineering
- The product management discussion and decision making is not a public process. 
- Members of the [OpenOlat Partner program](https://www.openolat.com/open-source/) get first-hand information about product decisions and are consulted for their priorities on a regular base. 
- If accepted, the frentix product managment team feeds the specified issue in to the [Jira issue management system](https://jira.OpenOlat.org) where the specification becomes publicly visible.
- Initially the issue status is "in specification" and assigned to the responsible UX/requirements engineer
- Members of the OpenOlat partner program can vote and comment on issues to express their thoughts
- If the issue is implemented by a participant of the OpenOlat partner program, the implementing party must add documentation about implementation details such as data structures, data life cycle, class layout, architecture etc. This depends a lot on the size of the issue. 
- The specification is eventually accepted and scheduled for a release and a sprint by the frentix product management team

### Development

- The issue is assigned to a developer and set to "ready for development"
- The assigned developer set issue status to „in progress“
- Depending on the size of the issue the development happens on the master or a dedicated feature branch
- The developer adds daily time tracking to the Jira issue. The remaining time is adjusted to always reflect the status quo.
- At the end or during development code reviews are made and solutions and problems are discussed in the development team
- The developer uses the coding checklist to make sure the code matches the best practice style
- The developer makes sure the final implementation and the issue description is consistent
- The developer searches a tester and creates a documentation subtask if the issue requires user documentation

### Testing / finishing

- The developer sets the issue to „resolved“ and prepares a test installation. Normally this happens on the frentix continuous integration test infrastructure
- The tester tests the issue to find all the bugs. When bugs are found, they are commented on the issue and the issue is re-opened
- The developer fixes bugs right away and resolves the issue so the tester can test again
- The issue is ready to merge when it is ready to ship: tested, no known issues, documentation available, unit tests green etc

### Merging / Releasing

- Before merging a branch to the main development, a formal sign-of by the architect is required. When all prior steps have been done in the right way this is not a big deal, it serves more the planning of the release. It‘s too late for code reviews anyway.
- After merging, the developer and tester do some sanity check to make sure everything has been merged properly. 
- The issue is set to closed by the tester. When closing, the remaining time must be set to 0.



## Specification

### Hotfixes

Very critical bugs are fixed as soon as possible. The patch is added directly to master and the current and other affected release branches. Discussions only happens internally or in the core committer community, decisions are fast. Documentation wise hotfixes are bugs. 

### Bugs

Normal bugs are reported in Jira directly by the frentix team. A bug must contain:

- Step-by-step information how to reproduce if reproducable
- Attach annotated screenshot that shows where exactly the bug appears
- Explain the expected versus the actual behavior
- Attach a RedScreen stack trace if available
- Attach Patch if fix is already available


Depending of the nature of the bug and the number of affected classes, fixing must not necessarily happen on a special branch and can be commited directly after getting the sign-off.

### Improvements / New features

Improvements and new features must be described carefully using a user centric approach. In the first round user workflows and general concepts are discussed. When a general understanding of the issue is found the more specific technical details are discussed. 

Improvement and new features must explain what is wrong, bad, missing with the status quo and what the value for the user is when this is implemented. 

Improvements and new features generally require GUI mockups / prototypes prior to submitting code. GUI mockups can be made using Figma, Balsamiq, annotated screenshots and alike. All relevant screen have to be mocked and added to the Jira Issue. This is absolutely mandatory. 


### Refactorings

Refactorings are house keeping tasks that normally do not add new features for users. Sometimes they manifest as improvements, but most of the time is is necessary work under the hood. Jira has no special issue type for refactorings, normally we use the „improvement“ type instead. 

Refactorings issues must explain what in the status quo is wrong and how it is better afterwards. Refactorings are often relevant for the system architecture and must be discussed in detail with the architect. Normally, refactorings are done on a dedicated branch. The must be implemented fully, partially refactorings are not desired. If a refactoring is too large for a single iteration or release, it must be split up into several issues. 

Refactorings must be discussed in the developer community and timed in a way so that inevitable code conflicts can be minimized. 



## Coding standards

### General
 
- New features must generally implement an On/Off switch at least on Spring level with property place holders. For most features an admin console with context help etc. is desired. In that case the config must be saved using the `PersistedProperties`
- Adding third party libraries to the `pom.xml` is not allowed unless accepted by the architect. Existing libraries must be evaluated first. New XMLParser or WebService stacks are not allowed unless approved by the architect. 
- When adding libraries the library must explicitly be checked on Apache 2.0 license compatibility.
- Logging only using `BasicController`, `BasicManager`, `LogDelegator`, `OLog`
- Generally return empty Collections and not `null`
- For XML serialization use only `XStream`  (no com.anthonyeden, properties.storeToXml ...)
- When using `XStream` aliases must be used, class names in created XML files are not allowed
- Use the Module class to initialize the module, get and set config values and to enable/disable the entire functionality
- Use the Manager class to implement the business logic and data access
- Use the Controller to implement a workflow, but don‘t cache data there, keep as little references as possible


### Code structure

New code must follow the given package structure. Whenever possible, existing code should be refactored to match the target package structure:

	xxx.package.new_feature
		_spring
			# If required add your spring config here. If possible use annotations
		manager
			# Implementation of managers and services
			NewFeatureManagerImpl.java
			NewFeatureThingDAO.java
			NewFeatureServiceImpl.java
		model
			# Implementation of model classes
			NewFeatureThingImpl.java
		restapi
			# If the module has a REST API, the endpoints and VO classes goe here
			NewFeatureThingVO.java
			NewFeatureWebservice.java
		notifications
			# If the modules provides notification handlers, it goes here
			NewFeatureNotificationsHandler.java
		search
			# If the module provides searchable documents, it goes here
			NewFeatureDocument.java
		security
			# If the module has some security callback infrastructure, it goes here
			NewFeatureSecurityCallback.java
		site
			# If the module has it's own site in the navigation, it goes here
			NewFeatureSite.java
			NewFeatureSiteDef.java
		ui
			_content
				# all the velocity templates
			_i18n
				# Translation files, at least DE an EN must be provided
			_static
				# Rarely modules have their own CSS or JS code. 
				css
				js
			# All the UI controllers, wizards etc. are in the UI package
			NewFeaturController.java
			NewFeaturFormController.java
		# On the base level the module API is added: 
		# - interface classes for Manager, Service and model 
		# - the module configuration
		NewFeatureModule.java
		NewFeatureManager.java
		NewFeatureService.java
		NewFeatureThing.java
		# finally some package documentation 
		package.html
		doc-files

Other sub packages are allowed. Whenever possible, code should be added to the existing project structure. Code outside the `org.olat` package is generally rejected. 

!!! example
	As a best-practice example have a look at the `org.olat.modules.grading` or `org.olat.modules.bigbluebutton`.


### UI

- No DB access during rendering
- No business logic in controllers
- No direct DB access in controllers -> business logic
- No direct file access in controllers -> business logic / VFS
- Mandatory i18n translation keys in German and English

### Managers

- Extends `BasicManager`
- Implements the business logic
- No rendering logic
- No access to `UserRequest`, `WindowControl` etc.
- Dependency between Managers only via Spring `@Autowired` 
- No xxx.getInstance()
- No direct access to `java.io.File`, `VFSManager` must be used instead
- No direct access to database, `DBImpl` must be used instead
- No direct access to LDAP, Mail etc, corresponding managers and services must be used

### Database

- PostgreSQL and MySQL must be implemented and tested
- Description of data model and fields ranges (min/max size etc)
- Description of data life-cycle and data volume

### Unit Tests

- All public methods of managers must be directly called in at least one jUnit test case
- Special care must be taken for methods that perform database queries as with different databases those queries can transform differently
- Data fields must be tested with border values (max length, min etc)
- Separate jUnit test have to be made for performance and unit tests

### Selenium Tests

- Every user story must be controlled using a Selenium test case

### Documentation

- The JavaDoc must be correct and reflect the state of the code
- JavaDoc must be complete at least on interface level, when no interface is available directly on class level
- Each user form should have a corresponding context help. The context help should not just describe what the user already sees in the form but explain what this form is good for, what the effects will be etc. The context help is not written by the developer but must be provided by the implementing party.
- User documentation is required for features and improvements depending on the kind of the issue. User documentation is not written by the developer but must be provided by the implementing party.


## License

Each new file must start with a license header which is based on the following template:

	/**
	 * <a href=“https://www.OpenOlat.org“>
	 * OpenOlat - Online Learning and Training</a><br>
	 * <p>
	 * Licensed under the Apache License, Version 2.0 (the "License"); <br>
	 * you may not use this file except in compliance with the License.<br>
	 * You may obtain a copy of the License at the
	 * <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache homepage</a>
	 * <p>
	 * Unless required by applicable law or agreed to in writing,<br>
	 * software distributed under the License is distributed on an "AS IS" BASIS, <br>
	 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. <br>
	 * See the License for the specific language governing permissions and <br>
	 * limitations under the License.
	 * <p>
	 * Initial code contributed and copyrighted by<br>
	 * ${date} by YOURORGANIZATION, https://www.yourorganization.com
	 * <p>
	 **/
	 
!!! note
	Only code published under the Apache 2.0 license is accepted in the project.

	 
## Commit

- When preparing the commit some formatting and code documentation tasks have to be done. 
- Check if code documentation is correct, document method arguments, behavior of null values etc.
- Don‘t document the obvious, document what is special or might be missleading. Leave references to Jira issues when usefull
- Always add a class description that explains what this is good for
- Add package description for entire modules, add the data model graphic, and other documentation you have there
- Rather delete wrong comments and commit without comment than letting wrong comments in files! 
- Always format using the project formatting rules
- Always run „organize imports“ on classes you modified
- Check all remaining TODO and FIXME markers. TODO and FIXME markers are only allowed for intermediate checkins
- At the end of the development things are either implemented or not, TODO and FIXME‘s are not help full at this point anymore. Convert them to new Jira issues if you really feel this should be implemented later
- Check all warnings and solve them e.g. use annotations 
- Before committing, the commit set must be reviewed carefully to ensure all necessary files are in the commit. 
- In the compare view the made changes shall be quickly reviewed. 
- Every code commit must have a Jira issue reference and a meaningful technical comment what this commit is about. In the Jira worklog the made comment should be non-technical. 
	 
