from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/result', methods=['GET'])
def show():
    with open ('result.json', "r") as jf:
        j = json.loads(jf.readline())

    return jsonify(j)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
