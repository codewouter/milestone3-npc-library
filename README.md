**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use. In this document all sources will be credited.**

# Milestone 3 - Dungeons and Dragons NPC Library

The milestone 3 project will be a webpage to showcase content I learned to develop in the third part of the Code Institute's Full stack developer bootcamp. It will be a basic full stack site using HTML/CSS (leaning heavily on Materialize) and especially python, the flask framework and MongoDB. The idea of an NPC library popped into my head whilst thinking about the upcoming vacation where I intend to play some oldschool tabletop DnD.

DnD is short for Dungeons and Dragons and it comprises of a game where a party goes on big adventures. More on this on the [wiki](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons_). These adventures play out mostly in the imagination of the players and especially the story leader called the Dungeon Master. The latter will use a premade adventure but sometimes think it all up him (or her)self). In the fantasy world a lot of non player characters reside, these are the NPS's (which is of course short for Non Player Character). It is hard to keep track of all these entities, so that's where this website comes in. A place where to add, edit, update and if necessary delete non player characters of the world. This way the information can be accessed anyplace anywhere as long as there is a browser and an internet connection!

At this point I will focus this library on DnD 5th edition. This means the library will have the following common DnD statistics for a character:
* Name
* Level
* Race
* Class
* Ability scores for Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
* Description

-------------- am i responive image ! ---------------------

## UX

### User stories:

* As a user I want to be able to view this site on my computer, mobile and tablet.
* As a user I want to see an overview of all NPC's in the database
* As a user I want to be able to see all the statistics of an NPC in one overview.
* As a user I want to be able to create and add a new NPC
* As a user I want to be able to edit an existing NPC
* As a user I want to be able to delete an existing NPC
* As a user I want to be able to add classes to choose from.
* As a user I want to be able to add races to choose from.
* As a user who plays DnD I want to see statistics appropriate for the DnD Realm.

### Planned UX elements

To adhere to all needs of the user the following UI elements are essential to create:
* A landing page where the site is described and explained
* A navigation bar for clear navigation across the site
* An overview (list) of all NPC's in the database.
* A button to add, edit or delete a character.
* A form where a new character can be entered.
* A form where an existing character is displayed and can be adjusted.
* A list of races with an option to remove or add a race.
* A list of classes with an option to remove or add a class.
* Some theme/image to make it abundantly clear that this is a fantasy/DnD setting.

### Database setup

A Mongo database will be used to store all data. Three collections will be needed:
* A collection of NPC's with all statistics.
* A collection of races.
* A collection of classes.

The races and classes will be used repeatedly, therefor they have their own collection which can be added to, edited and deleted. This also makes it possible to have a dropdown box to select a class or race in the NPC form.

### Planned pages of the website

* Home: A landing page with the navbar, hero image and welcome/explanation of the site.
* NPC list: A page with the list of NPC's with the main statistics name, level, race and class. Within this list a character can be selected which leads to the full overview of the NPC. Also on this page should be a button which leads to the create NPC page.
* NPC details: A page with the full overview of the character. Here two buttons should be present. One to delete the character (with an confirmation option) and one to edit the character which leads to the edit NPC page.
* Create NPC: A page to create a new NPC. This will be a form with the same layout as the NPC details page.
* Edit NPC: A page where all statistics can be altered and saved. This will be a form with the same layout as the NPC details page, with all known values displayed.
* Races: A page where all races are listed that can be chosen. Here buttons should be present for every entry to edit or delete. Also a button to create a new race.
* Classes: Like the Races page, but for classes.

### Other

* The navbar will have quicklinks to Home, NPC List, Races and Classes.
* Races and classes will be capitalized, the NPC name will not be, since that is all up to the user and it becomes a matter of taste. Should it be 'Duke Duvel of Moortgat' or Duke Duvel Of Moortgat', etc.
* During development I got the idea to use a form with locked input fields to display all statistics for a character. Then, when the edit button is pressed the form can be re-used with unlocked fields to edit where needed. This way the user will have a very easy time editing the form as the display is identical. The create character page can be copied the same way, but with empty fields (or placeholders). This ensures powerful consistency.

### Mockups

