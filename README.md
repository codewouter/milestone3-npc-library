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

Mockups/wireframes can be viewed within the project structure in /mockups/ms3mockups.pdf or in the [github repository ADDLINK!](????????????)


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

- [JQuery](https://jquery.com)
    - Some Jquery is used by materialize.

- [AmIresponsive](http://ami.responsivedesign.is/#)
    - Used to create Am I responsive picture.

- [Color Picker](https://imagecolorpicker.com/)
    - Used to detrmine gradient color for navbar, based of hero image.


## Testing

### Validation
* The HTML validator returned a lot of errors concerning the jinja elements (eg. Error: Bad value {{ url_for('welcome') }})). These are ignored as they concern Jinja code which is functioning as intended.
* The CSS validator returned no errors.
* The javascript validator returns only errors about undefined variables which are either JQuery selectors, or variables used within functions. The missing semicolons are at places where an embedded function ends.




In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
