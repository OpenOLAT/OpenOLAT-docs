
# Design Patterns

Design Patterns are high level not bound to specific components and are best practice solutions for how a user achieves a goal

*ToDo*
- [ ] Define the Navigation between Spaces
- [ ] Define Saving and canceling
  
---

## Navigation Patterns

### Back & Home

1. Clicking onto the logo always brings you to the homepage configured in the settings of your instance or set as your personal preference.
2. If we are in Kiosk mode, for example 

### Navigation between Spaces in OpenOlat

-- Tbd--

## Empty States in OO

Empty states are moments in an app where there is no data to display to the user.

![emptystate](assets/empty_state.jpg)

1. **Image**: A non-interactive image that relates to the situation (optional).
2. **Title**: A short and concise explanation. Should be in positive statement.
3. **Copy / Paragraph** Explain clearly the next action to populate the empty space OR explain why the space is empty and include the next actions or steps to get results. For Example, explaining that you can create groups here in this screen.
4. **Primary Action (optional)** The primary call to action referenced in the copy above.

### Empty Search State Variant

An Empty search results empty state serves as a placeholder when there are no search results after doing a search or filtering results.
It should describe that a search or filter came back with no results and does not contain a Primary or Secondar Action.

### When to use

Empty states always appear in the otherwise empty space, in the context of the data that’s missing. They can occur anywhere your app can display data, including but not limited to dashboards and tables.

When space is limited, use text only.