Mockups/wireframes can be viewed within the project structure in /mockups/ms3mockups.pdf or in the [github repository](https://github.com/codewouter/milestone3-npc-library/blob/master/Mockups/ms3mockups.pdf)


## Features

### Existing Features
**Existing features as developed from the list in the UX section**
    
1. A landing page where the site is described and explained
    - A simple welcome text explaining the site's purposes
2. A navigation bar for clear navigation across the site
    - The navigation bar has been created with links to all the implemented pages. For small devices the navbar is collapsed in a hamburgericons which, when clicked, opens a slide-in menu.
3. An overview (list) of all NPC's in the database.
    - The NPC list contains the four basic properties of the NPC; name, level, race and class. Each entry has a 'view' button which will lead to the extended NPC overview.
4. A button to add, edit or delete a character.
    - Add: See entry 5.
    - Edit & delete: See entry 6.
5. A form where a new character can be entered.
    - A new NPC can be created from the navbarlink (create NPC) and by clicking the 'new' button in the header of the NPC List. When the form is filled out the confirm button can be clicked to add the NPC to the database. Pressing the 'x' button, cancels the edit form and returns to the overview of the relevant NPC.
6. A form where an existing character is displayed and can be adjusted.
    - When an NPC is selected from the list using the 'view' button, the full overview of the relevant NPC is opened with two buttons in the header 'Edit' and 'Del'. When the first is pressed, the overview form becomes editable. Pressing the 'Del' button will prompt the user for confirmation, and if agreed, will delete the NPC from the database.
7. A list of races with an option to remove or add a race.
    - A link to the list of created races can be found in the navbar. When an entry is clicked, the description will be openened along with an edit or delete button. To create a new race, the user can press the new button. 
8. A list of classes with an option to remove or add a class.
    - A link to the list of created classes can be found in the navbar. When an entry is clicked, the description will be openened along with an edit or delete button. To create a new class, the user can press the new button. 
9. Some theme/image to make it abundantly clear that this is a fantasy/DnD setting.
    - On all pages a hero image is present which makes it abundantly clear. The background texture is reminiscent of old paper to add to the look and feel. I purposfully left the hero image on big viewport because of the somewhat 'smudged' look because it's a bit lowres. However, I liked it.

### Additional features

* When an action is called to delete an entry (NPC, race, class) a modal will popup to ask for confirmation.
* All lists will be sorted alphabetically.
* Only a name is mandatory to create an NPC. This is to ensure that everything a user is thinking up can be entered, without being forced to add in unnecessary values. Sometimes an awesome name is the only thing needed to store.
* As mentioned earlier. The character's name will not be capitalized on display, nor will it be set in all lowercase when entered in the database. This is to ensure the name stays intact. From my campaigning days I remember several characters with all kinds of upper- and lowercase combinations. (eg. d'Torrax the Magnificent).
* When a wordbreak is necessary, it will be broken at a space whenever possible.

### Features Left to Implement
* More statistics (the DnD charactersheet is huge)
* Option to add a picture of your NPC.
* Race/class stat modifiers which will be applied automatically.

## Technologies Used

* HTML/CSS
    * Mandatory.

