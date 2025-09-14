from flask import Flask, render_template, request, jsonify
import json
import os
from data.cv_data import CV_DATA

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html', data=CV_DATA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

