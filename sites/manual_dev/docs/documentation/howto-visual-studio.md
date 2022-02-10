# How to setup Visual Studio Code

Follow the steps below to checkout and work on the OpenOlat documentation using Visual Studio Code for non-techies. To learn more about the structure and how to test and compile the documentation please refere to [documentation README](index.md).

Make sure you [installed the development environment](index.md#install-dev-envir) first. 

## 1) Install Visual Code Studio 

Download and install the software from the [Visual Code Studio website](https://code.visualstudio.com). It is available for free for [Mac, Windows and Linux](https://code.visualstudio.com/#alt-downloads).

On the Mac the installation is very simple:

	brew install --cask visual-studio-code

## 2) Clone the OpenOlat-docs repository

The public repository is available at the following Git URL: 

	https://github.com/OpenOLAT/OpenOLAT-docs.git

![](assets/vcs-clone.png)

!!! note
	The repository at GitHub is a _read-only_ repository. If you are frentix staff and want to modify the repo, please ask for our interal Git Repo. Ask the Sys-Admin staff how to generate an SSH key to access the repository. 

## 3) Open a page for editing

Use the project explorer to find the page you want to edit. 

![](assets/vcs-edit.png)

!!! tip
	It is best to edit the different language versions at the same time. Additional languages of pages have the same page name and the language code in the file ending. E.g. `index.md` for the English page and `index.de.md` for the German version. 

## 4) Open a local preview

There are two ways of using the Visual Studio Code preview feature: 
1) Side-by-Side
2) In separate tab

Choose which fits better to your workflow / screen size

### Preview Side-by-Side

![](assets/vcs-preview1.png)

![](assets/vcs-preview2.png)

### Preview in separate tab

![](assets/vcs-preview3.png)

## 5) Review changes and commit to repository



!!! attention
	Carefully review all your changes and test them with `python3 -m mkdocs serve` with your browser before you commit and push your changes! You need write permissions on the repository for beeing able to push. 