* [Materialize](https://materializecss.com/)
    * The frontend of the site has been created making heavy use of materialize.

* [Googlefonts](https://fonts.google.com/) 
    * Googlefonts is being used through Materialize.

* [Balsamiq](https://balsamiq.com/)
    * The mockup wireframes were made using Balsamiq.

* Validators:
    * [HTML](https://validator.w3.org/)
    * [CSS](https://www.w3schools.com/w3css/w3css_validation.asp)
    * [Python](http://pep8online.com/)

- [JQuery](https://jquery.com)
    - Some Jquery is used by materialize.

- [AmIresponsive](http://ami.responsivedesign.is/#)
    - Used to create Am I responsive picture.

- [Color Picker](https://imagecolorpicker.com/)
    - Used to detrmine gradient color for navbar, based of hero image.


## Testing

### Validation
* The HTML validator returned no more errors after debugging and code cleaning. All pages and subpages were loaded and ran through the validator using their URL's.
* The CSS validator returned no errors.
* The Python (PEP8) validator returned no errors after cleaning up the code.

### Test run according to the user stories:

* As a user I want to be able to view this site on my computer, mobile and tablet.
    * All responsiveness was tested using either chrome's devtools or a real device, tested for:
        * Full desktop (real) at 1920x1080
        * Laptop (real) at 1366x768
        * Samsung Galaxy A5 (real) at 1080x1920 and 1920x1080
        * Samsung Galaxy A5 (simulated) at 360x640 and 640x360
        * Ipad (simulated) at 768x1024 and 1024x168
        * General responsiveness using the sliders of Chrome's Devtool.
    * For these tests, characters were created with excessive long or short entries and/or empty fields.

* As a user I want to see an overview of all NPC's in the database
    * The user can use the navigation menu/bar to got to the NPC List where a condensed list is shown with all entries from the database. Per entry the name, level, race and class are shown, if present.
* As a user I want to be able to see all the statistics of an NPC in one overview.
    * The user can select the view button in each entry of the NPC list to navigate to the extended overview of the selected NPC, all values are shown in a clear and comprehensive manner.
* As a user I want to be able to create and add a new NPC
    * From the NPC list through the 'new' button or by selecting 'Create new NPC' from the navbar, the user is taking to the 'New character' form. Here all values can be entered. When the user is satisfied, the form can be submitted through a button, or canceled if necessary.
* As a user I want to be able to edit an existing NPC
    * When a character overview is open concerning a specific NPC, the 'edit' button can be pressed and a form is shown with all data previously entered, ready to be edited. Again a confirm and cancel button is present. 
* As a user I want to be able to delete an existing NPC
    * When a character overview is open concerning a specific NPC, the 'del' button can be pressed and a confirmation dialog will pop up to ask for confirmation. 
* As a user I want to be able to add classes to choose from.
    * Through the menu option 'classes' the user can see all classes present in the database. A 'new' button is present to create a new class. Also, all entries can be easily edited or deleted.
* As a user I want to be able to add races to choose from.
    * Through the menu option 'races' the user can see all races present in the database. A 'new' button is present to create a new race. Also, all entries can be easily edited or deleted.
* As a user who plays DnD I want to see statistics appropriate for the DnD Realm.
    * When the users view an NPC they will see only see statistics that adhere to the Dungeon and Dragons Fifth edition rulebook.

### Further testing
* All links and buttons were tested exensively.
* Tens of characters were created with awkward entries. Empty fields, extremely long names, high and low values. After lots of debug and test cycles, no more errors were found.
* A friend with a lots coding and testing experienced stress-tested the whole project.

### Interesting bugs/errors found and solved during development.
* I branched off early to test if I could combine materialize with my own styling, also branched off to work on the editnpc.html and update_npc route because it seemed complex. After those I decided branches were not needed because I was working solo on this project.
* The hero image got either too high (taking up more than the whole viewport) or too small (just a small strip), depending on the size I entered. Decided to solve this through media queries to size it for specific viewport sizes.
* I had a lot of problems with the table I created to show the NPC List, especially text spilling out of the boundaries of the table. This pushed the who table beyond the width of the rest of the page. After consulting Slack, Eventyret_mentor advised me to drop the table altogether. Seeing I kept fiddling to get it right, I decided to rebuild the list using divs. In the end it was easier and much more controllable.
* Problems arose when activating the delete (del) buttons for classes and races lists. The confirmation modal was build in each iteration.  As I build it with a static id through each iteration while building the list, it was not unique. After consulting tutor support, I used the ._id value from each MongoDB entry as an ID to ensure they are unique. Many thanks to Haley.
* A very interesting problem was encountered when doing some intermediate testing on my phone. While everything worked fine on an simulated Galaxy A5, on my real device I could not make selections in every materialize select-lists (dropboxes). The touchscreen did not respond while selecting an entry in the list. Found a solution through google [here](https://github.com/Dogfalo/materialize/issues/4200).
* Jinja threw a lot of error because it had to capitalize() or lower() non-existing object values. Because I chose to allow empty fields (except name) in the NPC object. The selectboxes for class and race cannot be given a default value like other input-fields. When these fields are left empty, no key-value pair is created in the object. When the object is extracted from the database and entered into a page, the capitalize() method is used. When storing the class and race entries, the lower() method is used. To solve this I created if statements in the relevant functions to create an empty string in case one of the keys did not exist.
* The last big issue was encountered when using the HTML validator which gave two errors that in the input-field for both class and race, two values were selected. This was because of a default (disabled) selection of 'choose race/class' and when present the selection from the NPCObject itself. This was eventually solved after much trial and error and a lot of help from Tim_ci. The default selection of value 'create race'/'create class', is only present when there is no value for race/class in the NPCObject. This is coded through jinja if statements on the editnpc.html page.


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
