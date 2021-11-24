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
    print(json.loads(response.text))
    input("END>>>")


class game():
    def play(player_data):
        pass


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

if __name__ == "__main__":
    main()