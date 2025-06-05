import os, csv, threading, time
from steam_web_api import Steam
from howlongtobeatpy import HowLongToBeat

from dotenv import load_dotenv
csvInfo = []
def gameHourCheck(games):
    # tmpSearch = "Kingdom Come: Deliverance"
    # game = HowLongToBeat().search(tmpSearch)
    # if game is not None and len(game) > 0:
    #     best_element = max(game, key=lambda element: element.similarity)
        
    # print("Main Story:", best_element.main_story) # returns float, round for final build
    # print("Main + Extras:", best_element.main_extra)
    # print("Completionist:", best_element.completionist)

    #error from killing floor mod: defense alliance since it doesnt exist in hltb
    for i in range(0, len(games)):
        tmpSearch = games[i]
        game = HowLongToBeat().search(tmpSearch)
        print(tmpSearch)
        if game is not None and len(game) > 0:
            best_element = max(game, key=lambda element: element.similarity)
            csvInfo.append([tmpSearch, best_element.main_story, best_element.main_extra, best_element.completionist])
            #return  [tmpSearch+":","Main Story:", best_element.main_story, "Main + Extras:", best_element.main_extra, "Completionist:", best_element.completionist]
        time.sleep(0.01)
        #else:
            #return ""
    #print("Main Story:", best_element.main_story) # returns float, round for final build
    #print("Main + Extras:", best_element.main_extra)
    #print("Completionist:", best_element.completionist)



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
    

    spl1 = []
    spl2 = []
    spl3 = []
    spl4 = []
    spl5 = []
    spl6 = []
    spl7 = []
    spl8 = []
    spl9 = []
    spl10 = []
    inc = 0
    for i in range(0,user["game_count"]):
        if inc % 8 == 0:
            spl1.append(user["games"][i]["name"])
        elif inc % 8 == 1:
            spl2.append(user["games"][i]["name"])
        elif inc % 8 == 2:
            spl3.append(user["games"][i]["name"])
        elif inc % 8 == 3:
            spl4.append(user["games"][i]["name"])
        elif inc % 8 == 4:
            spl5.append(user["games"][i]["name"])
        elif inc % 8 == 5:
            spl6.append(user["games"][i]["name"])
        elif inc % 8 == 6:
            spl7.append(user["games"][i]["name"])
        elif inc % 8 == 7:
            spl8.append(user["games"][i]["name"])
        i+=1
    print(len(spl1)+len(spl2)+len(spl3)+len(spl4)+len(spl5))
    '''
    for i in range(0,user["game_count"]):
        gameTitle = user["games"][i]["name"]
        print(gameHourCheck(gameTitle))
        tmp = gameHourCheck(gameTitle)
        if tmp != "":
            csvInfo.append(tmp)
        print(str(i+1)+" / "+str(user["game_count"]))
        #print(user["games"][i]["name"])
    ''' 
    t1 = threading.Thread(target=gameHourCheck, args=(spl1,))
    t2 = threading.Thread(target=gameHourCheck, args=(spl2,))
    t3 = threading.Thread(target=gameHourCheck, args=(spl3,))
    t4 = threading.Thread(target=gameHourCheck, args=(spl4,))
    t5 = threading.Thread(target=gameHourCheck, args=(spl5,))
    t6 = threading.Thread(target=gameHourCheck, args=(spl6,))
    t7 = threading.Thread(target=gameHourCheck, args=(spl7,))
    t8 = threading.Thread(target=gameHourCheck, args=(spl8,))
 

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
   

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    

    csvInfo.sort(key=lambda x : x[0])
    csvInfo.insert(0, ["Title", "Main Story", "Main + Extras", "Completionist"])
    with open("steamgh.csv", "w", newline='') as newCsvFile:
        writer = csv.writer(newCsvFile)
        writer.writerows(csvInfo)
    print("DONE")

if __name__ == "__main__":
    main()
#ran at 6:46, completed run at 6:52, 6 min runtime
# 560 games = 0.64s per hltb api search
