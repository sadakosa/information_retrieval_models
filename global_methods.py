


import yaml
def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

import pickle
def save_bm25(bm25, file_path):
    file_path = './resources/bm25/' + file_path + '.pkl'
    with open(file_path, 'wb') as f:
        pickle.dump(bm25, f)

def load_bm25(file_path):
    file_path = './resources/bm25/' + file_path + '.pkl'
    with open(file_path, 'rb') as f:
        bm25 = pickle.load(f)
    return bm25

# ====================================================================================================
# Save to Json Functions
# ====================================================================================================
import json
import os

def save_to_json(data, file_name, folder_name):

    # e.g. file_path = './resources/tokenised_text/tokenised_scientific.json'
    file_path = './resources/' + folder_name + '/' + file_name + '.json'

    with open(file_path, 'w') as f:
        json.dump(data, f)

def load_json(file_name):
    file_path = './resources/' + file_name + '.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    else:
        return None

# ====================================================================================================
# Old Functions
# ====================================================================================================

# def get_text_from_file(file_path): 
#     with open(file_path, 'r') as file:
#         # Read the entire content of the file
#         content = file.read()

#     return content

# import csv
# def get_search_terms():
#     csv_file_path = 'search_terms.csv'
#     search_terms = []

#     with open(csv_file_path, mode='r') as file: # open the csv file, read
#         # Create a CSV reader object
#         csv_reader = csv.reader(file)
        
#         # Iterate over each row in the CSV file
#         for row in csv_reader:
#             # Append each row to the data array
#             search_terms.append(row)
#     return search_terms