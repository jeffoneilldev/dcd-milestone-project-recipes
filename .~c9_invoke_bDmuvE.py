import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-xc4tx.mongodb.net/recipes?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')

@app.route('/recipe_index')
def recipe_index():
    return render_template("index.html", recipe=mongo.db.recipe.find())

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
        'procedure':request.form.get('procedure'),
        'image':request.form.get('image')
    })
    return redirect(url_for('get_recipe'))



the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_searches =  mongo.db.search_recipes.find()
    return render_template('editrecipe.html', recipe = the_recipe,
                           search_recipes = all_searches)


"""search route for search bar and radio buttons filter"""
@app.route('/find_recipe', methods=['POST', 'GET'])
def find_recipe():
   
   

    recipesearch = request.form.to_dict
    recipe = mongo.db.recipe
    
    searchresult = list(recipe.find_one())
    for result in searchresult:
        
        print(recipesearch)
    return render_template('recipe.html', result=result)


    
"""testing more search options
@app.route('/find_recipe', methods=['POST', 'GET'])
def find_recipe():
    recipesearch = request.form['search']
    mongo.db.recipe.create_index([('name', 'text')])
    query = ( { "$search": { "$search": recipesearch } } )
    searchresult = mongo.db.recipe.find(query)
    print(recipesearch)
    return render_template('recipe.html', recipesearch=recipesearch, searchresult=searchresult)


@app.route('/find_recipe/<recipe_id>', method=["POST"])
def find_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe_id = request.args.get('recipe_id')   -took this from above example
    recipe.search( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine':request.form.get('cuisine'),
        'author': request.form.get('author'),
        'suitable_for': request.form.get('suitable_for'),
        'ingredients':request.form.get('ingredients'),
        'procedure':request.form.get('procedure'),
        'image':request.form.get('image')
    })
    return render_template('recipe.html', recipe_id=recipe_id)
"""


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
