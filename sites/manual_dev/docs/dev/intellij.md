# IntelliJ

## Basic Setup

## Code Style

### Java Imports

#### Never Use Wildcard Imports

We want imports to be explicit and complete. For this reason, we avoid wildcard imports such as 

```import java.util.*;```

Go to _Preferences → Editor → Code Style → Java_ and select the tab _Imports_ in the content area.

Check the field _Use single class import_ and set the _Class count to use import with '\*'_ to 9999.
Also set _Names count to use static import with '\*'_ to 9999:

![](assets/intellij_imports_single_class_and_wildcards.png){ class="lightbox lightbox-xl" title="No IntelliJ Wildcard Imports" }

If we now tell IntelliJ to
_Optimize Imports_, IntelliJ will never replace imports of classes from the same package
with a wildcard.

#### Import Layout

We want all Java source files to sort imports so that static imports are at the top, 
followed by **java** classes, **javax** classes, and all other classes.

Go to _Preferences → Editor → Code Style → Java_ and select the tab _Imports_ in the content area.

Scroll down to _Import Layout_. Use the up and down arrows to arrange the imports, resulting in
the following layout:

![](assets/intellij_java_import_layout.png){ class="lightbox lightbox-xl" title="IntelliJ Import Layout" }

With this setting, the static imports come first, followed by the imports of the **java** classes, 
the **javax** classes, and all other classes.
