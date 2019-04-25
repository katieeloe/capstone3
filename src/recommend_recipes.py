import json
import pandas as pd
import numpy as np
from multi_key_dict import multi_key_dict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
from map_features import dummify_features
pd.options.display.max_columns = 500

def open_files(file_path, recipe_file, ids_file):
    recipe_file = open(file_path + recipe_file, 'r')
    ids_file = open(file_path + ids_file, 'r')
    return recipe_file.read(), ids_file.read()


def convert_to_json(recipes_text, ids_text):

    recipe_ids = list(map(lambda x: int(x), ids_text.split(", ")))
    recipes_list = recipes_text.split("$%&->recipe_end<-&%$")
    recipes_json = []
    for recipe in recipes_list:
        recipes_json.append(json.loads(recipe))
    return recipes_json, recipe_ids

def create_feature_lists(recipes_json):
    return dummify_features(recipes_json)

def vectorize_features(categorical_feat):

    feat_strings = []
    for recipe in categorical_feat:
        feat_strings.append(' '.join(recipe))
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(feat_strings)
    features_dense = X.todense()
    features_df = pd.DataFrame(features_dense, columns = vectorizer.get_feature_names())
    return features_df.astype(bool).astype(int)

def compute_distances(features_df):
     return cosine_similarity(features_df)

def find_recommendations(cosine_similarities, recipes_json):
    num_rec = 5
    results = []

    for idx, recipe in enumerate(recipes_json):
        similar_indices = cosine_similarities[idx].argsort()[:-num_rec-2:-1]
        similar_indices = similar_indices[1:]

        for i in similar_indices:
            rec = []
            rec.append(recipe.get('id'))
            rec.append(recipe.get('title'))
            rec.append(recipes_json[i].get('title'))
            rec.append(recipes_json[i].get('image'))
            rec.append(recipes_json[i].get('winePairing').get('pairedWines'))
            rec.append(recipes_json[i].get('winePairing').get('pairingText'))
            rec.append(recipes_json[i].get('sourceUrl'))

            results.append(rec)

    return results

def load_mongo(table_name, results):
    client = MongoClient('localhost', 27017)
    db = client.recipes
    doc_tab = db[table_name]
    post = {'results': results}
    db[table_name].insert_one(post)

if __name__ == "__main__":
    file_path = '/home/katie/01-OneDrive/01_galvanize_dsi/capstones/03-capstone_3/data/'
    recipes_text , ids_text = open_files(file_path, recipe_file = 'random_recipes.txt' , ids_file = 'recipe_ids.csv')
    recipes_json, recipe_ids = convert_to_json(recipes_text, ids_text)
    categorical_feat, unbucketed_ingredients = create_feature_lists(recipes_json)
    features_df = vectorize_features(categorical_feat)
    cosine_similarities = compute_distances(features_df)
    results = find_recommendations(cosine_similarities, recipes_json)
    #load_mongo('recs_even_weights', results)
