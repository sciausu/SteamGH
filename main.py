import os
from steam_web_api import Steam
from howlongtobeatpy import HowLongToBeat

from dotenv import load_dotenv
load_dotenv()

# modify / create a .env file and add associated values
steamID = os.getenv("STEAM_ID")
key = os.getenv("STEAM_API_KEY")

print("API key: ", key) 
print("Steam ID: ", steamID)

steam = Steam(key)


tmpSearch = "Kingdom Come: Deliverance"
game = HowLongToBeat().search(tmpSearch)
if game is not None and len(game) > 0:
    best_element = max(game, key=lambda element: element.similarity)
    
print("Main Story:", best_element.main_story) # returns float, round for final build
print("Main + Extras:", best_element.main_extra)
print("Completionist:", best_element.completionist)

# arguments: steamid
#user = steam.users.get_owned_games(steamID)


# def main():

#     if __name__ == "__main__":
#         main()