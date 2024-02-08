import sys
import json
path ="config/config.json"

# doing it the function way 

def load_json(path):
    with open(path,"r") as config_file:
        config =json.load(config_file) 
        return config



config = load_json(path)

BOT_TOKEN = config["bot_token"]
DB_PATH = config["db_path"]
ADMINS = config["admins"]


## LATER INCLUDE except filenotfound error...
