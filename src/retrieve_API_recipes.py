import requests # Python package to send get/post requests to a webpage
import os       # Python package to interface with the operating system
from operator import itemgetter
from collections import Counter

def get_recipe_summaries_simple(query_tag, recipe_count, payload, offset = 0):

    """
    The enpoint that allows a cuisine parameter to be specified returns a recipe summary, not the full recipe.
    Storing recipe summary to retreive recipe IDs, which will be fed into a second enpoint that returns full recipes.
    """

    offset_num = str(offset)
    number = str(recipe_count)
    endpoint = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?number=' + number + '&offset=' + offset_num + '&query=' + query_tag

    response = requests.get(endpoint, headers=payload)
    results = response.json()['results']

    recipe_summaries = []
    for recipe_info in results:
        recipe_summaries.append(recipe_info)

    return recipe_summaries

def get_recipe_summaries_complex(cuisine, number, offset, payload):

    """
    The enpoint that allows a cuisine parameter to be specified returns a recipe summary, not the full recipe.
    Storing recipe summary to retreive recipe IDs, which will be fed into a second enpoint that returns full recipes.
    """

    url_start = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex?cuisine='
    url_cuisine = cuisine
    url_middle = '&type=main+course&ranking=2&limitLicense=false&offset='
    offset_num = str(offset)
    number = str(number)
    endpoint = url_start + url_cuisine + url_middle + offset_num + '&number=' + number
    response = requests.get(endpoint, headers=payload)
    results = response.json()['results']
    for recipe_info in results:
        recipe_summaries.append(recipe_info)

def get_recipe_ids(results):
    recipe_ids = []
    for recipe in results:
        recipe_ids.append(str(recipe['id']))

    return recipe_ids

def get_full_recipe_single(recipe_ids, payload):

    error_status_ids = []
    error_counts = Counter()
    full_recipes = []

    for id in recipe_ids:
        endpoint = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/' + id + '/information'
        response = requests.get(endpoint, headers=payload)
        if response.status_code != 200:
            error_status_ids.append((id , response.status_code))
            error_counts[response.status_code] += 1
            continue
        else:
            full_recipes.append(response.text)

    return full_recipes

def get_random_recipes(number, payload):
    '''
    This endpoint pulls the full recipes.
    '''
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=" + str(number)
    response = requests.get(endpoint, headers=payload)
    recipe_text = response.text.replace('},{"vegetarian' , '}$%&->recipe_end<-&%${"vegetarian')
    recipe_json = response.json()['recipes']
    recipe_ids = [recipe['id'] for recipe in recipe_json]

    return recipe_text[12:-2], recipe_ids, response

def write_to_file(recipe_text, recipe_ids, folder_path, recipe_file_name, id_file_name):
    """
    Args:
        recipe_text: String formatted json object containing full recipes.
        folder_path: String. File path of folder containing text document to be updated. DO NOT INCLUDED FILE NAMEself.
        file_name: String. Name of text doc conatined in above folder to update.
    """

    recipe_file_path = folder_path + recipe_file_name
    id_file_path = folder_path + id_file_name
    #recipe_txt = '$%&->recipe_end<-&%$'.join(recipe_lst)
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

    # recipe_summaries = get_recipe_summaries(query_tag = 'cookie', recipe_count = 100 , offset = 100, payload = payload)
    #
    # recipe_ids = get_recipe_ids(recipe_summaries, payload = payload)
    #
    # full_recipes = get_full_recipe_single(recipe_ids, payload = payload)

    folder_path = '/home/katie/01-OneDrive/01_galvanize_dsi/capstones/03-capstone_3/data/'
    text_files = ['cookie_recipes.txt', 'cookie_recipes_2.txt', 'test_append.txt', 'random_recipes.txt', 'recipe_ids.csv']

    #can only pull up to 100 in one call to API
    recipe_text, recipe_ids, response = get_random_recipes(number = 100, payload = payload)
    write_to_file(recipe_text, recipe_ids, folder_path, recipe_file_name = text_files[3], id_file_name = text_files[4])
