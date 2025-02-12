import os
from steam_web_api import Steam

from dotenv import load_dotenv
load_dotenv()

# modify / create a .env file and add associated values
steamID = os.getenv("STEAM_ID")
key = os.getenv("STEAM_API_KEY")

print("API key: ", key)
print("Steam ID: ", steamID)

steam = Steam(key)


# arguments: steamid
#user = steam.users.get_owned_games(steamID)