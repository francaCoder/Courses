from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask API
# # Create an instance of SQLAlchemy
# # Define the structure of the Post / Author Table

app = Flask(__name__)
app.config["SECRET_KEY"] = "FE$POU#*%@FB"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog2.db"


db = SQLAlchemy(app)
db: SQLAlchemy


# Id_author, name, email, password, admin
class Post(db.Model):
    __tablename__ = "post"
    id_post = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    id_author = db.Column(db.Integer, db.ForeignKey("author.id_author"))


# Id_author, name, email, password, admin, posts
class Author(db.Model):
    __tablename__ = "author"
    id_author = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    admin = db.Column(db.Boolean)
    posts = db.relationship("Post")


def initialize_database():
    # Execute
    db.drop_all()
    db.create_all()

    # ADM's
    author = Author(name="Matheus", email="matheus@hotmail.com", password="123456", admin=True)
    db.session.add(author)
    db.session.commit()

if __name__ == "__main__":
    initialize_database()

