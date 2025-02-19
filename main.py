import os
from steam_web_api import Steam
from howlongtobeatpy import HowLongToBeat

from dotenv import load_dotenv

def gameHourCheck(gameTitle):
    # tmpSearch = "Kingdom Come: Deliverance"
    # game = HowLongToBeat().search(tmpSearch)
    # if game is not None and len(game) > 0:
    #     best_element = max(game, key=lambda element: element.similarity)
        
    # print("Main Story:", best_element.main_story) # returns float, round for final build
    # print("Main + Extras:", best_element.main_extra)
    # print("Completionist:", best_element.completionist)

    #error from killing floor mod: defense alliance since it doesnt exist in hltb
    tmpSearch = gameTitle
    game = HowLongToBeat().search(tmpSearch)

    if game is not None and len(game) > 0:
        best_element = max(game, key=lambda element: element.similarity)
        return  tmpSearch+":","Main Story:", best_element.main_story, "Main + Extras:", best_element.main_extra, "Completionist:", best_element.completionist
    else:
        return ""
    print("Main Story:", best_element.main_story) # returns float, round for final build
    print("Main + Extras:", best_element.main_extra)
    print("Completionist:", best_element.completionist)



def main():

    load_dotenv()

    # modify / create a .env file and add associated values
    steamID = os.getenv("STEAM_ID")
    key = os.getenv("STEAM_API_KEY")

    print("API key: ", key) 
    print("Steam ID: ", steamID)

    steam = Steam(key)

    
    user = steam.users.get_owned_games(steamID)
    #print(user)
    print(user["game_count"]) #prints number of owned games
    
    for i in range(0,user["game_count"]):
        gameTitle = user["games"][i]["name"]
        print(gameHourCheck(gameTitle))
        print(str(i+1)+" / "+str(user["game_count"]))
        #print(user["games"][i]["name"])


if __name__ == "__main__":
    main()
#ran at 6:46, completed run at 6:52, 6 min runtime
# 560 games = 0.64s per hltb api search
