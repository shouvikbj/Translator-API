from flask import Flask, jsonify, request
import os
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__, static_url_path="")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "thisisasecretkey"
CORS(app, origins="*")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["GET", "POST"])
def default():
    return "<h1 style='text-align:center'>404<h1>"

@app.route("/api", methods=["GET", "POST"])
def default_api():
    return "<h1 style='text-align:center'>404<h1>"

@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.json
    try:
        translator = Translator()
        # detected_language = translator.detect(data["inputText"]).lang
        translation = translator.translate(data["inputText"], dest=data["selectedLanguage"]).text
        res = {
            "status": "ok",
            "translatedText": translation,
            "message": "Successfully translated!"
        }
        return jsonify(res)
    except Exception:
        res = {
            "status": "not-ok",
            "message": "Could not translate!"
        }
        return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)