import json

def update_leaderboard(username,wpm,json_file="leaderboard.json"):

    try:
        with open(json_file,"r") as f:
            leaderboard = json.load(f)
    
    except FileNotFoundError: #To handle the Error of empty file
        leaderboard = {}



    leaderboard[username] = wpm

    #sort_leaderboard
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    # leaderboard(python dictionary) --> json (dump)

    with open(json_file,"w") as f:
        json.dump(leaderboard,f)


update_leaderboard("kishan kumar",26.8)