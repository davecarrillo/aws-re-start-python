import json

def read_json_file(file_name):
    data = ""
    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data