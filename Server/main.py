from os import name
from flask import Flask, request, jsonify
import json
import string
import random

def id_generator(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    app = Flask('app')

    @app.route("/")
    def hello():
        return "GAME SERVER WORKING :)"

    @app.route('/ping', methods=["POST"])
    def ping():
        return "Pong"

    @app.route('/join', methods=["POST"])
    def join():
        data = request.json
        dat = json.loads(open("dat.json", "r").read())
        if len(dat["players"]) == 0:
            tmp2 = "master"
        else:
            tmp2 = "player"
        tmp = {
            "name":data["name"],
            "token":str(id_generator()),
            "role":tmp2
        }
        dat["players"].append(tmp)
        with open("dat.json", "w") as f:
            f.write(json.dumps(dat, indent=4))
            f.close()
        return (tmp)
        

    @app.route('/check_game', methods=["POST"])
    def check_game():
        dat = json.loads(open("dat.json", "r").read())
        return str(dat["game"]["on"])


    @app.route("/start_game", methods=["POST"])
    def start_game():
        data = request.json
        dat = json.loads(open("dat.json", "r").read())
        for x in dat["players"]:
            if x["role"] == "master":
                currentMaster = x["token"]
        if data["token"] == currentMaster:
            dat["game"]["on"] = True
            with open("dat.json", "w") as f:
                f.write(json.dumps(dat, indent=4))
                f.close()
            return "True"
        else:
            return "False"


    @app.route('/reset', methods=["POST"])
    def reset():
        dat = json.loads(open("dat.json", "r").read())

        dat["players"] = []
        dat["game"] = {"on": False,"currentP1":"","currentP2":"","wisper":"","awnser":""}

        with open("dat.json", "w") as f:
            f.write(json.dumps(dat, indent=4))
            f.close()

        return ":)"

    @app.route("/get_open_data",methods=["POST"])
    def get_open_data():
        dat = json.loads(open("dat.json", "r").read())
        data = request.json
        work = 0
        for x in dat["players"]:
            if x["token"] == data["token"]:
                work = 1
        if work == 1:
            tmp = {
                "working":True,
                "game":{
                    "on":dat["game"]["on"],
                    "currentP1":dat["game"]["currentP1"],
                    "currentP2":dat["game"]["currentP2"]
                },
                "players":[]
            }
            for x in dat["players"]:
                tmp2 = {
                    "name":x["name"],
                    "role":x["role"]
                    }
                tmp["players"].append(tmp2)
            return tmp
        else:
            return {"working":False,"reason":"Bad Token"}        

    app.run(host='0.0.0.0', port=8080)
        

if __name__ == "__main__":
    main()