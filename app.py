import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = "our_secret"
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-xc4tx.mongodb.net/recipes?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def recipe_index():
    """to bring the user to the home page"""
    return render_template("index.html", recipe=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    """to bring the user to the add recipe page"""
    return render_template("addrecipe.html",
    search_recipes=mongo.db.search_recipes.find())

   
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """to insert a recipe into the db & bring the user back to the recipes page"""
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('find_recipe'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """to bring the user to the edit recipe page and 
    display the selected recipe form already populated and have it ready for editing"""
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_searches =  mongo.db.search_recipes.find()
    return render_template('editrecipe.html', recipe = the_recipe,
                           search_recipes = all_searches)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """to update changes made to the edited recipe and return the user to the recipes page"""
    recipe = mongo.db.recipe
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine':request.form.get('cuisine'),
        'author': request.form.get('author'),
        'suitable_for': request.form.get('suitable_for'),
        'ingredients':request.form.get('ingredients'),
        'procedure':request.form.get('procedure'),
        'image':request.form.get('image')
    })
    return redirect(url_for('find_recipe'))


@app.route('/find_recipe', methods=['GET', 'POST'])
def find_recipe():
    """to take the input from searches, filters and recipes button and display the result on the recipes page"""
    searchitem = request.form.get('recipe_name') or request.form.get('suitable_for') or request.form.get('cuisine')
    print(searchitem)
    if searchitem:    
        flash("Here are the results of your search...")
        searchitem = request.form.to_dict()
        query = ( { "$text": { "$search": searchitem } } )
        search_results = mongo.db.recipe.find(searchitem)
        return render_template('recipe.html', recipe=search_results, searchitem=searchitem)

    else:
        return render_template("recipe.html", recipe=mongo.db.recipe.find())


@app.route('/show_recipe', methods=['GET', 'POST'])
def show_recipe():
    """to display the selected recipe on a new page with all of the recipe information"""
    searchitem = request.form.get('recipe_name') or request.form.get('suitable_for')
    if searchitem:    
        searchitem = request.form.to_dict()
        query = ( { "$text": { "$search": searchitem } } )
        search_results = mongo.db.recipe.find(searchitem)
        return render_template('showrecipe.html', recipe=search_results, searchitem=searchitem)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """to remove the selected recipe from the list/db"""
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('find_recipe'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
