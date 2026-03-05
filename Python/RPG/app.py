from flask import Flask, jsonify, request

app = Flask(__name__)

hero = {"nom": "Link", "hp": 10, "or": 10}

@app.route('/stats', methods=['GET'])
def voir_stats():
    return jsonify(hero)

# --- NOUVELLE ROUTE : SOIGNER ---
@app.route('/soin', methods=['POST'])
def soigner_hero():
    hero["hp"] = 50
    return jsonify({"message": "Link a été soigné !", "nouveaux_hp": hero["hp"]})

if __name__ == '__main__':
    app.run(debug=True, port=8000)