import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-xc4tx.mongodb.net/recipes?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')


@app.route('/recipe_home')
def recipe_home():
    return render_template("home.html", recipe=mongo.db.recipe.find())
    
@app.route('/find_recipe')
def find_recipe():
    return render_template("searchrecipe.html", recipe=mongo.db.recipe.find())

@app.route('/recipe_meateater')
def recipe_meateater():
    return render_template("meateater.html", meateaters=mongo.db.meateaters.find())

@app.route('/recipe_vegetarian')
def recipe_vegetarian():
    return render_template("vegetarian.html", vegetarian=mongo.db.vegetarian.find())
    
@app.route('/recipe_irish')
def recipe_irish():
    return render_template("irish.html", irish=mongo.db.irish.find())

@app.route('/recipe_italian')
def recipe_italian():
    return render_template("italian.html", italian=mongo.db.italian.find())
    
@app.route('/recipe_chinese')
def recipe_chinese():
    return render_template("chinese.html", chinese=mongo.db.chinese.find())


@app.route('/recipe_kittyogrady')
def recipe_kittyogrady():
    return render_template("kittyogrady.html", kittyogrady=mongo.db.kittyogrady.find())
    
@app.route('/recipe_kimsang')
def recipe_kimsang():
    return render_template("kimsang.html", kimsang=mongo.db.kimsang.find())
    
@app.route('/recipe_paolodicanio')
def recipe_paolodicanio():
    return render_template("paolodicanio.html", paolodicanio=mongo.db.paolodicanio.find())
    


@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html", recipe=mongo.db.recipe.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    search_recipes=mongo.db.search_recipes.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_searches =  mongo.db.search_recipes.find()
    return render_template('editrecipe.html', recipe = the_recipe,
                           search_recipes = all_searches)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine':request.form.get('cuisine'),
        'author': request.form.get('author'),
        'suitable_for': request.form.get('suitable_for'),
        'ingredients':request.form.get('ingredients'),
        'procedure':request.form.get('procedure')
    })
    return redirect(url_for('get_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
