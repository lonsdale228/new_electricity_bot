from flask import Flask


def flask_start():
    app = Flask(__name__)
    app.config['ENV'] = 'development'

    @app.route("/")
    def login():
        return "Hello World!"

    @app.route("/beba", methods=['POST', 'GET'])
    def success():
        # if not botStateMain["getReq"]:
        # botStateMain.timeLastPOST=getNowTime().timestamp()
        # print("POST Received",botStateMain.timeLastPOST)
        return "this is success"

    app.run(host="0.0.0.0", port=1243)
