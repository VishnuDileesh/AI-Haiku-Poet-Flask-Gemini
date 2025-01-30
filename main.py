from flask import Flask, jsonify, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

import os 

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/generate-haiku", methods=['POST'])
def generate_haiku():
    theme = request.form.get('theme', None)

    response = model.generate_content(f"You are an expert haiku poet who is in love with nature. Write me a haiku about {theme}")
    return jsonify({"haiku": response.text})




if __name__ == '__main__':
    app.run(debug=True)
