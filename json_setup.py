import os
import re
import json
from nltk import sent_tokenize

def main(remake=False):
    
    if remake==True:
        directory_path = "C:/Users/MCOB PHD 14/Dropbox/Charlie's Dissertation/Beige Books"
        json_data = make_json_data(directory_path)
        dump_json(json_data)
    elif remake==False:
        pass

    with open('output.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def make_json_data(directory_path):
    # Iterate over files in the directory
    json_data = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            # Create a dictionary for the current file
            file_data = {}

            # Read the full text from the file
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                full_text = file.read()

                # Tokenize the full text into sentences
                sentences = sent_tokenize(full_text)

                # Add data to the file dictionary
                file_data['full_text'] = full_text
                file_data['sentences'] = sentences

            # Add file data to the main dictionary
            json_data[filename] = file_data

    return json_data

def dump_json(json_data):
    # Convert the dictionary to JSON format
    json_output = json.dumps(json_data, indent=2)

    # Save the JSON data to a file
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_output)