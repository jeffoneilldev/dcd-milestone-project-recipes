import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-xc4tx.mongodb.net/recipes?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html", recipe=mongo.db.recipe.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    search_recipes=mongo.db.search_recipes.find())
    
@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_searches =  mongo.db.search_recipes.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           search_recipes=all_searches)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
