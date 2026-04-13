from flask import Flask, request, jsonify

app = Flask(__name__)
player_count = 0

@app.route("/update", methods=["POST"])
def update():
    global player_count
    data = request.get_json()
    player_count = data["players"]
    return jsonify({"status": "ok"})

@app.route("/count", methods=["GET"])
def count():
    return jsonify({"players": player_count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
