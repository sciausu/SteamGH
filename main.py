import os
from steam_web_api import Steam

from dotenv import load_dotenv
load_dotenv()

# modify / create a .env file and add associated values
steamID = os.getenv("STEAM_ID")
KEY = os.getenv("STEAM_API_KEY")

print("API key: ", KEY)
print("Steam ID: ", steamID)

steam = Steam(KEY)


# arguments: steamid
#user = steam.users.get_owned_games(steamID)