from re import L
import requests
import time
import random
import os
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def join(name):
    bundle = {"name":name}
    response = requests.post("http://192.168.86.180:8080/join", json = bundle)
    return (json.loads(response.text))


class game():
    def play(player_data):
        
        cls()
        
        if player_data["role"] == "master":
            input("Press enter to Start Game")
            tmp = {"token":player_data["token"]}
            response = requests.post("http://192.168.86.180:8080/start_game", json=tmp)
            print(response.text)
        else:
            waiting = 1
            run = 0
            while waiting == 1:
                print(f"Waiting for game start ({run})")
                time.sleep(2)
                run += 1
                response = requests.post("http://192.168.86.180:8080/check_game")
                if response.text == "True":
                    waiting = 0
        
        game_on = 1
        while (game_on == 1):
            cls()
            tmp = {"token":player_data["token"]}
            response = requests.post("http://192.168.86.180:8080/get_open_data", json=tmp)
            open_data = json.loads(response.text)
            #print(open_data)
            print("Questioner: %s"%(open_data["game"]["currentP1"]))
            print("Responder: %s"%(open_data["game"]["currentP2"]))
            owner = ""
            players = []
            for z in open_data["players"]:
                if z["role"] == "player":
                    players.append(z["name"])
                elif z["role"] == "master":
                    owner = z["name"]

            print("Game Owner: %s"%(owner))
            print("Players:")
            for x in players:
                print(" - %s"%(x))
            print()
            
            

            input(": ")




def main():
    on = 1
    while on == 1:
        cls()
        print("1) Join Game\n2) Reset Game")
        cmd = input(": ")
        if cmd == "1":
            name = input("Name: ")
            if len(name) > 0:
                player_data = join(name)
                game.play(player_data)
            else:
                print("Your name must be longer than 1 char")
                input("Press enter to continue...")
        if cmd == "2":
            requests.post("http://192.168.86.180:8080/reset")

if __name__ == "__main__":
    main()