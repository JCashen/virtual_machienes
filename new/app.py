from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Root:Bungle_11@35.242.174.199/game_reviews"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
