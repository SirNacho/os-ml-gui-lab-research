#This is related to functions that uses the json files to search for stuff.

import json

def list_all(path):
    with open(path, 'r') as file:
        data = json.load(file)

    return data

def search_value_in_json_files(path, key):
    with open(path, 'r') as file:
        data = json.load(file)

    for item in data:
        if item[key] != None:
            return item[key]
    else:
        print("No key found.")
def search_keys_in_json_files(path, name, search_term):
    with open(path, 'r') as file:
        data = json.load(file)

    for item in data:
        if item["name"] == name:
            return item[search_term]
        else:
            print("No key found.")

def replace_value_in_json_files(path, key, value):
    with open(path, 'r') as file:
        data = json.load(file)

    count = 1
    for item in data:
        try:
            if item[key] != None:
                item[key] = value
        except:
            print(f"No keys, {key}, found on Dictionary {count}.")
        count += 1

    write_json_files(data, path)



def write_json_files(userData: list[dict], path):
    with open(path, 'w') as file:
        json.dump(userData, file, indent=4)