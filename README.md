# Adapt Helper

This is an Sublime Text package to help with the population of content in the [Adapt Framework](https://github.com/adaptlearning/adapt_framework).

## Installation

Note: you must have [Package Control](https://sublime.wbond.net/installation) installed before following these steps.

1. In Sublime Text, open the Command Palette by clicking *Tools > Command Palette…* or by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>.
2. Type `add repo` and select *Package Control: Add Repository*.
3. Type `https://github.com/tomgreenfield/AdaptHelper` and press <kbd>↵ Enter</kbd>.
4. Open the Command Palette again, type `install` and select *Package Control: Install Package*.
5. Select *AdaptHelper* from the list that appears to install the package.

## Commands

Note: the following has only been tested on Windows. Requires [Node.js](http://nodejs.org), [Git](http://git-scm.com/) and [Grunt](http://gruntjs.com/getting-started) to be installed.

### Grunt

With this package you may run grunt commands inside Sublime Text. 

From the side bar, right-click and select *Grunt here…* on the folder you wish to grunt.

You may either type some parameters e.g. `build` or `dev`, or just press <kbd>↵ Enter</kbd> to run the default grunt command.

### Other

You may also run other commands e.g. `npm install` by selecting *Run other command here…* from a folder's context menu.

### Cancel

To kill a running command, right-click the side bar or output panel and select *Cancel running task*.

## Snippets

The easiest way to insert snippets is by using triggers.

For example, type `hotgraphic` then press <kbd>Tab ↹</kbd> to insert a hot graphic component.

These snippets are only programmed to trigger in JSON files. To see a list of all snippets and their triggers, open the Command Palette and type `snippet`.

This package includes snippets for

* Course
* Content Object
* Article
* Block
* Components:
 * Accordion
 * Blank
 * GMCQ
 * Graphic
 * Hot Graphic
 * Matching
 * MCQ (three variations)
 * Media
 * Narrative
 * Slider
 * Text
 * Text Input
* Core extensions:
 * Assessment
 * Resources
 * Trickle