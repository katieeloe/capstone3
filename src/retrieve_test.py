import requests # Python package to send get/post requests to a webpage
import os       # Python package to interface with the operating system
import pandas as pd
import csv
import json
from operator import itemgetter
from collections import Counter


def get_random_recipes(number, payload):
    '''
    This endpoint pulls the full recipes.
    '''
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=" + str(number)
    response = requests.get(endpoint, headers=payload)
    recipe_text = response.text.replace('},{"vegetarian' , '}$%&->recipe_end<-&%${"vegetarian')
    recipe_json = response.json()['recipes']
    recipe_ids = [recipe['id'] for recipe in recipe_json]

    return recipe_text[12:-2], recipe_json, recipe_ids, response

def get_current_ids(file_path):

    with open(file_path, 'r') as f:
        current_recipe_ids = csv.reader(f)
        current_recipe_ids = list(current_recipe_ids)[0]
        current_recipe_ids = set([int(id) for id in current_recipe_ids])
    return current_recipe_ids

def remove_duplicate_recipes(current_recipe_ids, recipe_json, recipe_ids):
    for idx, id in enumerate(recipe_ids):
        if id in current_recipe_ids:
            del recipe_json[idx]
            del recipe_ids[idx]
            continue

    recipe_text = json.dumps(recipe_json).replace('}, {"vegetarian' , '}$%&->recipe_end<-&%${"vegetarian')[1:-1]


    return recipe_text, recipe_ids


def write_to_file(recipe_text, recipe_ids, folder_path, recipe_file_name, id_file_name):
    """
    Args:
        recipe_text: String formatted json object containing full recipes.
        folder_path: String. File path of folder containing text document to be updated. DO NOT INCLUDED FILE NAMEself.
        file_name: String. Name of text doc conatined in above folder to update.
    """

    recipe_file_path = folder_path + recipe_file_name
    id_file_path = folder_path + id_file_name

    ids_string = str(recipe_ids)[1:-1]
    with open(recipe_file_path, mode='a') as localfile:

        if os.stat(recipe_file_path).st_size == 0:
            localfile.write(str(recipe_text))
        else:
            localfile.write("$%&->recipe_end<-&%$")
            localfile.write(str(recipe_text))

    with open(id_file_path, mode='a') as localfile:

        if os.stat(id_file_path).st_size == 0:
            localfile.write(str(ids_string))
        else:
            localfile.write(", ")
            localfile.write(str(ids_string))



if __name__ == "__main__":

    API_KEY = os.environ['Spoontacular_API_KEY']
    payload = {'X-RapidAPI-Key': API_KEY}

    folder_path = '/home/katie/01-OneDrive/01_galvanize_dsi/capstones/03-capstone_3/data/'
    text_files = ['random_recipes.txt', 'recipe_ids.csv', 'test_recipes.txt', 'test_ids.txt']

    current_recipe_ids = get_current_ids('/home/katie/01-OneDrive/01_galvanize_dsi/capstones/03-capstone_3/data/recipe_ids.csv')

    #can only pull up to 100 in one call to API
    recipe_text, recipe_json, recipe_ids, response = get_random_recipes(number = 2, payload = payload)
    recipe_text, recipe_ids = remove_duplicate_recipes(current_recipe_ids, recipe_json, recipe_ids)

    write_to_file(recipe_text, recipe_ids, folder_path, recipe_file_name = text_files[0], id_file_name = text_files[1])
