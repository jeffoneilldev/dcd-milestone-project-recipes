# Data Centric Development Milestone Project
For my DCD Milestone Project, I have created an application to access meal recipes called “World of Recipes”.  
When prompted by the user, the app retrieves the selected recipe from a database and displays the information to the user.

## UX
I wanted my app to have a colourful and modern appearance.  To have an intuitive interface and present the information clearly in desktop as it does in mobile devices.
A typical user of this app would be looking for the following: 

### User stories

1. **A person not used to using apps** will need a simple interface for them to navigate.  They will need to know immediately what options are available to them and what the app has to offer.
2. **As a novice in the kitchen,** this user would be looking for all of the details needed to cook a meal, including ingredients and cooking procedure.
3. **A regular user of the app** will want priority and easy access to all the recipes available in the app.  They will want the ability to add their own recipes to the app or edit or delete recipes from the app.
4. **A cook looking for recipe ideas** to suit say, vegetarians who like Chinese food, will want the ability to filter through the list of recipes according to their selections.

### Mock-ups and Database Schema
The mock-up I used for planning the application are in my images folder under the names **mockUpPage1.jpeg** and **mockUpPage2.jpeg**

My database schema can be found in the "database-schema" folder as **dbschema.png**.  I created my database in MongoDB Atlas. For each recipe in my "recipe" collection I had the following fields: recipe_name, cuisine, suitable_for, author, ingredients, procedure and image. Each recipe has it's own ID in the first row.  In my "Addrecipe" and "Editrecipe" forms I needed another collection called "search_recipes" with two entries, suitable_for: "Vegetarian" and suitable_for: "Meat eaters" so the user can select the relevant one for the form.

### Page template appearance
In the top section of every page I have a navigation bar with page destinations available to the user.  A background image associated with recipes stretches halfway down the page with the name of the app across it and a search bar underneath.  This image is very colourful and brightens up the page.  Then there is a footer with copyright details. 

This layout is fully responsive on mobile, medium and large screens.

## Features
### Existing Features
- **Nav bar**: provides page selections on every page for easy navigation.
- **Home (Username Login)**: First landing on the app I give a brief introduction about what the app is about.  I have a "username login" facility which (when wired up) will allow the signed in user to access all the facilities of the app.
- **Recipes (Buttons / Filters)**: Allows the user to browse all the recipes available on the app in a list with the name, image and brief description of each recipe and a button to click on for further information. At the top of the recipes page, there is an option to filter the recipes into vegetarian or meaty or a choice of cuisines.  A combination of these will return the correct result.  When a recipe is selected, full details (author, ingredients, image and procedure) are revealed in a new page with an option to edit or delete the selected recipe. If the user decides to "Edit" the recipe, then the user is brought to a pre-filled form where they can edit the details of the recipe. This edited version will be updated in the app. Also, if the user decided to "Delete" the recipe, the recipe will be deleted from the app.
- **Add Recipe (Form / Button)**: Allows the user to add their own recipe to the app by entering their details into a form and selecting the "Add Recipe" button. Next time they browse the recipes they will find their own recipe there also.
- **Edit Recipe (Form / Button)**: Allows the user to edit a recipe and update it in the database.  Whatever recipe is selected for editing, the user is brought to a page displaying a pre-populated form ready for editing.
- **Search Bar**: Retrieves the recipe according to th inputted text.
- **Footer**: Displays the copyright of the app on every page.

### Features Left to Implement
- Password authentication for a working sign in form to allow access to the app.
- add a "like" voting system for each recipe.
- pagination for long lists of recipes.

## Technologies Used
- Flask: a Python web framework for building this app.
- Javascript: For interactions   
- Bootstrap (getbootstrap.com): For layout, theme and grid system.
- MongoDB databases.
- HTML & CSS for template creation

## Testing
### Code Validation
- HTML was validated using W3C Markup Validation Service.  I got a recurring error saying that "{" is not allowed in my 'url_for' lines. Also, the validator recommended I put in a DOCTYPE, <head> and <title> into my templates, but these are inherited from my base.html already, leaving only the block content for each template.  So, after much advice, I decided to leave them in as they are necessary for my code to work.
- CSS was validated using Jigsaw with no errors found.
- JavaScript was validated using JSHint.

**Testing as per user stories above:**

- **User story 1:**  Landing on the "Home" page for the first time, the inexperienced user can navigate the page easily because of the simple layout and obvious options available.
- **User story 2:**  The novice in the kitchen will find the ingredients and full cooking procedure to whatever recipe they select.
- **User story 3:**  The regular user can sign in to the app for full access to it's features, including adding their own recipes, editing current recipes or deleting any recipe from the app.
- **User story 4:**  The chef looking for recipe ideas can filter their selections by selecting a cuisine type and/or vegetarian or meaty recipes.  The result of their selection will appear on screen and if they want to see the full details of their selected recipe, they can select the "View Recipe" button.

**Other Testing...**

- All buttons and links have been tested and they all go to their desired destinations.
- The "Username Log in" was fully tested to show it will not submit a blank input (the user is shown what input is required).  When the user enters their username, they will be brought to the recipes page.  Password authentication will be introduced at a later stage. 
- Form testing was fully tested resulting in: "Add recipe" and "Edit recipe" forms must be fully filled before submission.  No blank forms will be accepted.  I used "required" on each input line to assure this.  I placed a default image in the image URL input line in case the user does not have an image to input.  On submission, the recipe is added to the recipes list. 
- Responsiveness testing on desktop, tablet and mobile devices showed appropriate app layout on each.
- Python debugger for function testing in the console: when trying to figure out what was being inputted and retrieved to and from my functions I used print() etc
- Testing on the search bar showed that whatever text is entered, it will retrieve a recipe from partial matches and the search is also case-insensitive.  Working perfectly.

## Deployment
This app was developed in AWS Cloud 9.  I used git version control and kept all records of my app in my Github repository.  Before deploying, I made sure to switch my **debug** value to **False** in app.py.

I took the following steps to deploy my project using **Heroku**:
- Logged in and created a new app called **recipes-jeffoneill**
- I synced my Heroku app with my Github repository for full version control. (I took the **heroku git:remote** code from Heroku and put it in my terminal)
- I created a **requirements.txt** file to show Heroku what technologies are used to run my app.
- I created a **Procfile** to show Heroku how to run my app.
- In Heroku, Settings, Config Vars, I created **IP 0.0.0.0** and **PORT 5000** because I need these environment variables in my app.py file.
- In my terminal I put **git push heroku master** then **heroku ps:scale web=1**

Here is the live link to my "recipes" heroku app,  **https://recipes-jeffoneill.herokuapp.com/**

## Credits
### Content
Bootstrap "Clean Blog" Theme

### Media
Recipe images from **www.spendwithpennies.com, vikalinka.com, healthynibblesandbits.com, shop.countdown.co.nz, www.tasteofhome.com, www.errenskitchen.com**
Background image from **www.theloop.ca**
To create my database scema, I used **dbdiagram.io**

### Acknowledgements
w3schools.com  
Bootstrap docs
Mongo docs
stackoverflow.com
Slack  
Code institute tutorials and Tutor support.  
My code institute mentor **Maranatha Ilesanmi** for advice throughout the project.