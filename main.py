from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import google.generativeai as genai
from dotenv import load_dotenv

import os 

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

# Database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haikus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Haiku model
class Haiku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    theme = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Haiku {self.id}>'

# Create the tables in the database
with app.app_context():
    # db.drop_all()  # Drops all tables 
    db.create_all()


# Defining routes
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/generate-haiku", methods=['POST'])
def generate_haiku():
    data = request.get_json()  # Get JSON data from the request
    theme = data.get('theme', None)  # Access the 'theme' key from the JSON data

    response = model.generate_content(f"You are an expert haiku poet who is in love with nature. Write me a haiku about {theme}")

    haiku_text = response.text

    # Save the haiku to the database
    new_haiku = Haiku(text=haiku_text, theme=theme)
    db.session.add(new_haiku)
    db.session.commit()

    return jsonify({"haiku": response.text})




if __name__ == '__main__':
    app.run(debug=True)
