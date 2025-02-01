# Haiku Generator

A simple web application that generates nature-themed haikus using Google's Gemini AI model. The application takes a theme as input and creates a beautiful haiku based on that theme, leveraging the power of Gemini 1.5 Flash for creative poetry generation. All generated haikus are stored in a SQLite database for persistence.

## Features

- Web-based interface for easy interaction
- Generates unique nature-themed haikus using Gemini AI
- Fast response times using Gemini 1.5 Flash model
- SQLite database storage for all generated haikus
- Simple and intuitive user experience

## Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd AI-Haiku-Poet-Flask-Gemini
```

2. Install the required dependencies:
```bash
pip install flask
pip install google-generativeai
pip install python-dotenv
pip install flask-sqlalchemy
```

3. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

To start the application, run:

```bash
python main.py
```

The application will be available at `http://localhost:5000`. On first run, it will automatically create the SQLite database file (`haikus.db`).

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter a theme in the input field (e.g., "autumn leaves", "mountain stream", "cherry blossoms")
3. Click the generate button
4. The application will return a unique nature-themed haiku based on your input and store it in the database

## Project Structure

```
haiku-generator/
├── main.py           # Flask application and Gemini AI integration
├── haikus.db         # SQLite database file
├── .env             # Environment variables (API key)
├── README.md        # Project documentation
└── static/          # Static folder
    └── css/
        └── styles.css  
    └── js
        └── script.js
└── templates/       # HTML templates
    └── index.html   # Main web interface
```

## Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE haiku (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    theme VARCHAR(255) NOT NULL
);
```

## Technologies Used

- Flask: Python web framework for serving the application
- Flask-SQLAlchemy: SQL ORM for database management
- SQLite: Lightweight database for storing haikus
- Google Gemini AI 1.5 Flash: Advanced language model for haiku generation
- HTML/CSS/JavaScript: Frontend interface
- python-dotenv: Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to Google's Gemini AI for powering the haiku generation
- Inspired by the beauty of traditional Japanese haiku poetry