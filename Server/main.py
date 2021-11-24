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
        tmp = {
            "name":data["name"],
            "token":str(id_generator())
        }
        dat["players"].append(tmp)
        with open("dat.json", "w") as f:
            f.write(json.dumps(dat, indent=4))
            f.close()
        return (dat)
        



    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()