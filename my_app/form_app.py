from flask import Flask, render_template, request, jsonify
import pymongo
from pymongo import MongoClient
import pprint
import pandas as pd
import numpy as np
import sys
import pickle


app = Flask(__name__)

all_recs_df = pd.read_pickle('static/recs.pkl')

# def get_recs():
#     recs = []
#     client = MongoClient("localhost", 27017)
#     db = client.recipes
#     collection = db['recs_even_weights']
#     cursor = collection.find({})
#     for document in cursor:
#         recs.append(document['results'])
#     return pd.DataFrame(recs[0])

def generate_preference_selection():
    return pd.Series(['Italian', 'Asian', 'Keto', 'Gluten-Free'])

@app.route('/base_recipes', methods=['GET'])
def generate_base_recipes():
    preference = request.args.get('preference')
    #print(('kt', preference), sys.stderr)
    if preference:
        df = pd.DataFrame([('Italian', 569247, 'Risotto with mushrooms'),('Italian', 505885, 'Chicken Alfredo Roll-ups'),
        ('Italian', 492657, 'Italian Meatloaf'),('Italian', 682815, 'Crockpot Italian Chicken and Broccoli Rabe Chili'),
        ('Italian', 630921, 'Pasta E Fagioli (Pasta and Beans) by Sarah Olsen'),('Italian', 520988, 'Baked Chicken Parmesan Meatballs'),
        ('Italian', 330708, 'The Ultimate Lasagna'),('Italian', 700125, '5 minute Salami Caper Crostini'),
        ('Asian', 486815, 'onion raita , how to make onion raita | pyaaz ka raita'),('Asian', 779158, 'Easy 10 Minute Asian Zucchini Noodles (low-carb, Paleo)'),
        ('Asian', 612070, 'rice pakora | chawal ke pakore'),('Asian', 588541, 'Peach lassi'),
        ('Asian', 560604, 'Sweet and Sour Chicken Lettuce Wraps'),('Asian', 196648, 'Serious Heat: The Quickie Banh Mi'),('Asian', 606906, 'Indian Rice'),
        ('Asian', 953966, 'Shredded Cabbage Salad with Apples and Curry'),('Keto', 779440, 'Porter House Steak with Mushrooms'),
        ('Keto', 513967, 'Kitchen Tip: Perfect Seared Steak with Charred Crust'),('Keto', 623661, 'Southern Breakfast Casserole'),
        ('Keto', 206991, 'Dinner Tonight: Hanger Steak with Shallots and Mushrooms'),('Keto', 972995, 'Chicken Salad Lettuce Wraps'),
        ('Keto', 628125, 'Roasted Cajun Cauliflower and Sausage #MeatballMasters'),('Keto', 411150, 'Omelet Wedges with Cheese Sauce'),
        ('Keto', 541292, 'Taiwanese Hot Pot and Homemade Meatballs'),('Gluten-Free', 506775, 'Slightly Sriracha’d Lamb Mini Meatballs'),
        ('Gluten-Free', 509936, 'Lime Cilantro Sweet Potatoes with Black Beans'),('Gluten-Free', 388526, 'Cowboy Bacon Beans'),
        ('Gluten-Free', 378096, 'Spicy Chicken and Rice'),('Gluten-Free', 779440, 'Porter House Steak with Mushrooms'),
        ('Gluten-Free', 606383, 'Pickled Cherries'),('Gluten-Free', 248349, 'Green Tomato and Jalapeno Jam'),
        ('Gluten-Free', 494115, 'Fish Tacos with Mango Salsa and Cilantro Lime Sauce')])
        df.columns = ['category', 'id', 'title']


        return df.query("category == @preference").to_json(orient = 'records')

@app.route('/', methods=['GET'])
def index():
    """Render a simple splash page."""
    preference_selection_df = generate_preference_selection()
    base_recipes_df = generate_base_recipes()
    return render_template('form/submit.html', base_recipes_df = base_recipes_df, preference_selection_df = preference_selection_df)


@app.route('/recommend', methods=['POST'])
def reccomend():
    """Recieve the recipe to base recommendation off and display recommendations to user.
    """
    selection = str(request.form['recipe'])
    #all_recs_df = get_recs()
    recs_df = all_recs_df[all_recs_df[1] == selection]
    recs_df = recs_df.iloc[:, 2:]
    column_headers = ['Recipe Name', 'Recipe Image', 'Paired Wines', 'Additional Pairing Info', 'Recipe URL']
    return render_template('form/recommend.html', recs_df = recs_df, selection = selection, column_headers = column_headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
