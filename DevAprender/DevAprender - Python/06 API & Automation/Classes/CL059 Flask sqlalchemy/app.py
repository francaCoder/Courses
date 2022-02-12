from flask import Flask, jsonify, request, make_response
from structure_database import Author, Post, app, db
import json
import jwt
from datetime import datetime, timedelta
from functools import wraps


def mandatory_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        toke = None
        # Check if it was sent
        if "x-acess-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"Message": "Couldn't find the token."}, 401)

        try:
            result = jwt.decode(token, app.config["SECRET_KEY"])
            author = Author.query.filter_by(id_author=result["id_author"]).first()
        except:
            return jsonify({"Message": "Invalid Token"})
        return f(author, *args, **kwargs)
    return decorated()



@app.route("/login")
def login():
    authorized = request.authorization
    if not authorized or not authorized.username or not authorized.password:
        return make_response("Invalid Login", 401,
                             {"WWW-Authenticate": "Basic realm='Mandatory Login'"})
    user = Author.query.filter_by(name=authorized.username).first()
    if not user:
        return make_response("Invalid Login", 401,
                             {"WWW-Authenticate": "Basic realm='Mandatory Login'"})
    if authorized.password == user.password:
        token = jwt.encode({"id_author": user.id_author, "exp": datetime.utcnow() + timedelta(minutes=30)}, app.config["SECRET_KEY"])
        return jsonify({"token": token.decode("UTF-8")})
    return make_response("Invalid Login", 401,
                         {"WWW-Authenticate": "Basic realm='Mandatory Login'"})


# Default Route - GET http://localhost:5000
@app.rout("/")
@mandatory_token # Now the user needs to have a valid token
def get_posts(author):
    return jsonify(posts)


# Route - GET c/ id http://localhost:5000/posts/1
@app.route("/post/<int:index>", methods=["GET"])
@mandatory_token
def get_post_by_id(author, index):
    return jsonify(posts[index])

# New post - POST http://localhost:5000/post
@app.route("/post", methods=["POST"])
@mandatory_token
def new_post():
    post = request.get_json()
    posts.append(post)

    return jsonify(post, 200)


# Change an existing post - PUT http://localhost:5000/post/2
@app.route("/post/<int:index>", methods=["PUT"])
@mandatory_token
def change_post(author, index):
    changed_post = request.get_json()
    posts[index].update(changed_post)

    return jsonify(posts[index], 200)


# Delete a post - DELETE http://localhost:5000/post/1
@app.route("/post/<int:index>", methods=["DELETE"])
@mandatory_token
def delete_post(author, index):
    try:
        if posts[index] is not None:
            del posts[index]
            return jsonify(f"The post {posts[index]} was successfully deleted.", 200)
    except:
        return jsonify("Couldn't find the post for deletion.", 404)


@app.route("/")
@mandatory_token
def get_authors(author, ):
    authors = Author.query.all()
    authors_list = []
    for author in authors:
        current_author = {
            "id_author": author.id_author,
            "name": author.name,
            "email": author.email
        }
        authors_list.append(current_author)

    return jsonify({"authors": authors_list})


@app.route("/authors/<int:index>", methods=["GET"])
@mandatory_token
def get_authors_by_id(author, index):
    author = Author.query.filter_by(id_author=index).first()
    if not author:
        return jsonify("Couldn't find this Author.")
    current_author = {
        "id_author": author.id_author,
        "name": author.name,
        "email": author.email
    }

    return jsonify(f"You searched for author: {current_author}")


@app.route("/authors", methods=["POST"])
@mandatory_token
def new_author(author, ):
    newAuthor = request.get_json()
    author = Author(
        name=newAuthor["name"],
        password=newAuthor["password"],
        email=newAuthor["email"],
    )

    db.session.add(author)
    db.session.commit()

    return jsonify({"Message": "New author created successfully"}, 200)


@app.route("/authors/<int:index>", methods=["PUT"])
@mandatory_token
def change_author(author, index):
    changed_author = request.get_json()
    author = Author.query.filter_by(id_author=index).first()
    if not author:
        return jsonify({"Message": "Couldn't find this author."})
    try:
        if changed_author["name"]:
            author.name = changed_author["name"]
    except:
        pass
    try:
        if changed_author["email"]:
            author.email = changed_author["email"]
    except:
        pass
    try:
        if changed_author["password"]:
            author.password = changed_author["password"]
    except:
        pass

    db.session.commit()
    return jsonify({"Message": "Author changed successfully."}, 200)


@app.route("/authors/<int:index>", methods=["DELETE"])
@mandatory_token
def delete_author(author, index):
    existing_author = Author.query.filter_by(id_author=index).first()
    if not existing_author:
        return jsonify({"Message": "Couldn't possible find this author"})
    db.session.delete(existing_author)
    db.session.commit()

    return jsonify({"Message": "Author successfully deleted."}, 200)


app.run(port=5000, host='localhost', debug=True)