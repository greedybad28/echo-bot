import sys
import json
path ="config/config.json"
print(sys.argv[0])

with open(path,"r") as stream:
    config=json.load(stream)

print(config)
BOT_TOKEN = config["bot_token"]
DB_PATH = config["db_path"]
ADMINS = config["admins"]

print(BOT_TOKEN,DB_PATH,ADMINS)

## LATER INCLUDE except filenotfound error...
