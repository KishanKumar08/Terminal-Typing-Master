import json

def update_leaderboard(username,wpm,json_file="leaderboard.json"):

    try:
        with open(json_file,"r") as f:
            leaderboard = json.load(f)
    
    except FileNotFoundError: #To handle the Error of empty file
        leaderboard = {}


    #update leaderboard

    if username in leaderboard:
        print("The Username is already exists.")
    else:
        leaderboard[username] = wpm


    # leaderboard(python dictionary) --> json (dump)

    with open(json_file,"w") as f:
        json.dump(leaderboard,f)


update_leaderboard("kishan kumar",26.8)