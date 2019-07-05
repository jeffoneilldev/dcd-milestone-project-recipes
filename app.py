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


# to get the search bar input and find the recipe
@app.route('/find_recipe', methods=['GET', 'POST'])
def find_recipe():
    searchitem = request.args.get('searchitem')

    if request.method == 'POST':
        search_results = request.form.to_dict()
        
        if search_results:
            mongo.db.recipe.createIndex( { "$**": "text" } )
            mongo.db.recipe.find( { "$text": { "$search": searchitem } } )

    return render_template('recipe.html', searchitem=searchitem)

# search bar
@app.route('/searchbar_item', methods=['GET','POST'])
def searchbar_item():

    # get search item and redirect to find_recipe route
    searchitem = request.form['search']
    return redirect(url_for('find_recipe', searchitem=searchitem))



"""testing more search options
@app.route('/find_recipe', methods=['POST', 'GET'])
def find_recipe():
    searchitem = request.form.get('search')
    print(searchitem)
    recipe_name=mongo.db.recipe.recipe_name
    cuisine = mongo.db.recipe.cuisine
    author = mongo.db.recipe.author
    suitable_for = mongo.db.recipe.suitable_for
    
    mongo.db.recipe.createIndex( { recipe_name: "text", cuisine: "text", author: "text", suitable_for: "text" } )

    searchresult = mongo.db.recipe.find( { "$text": { "$search": searchitem } } )
    
    return render_template('recipe.html', searchresult=searchresult)
"""
"""
mongo.db.recipe.insert(
   [
     { recipe_name: "Pasta Bake", cuisine: "Italian", author: "Paolo DiCanio", suitable_for: "Vegetarian" },
     { recipe_name: "Spaghetti Bolognese", cuisine: "Italian", author: "Paolo DiCanio", suitable_for: "Meat eaters" },
     { recipe_name: "Irish Stew", cuisine: "Irish", author: "Kitty O'Grady", suitable_for: "Meat eaters" },
     { recipe_name: "Jacket Potatoes", cuisine: "Irish", author: "Kitty O'Grady", suitable_for: "Vegetarian" },
     { recipe_name: "Chow Mein", cuisine: "Chinese", author: "Kim Sang", suitable_for: "Vegetarian" },
     { recipe_name: "Chicken Curry", cuisine: "Chinese", author: "Kim Sang", suitable_for: "Meat eaters" }
   ]
)
"""
"""
recipe = mongo.db.recipe
    recipe_name = mongo.db.recipe.recipe_name
    cuisine = mongo.db.recipe.cuisine
    author = mongo.db.recipe.author
    suitable_for = mongo.db.recipe.suitable_for
"""


"""search route for search bar and radio buttons filter
@app.route('/find_recipe', methods=['POST', 'GET'])
def find_recipe():
   recipe_id=request.args.get('search')
   
   searchresult =  mongo.db.recipe.find_one({"search": ObjectId()})

   print(recipe_id)
   return render_template('recipe.html', searchresult=searchresult)
"""


"""
@app.route('/find_recipe', methods=['POST', 'GET'])
def find_recipe():
    recipesearch = request.form.to_dict('search')
    recipe = mongo.db.recipe
    
    searchresult = list(recipe.find_one())
    for result in searchresult:
        
        print(recipesearch)
    return render_template('recipe.html', result=result)
"""

    
"""
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
