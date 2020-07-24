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


## UX

User stories:

* As a user I want to be able to view this site on my computer, mobile and tablet.
* As a user I want to see an overview of all NPC's in the database
* As a user I want to be able to see all the statistics of an NPC in one overview.
* As a user I want to be able to create and add a new NPC
* As a user I want to be able to edit an existing NPC
* As a user I want to be able to delete an existing NPC
* As a user I want to be able to add classes to choose from.
* As a user I want to be able to add races to choose from.
* As a user who plays DnD I want to see statistics appropriate for the DnD Realm.

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

A Mongo database will be used to store all data. Three collections will be needed:
* A collection of NPC's with all statistics.
* A collection of races.
* A collection of classes.

The races and classes will be used repeatedly, therefor they have their own collection which can be added to, edited and deleted. This also makes it possible to have a dropdown box to select a class or race in the NPC form.

The layout of the site will be:
* Home: A landing page with the navbar, hero image and welcome/explanation of the site.
* NPC list: A page with the list of NPC's with the main statistics name, level, race and class. Within this list a character can be selected which leads to the full overview of the NPC. Also on this page should be a button which leads to the create NPC page.
* NPC details: A page with the full overview of the character. Here two buttons should be present. One to delete the character (with an confirmation option) and one to edit the character which leads to the edit NPC page.
* Create NPC: A page to create a new NPC. This will be a form with the same layout as the NPC details page.
* Edit NPC: A page where all statistics can be altered and saved. This will be a form with the same layout as the NPC details page, with all known values displayed.
* Races: A page where all races are listed that can be chosen. Here buttons should be present for every entry to edit or delete. Also a button to create a new race.
* Classes: Like the Races page, but for classes.

Other

* The navbar will have quicklinks to Home, NPC List, Races and Classes.
* Races and classes will be capitalized, the NPC name will not be, since that is all up to the user and it becomes a matter of taste. Should it be 'Duke Duvel of Moortgat' or Duke Duvel Of Moortgat', etc.
* During development I got the idea to use a form with locked input fields to display all statistics for a character. Then, when the edit button is pressed the form can be re-used with unlocked fields to edit where needed. This way the user will have a very easy time editing the form as the display is identical. The create character page can be copied the same way, but with empty fields (or placeholders). This ensures powerful consistency.

### Mockups

Mockups/wireframes can be viewed within the project structure in /mockups/ms3mockups.pdf or in the [github repository](????????????)


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

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
