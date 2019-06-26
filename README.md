# Data Centric Development Milestone Project
For my DCD Milestone Project, I am creating an application to access recipes called “Around the world recipes”.  
The app will retrieve data from a database when prompted by the user. The information will then be displayed to the user.

## UX
A typical user of this app would be looking for the following: 

1. A pleasant, easy to follow user interface that is not too complicated.  
2. Immediately know the options available to them.  
3. Have easy access to all the recipes available through the app.
4. Be able to add their own recipe to the app.  
5. Search the app for a recipe according to their preferred selections.

The mock-up I used for planning the application is a file in my project under the name recipesMockUp.jpeg

In the top section I have a navigation bar with all selections available to the user and a relevant background image associated with recipes stretching down the page.  Underneath I give a brief introduction and a static "Sign in" form to display the possibility of adding extra security to the app. 

This layout is fully responsive on mobile, medium and large screens.


## Features
### Existing Features
- All Recipes: Allows the user to browse all the recipes available on the app. When a recipe is selected, full details (author, ingredients, image and procedure) are revealed with an option to edit or delete the selected recipe. If the user decides to "Edit" the recipe, then the user is brought to a pre-filled form where they can edit the details of the recipe. This edited version will be updated in the app. Also, if the user decided to "Delete" the recipe, the recipe will be deleted from the app.
- Add Recipe: Allows the user to add their own recipe to the app by entering their details into a form and selecting the "Add Recipe" button. Next time they browse the recipes they will find their own recipe there also.
- Search Recipes: Allows the user to search the recipe by entering text to an input box... When any of these extra options are selected, the user is brought to a page showing the recipes relevant to their selection.

### Features Left to Implement
- a "recipes amount" counter.
- a working sign in form to allow access to the app.

## Technologies Used
Flask: a Python web framework for building this app.
Materialize: Accordion effect on recipe descriptions;  collapsible headers
Javascript: For interaction   
Bootstrap (getbootstrap.com): For the layout and theme.
MongoDB databases.

## Testing
As per my primary targets above:

1. A regular user can easily access any recipe from the database through this app.
2. A new user can navigate the page easily because of the simple layout and obvious options available.

Other Testing...

- HTML and CSS code was validated through the relevant validators.

## Deployment
I deployed my project using Heroku...Here is the live link to my "recipes" app 
## Credits
### Content
Recipe images from Google.

### Media
Header and Footer images created by me using Affinity Designer Pro on Mac.

### Acknowledgements
Code institute tutorials.  
w3schools.com  
Slack  
stackoverflow.com
