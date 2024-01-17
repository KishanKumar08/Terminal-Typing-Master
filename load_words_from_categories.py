import json

def load_words_from_json_function():

    with open("collectionofwords.json","r") as f:
        words = json.load(f)

    return words

load_words_from_json_function()

