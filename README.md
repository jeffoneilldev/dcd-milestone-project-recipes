# Data Centric Development Milestone Project
For my DCD Milestone Project, I am creating an application to access recipes called “World of Recipes”.  
The app will retrieve data from a database when prompted by the user. The information will then be displayed to the user.

## UX
A typical user of this app would be looking for the following: 

1. A pleasant, easy to follow user interface that is not too complicated.  
2. Immediately know the options available to them.  
3. Have easy access to all the recipes available through the app.
4. Be able to add their own recipe to the app.  
5. Be able to edit and delete recipes from the app.
5. Search the app for their preferred recipe.

The mock-up I used for planning the application are in my images folder under the names mockUpPage1.jpeg and mockUpPage2.jpeg

In the top section of every page I have a navigation bar with page destinations available to the user.  A background image associated with recipes stretches halfway down the page with the name of the app across it.  This image is very colourful and brightens up the page.  Then there is a footer with copyright details. 

This layout is fully responsive on mobile, medium and large screens.

### Database Schema
I created my database in MongoDB Atlas. For each recipe in my "recipe" collection I had the following fields: recipe_name, cuisine, suitable_for, author, ingredients, procedure and image. Each recipe has it's own ID in the first row. The finalised version of my database schema can be found in the "database-schema" folder, dbschema.jpeg. I have also put a dbfilters.jpeg here showing the reasoning behind the filters i decided to implement.

## Features
### Existing Features
- "Home": First landing on the app I give a brief introduction about what the app is about.  I have a "username login" facility which (when wired up) will allow the signed in user to access all the facilities of the app.  Underneath, for casual browsers, I have a "Quick search" option to allow the user to view what recipes we have to offer.
- "Recipes": Allows the user to browse all the recipes available on the app in a list with the name, image and brief description of each recipe and a button to click on for further information. At the top of the recipes page, there is an option to filter the recipes into vegetarian or meaty or a choice of cuisines.  A combination of these will return the correct result.  When a recipe is selected, full details (author, ingredients, image and procedure) are revealed in a new page with an option to edit or delete the selected recipe. If the user decides to "Edit" the recipe, then the user is brought to a pre-filled form where they can edit the details of the recipe. This edited version will be updated in the app. Also, if the user decided to "Delete" the recipe, the recipe will be deleted from the app.
- "Add Recipe": Allows the user to add their own recipe to the app by entering their details into a form and selecting the "Add Recipe" button. Next time they browse the recipes they will find their own recipe there also.
- "Edit Recipe": Allows the user to edit a recipe and update it in the database.  Whatever recipe is selected for editing, the user is brought to a page displaying a pre-populated form ready for editing.

### Features Left to Implement
- a working sign in form to allow access to the app.
- add a "like" voting system for each recipe.
- pagination for long lists of recipes.

## Technologies Used
Flask: a Python web framework for building this app.
Javascript: For interaction   
Bootstrap (getbootstrap.com): For the layout and theme.
MongoDB databases.
HTML & CSS for template creation

## Testing
As per my primary targets above:

1. A regular user can easily access any recipe from the database through this app. They can easily find a recipe using the "Quick Search" button.
2. A new user can navigate the page easily because of the simple layout and obvious options available.
3. A user can add their own recipes, edit current recipes or delete any recipe from the app.

Other Testing...

- Python debugger
- HTML and CSS code was validated through the relevant validators.

## Deployment
I deployed my project using Heroku...Here is the live link to my "recipes" app 
## Credits
### Content
Bootstrap Theme

### Media
Recipe and Background images from Google.

### Acknowledgements
Code institute tutorials.  
w3schools.com  
Slack  
stackoverflow.com
Bootstrap docs
Mongo docs