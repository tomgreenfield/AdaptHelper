# Adapt Helper

This is a Sublime Text package to help with the population of content in the [Adapt Framework](https://github.com/adaptlearning/adapt_framework).

## Installation

Note: you must have [Package Control](https://sublime.wbond.net/installation) installed before following these steps.

1. In Sublime Text, open the Command Palette by clicking *Tools > Command Palette…* or by pressing <kbd>Ctrl</kbd>+<kbd>⇧ Shift</kbd>+<kbd>P</kbd>.
2. Type `add repo` and select *Package Control: Add Repository*.
3. Type `https://github.com/tomgreenfield/AdaptHelper` and press <kbd>↵ Enter</kbd>.
4. Open the Command Palette again, type `install` and select *Package Control: Install Package*.
5. Select *AdaptHelper* from the list that appears to install the package.

## Usage

### Snippets

The easiest way to insert snippets is by using triggers.

For example, type `hotgraphic` then press <kbd>Tab ↹</kbd> to insert a hot graphic component.

These snippets are only programmed to trigger in JSON files. To see a list of all snippets and their triggers, open the Command Palette and type `snippet`.

This package includes snippets for

* Course
* Content Object
* Article
* Block
* Core-bundled components:
 * Accordion
 * Assessment Results
 * Blank
 * GMCQ
 * Graphic
 * Hot Graphic
 * Matching
 * MCQ (four variations)
 * Media
 * Narrative
 * Slider
 * Text
 * Text Input
* Core-bundled extensions:
 * Assessment
 * Bookmarking
 * Resources
 * Trickle
* Start Controller

### Commands

Note: the following has only been tested on Windows. Requires [Node.js](http://nodejs.org) and [Grunt](http://gruntjs.com/getting-started)/[Gulp](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)/[Rub](https://github.com/cgkineo/adapt-buildkit-rub) to be installed.

#### Grunt

With this package you can run Grunt commands inside Sublime Text.

From the side bar, right-click and select *Grunt Here…* on a folder containing a Gruntfile and a node_modules sub-folder.

You can either type some parameters e.g. `build` or `dev`, or just press <kbd>↵ Enter</kbd> to run the default Grunt command.

#### Gulp

Similar to the Grunt command, you can select *Gulp Here…* on a folder containing a gulpfile and a node_modules sub-folder.

#### Rub

To use the native buildkit Rub, select *Rub Here…* on a folder containing a rub batch file and a buildkit/node_modules sub-folder.

#### Other

You can also run other commands e.g. `npm install` by selecting *Run Command Here…* from a folder’s context menu.

#### Redo

To redo the most recently run command, right-click the main content area or output panel and select *Redo "&lt;command&gt;"*.

#### Cancel

To kill a running command, right-click the side bar or output panel and select *Cancel Running Task*.

If the output panel becomes hidden, you can show it again from *Tools > Build Results > Show Build Results*.