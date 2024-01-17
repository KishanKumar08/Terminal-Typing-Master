import json

def username_exists_or_not(username,json_file="leaderboard.json"):

    try:
        with open(json_file,"r") as f:
            Leaderboard = json.load(f)
    
    except FileNotFoundError: #To handle the Error of empty file
        Leaderboard = {}

    if username in Leaderboard:
        return True
    else:
        return False

username_exists_or_not("kishan2")