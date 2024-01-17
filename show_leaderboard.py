import json
from termcolor import colored

def show_leaderboard():

    # load json file 
    with open("leaderboard.json","r") as file:
        leaderboard = json.load(file)

    #show the leaderboard in terminal
    print()
    print(colored("🏆 LeaderBoard :- 🏆","red"))
    print("--------+++------------")

    rank = 1
    for (username,wpm) in leaderboard.items():
        if rank==1:
            print(colored(f"{rank}. {username} - {wpm:.2f} WPM :- Winner of The Game 🏆","cyan",))
        else:
            print(colored(f"{rank}. {username} - {wpm:.2f} WPM","green"))   
        rank+=1

show_leaderboard()