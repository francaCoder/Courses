
# My first API - FLASK
# FLASK & FLASK RESTFUL

from flask import Flask, jsonify, request

app = Flask(__name__)
"""
1 - Set the objective of the API
    Exemple: We will build an API of blog, where i can consult, change, create and delete posts in a blog using the API
2 - What will be the URL? 
    Exemple: Local application → ("https://localhost:5000")
    cloud →  (www.domain.com/api)
3 - Endpoints 
    you must make available the endpoints for each functionality
    > /posts/1...2
    > /create/....
4 - What resources the API will make available? : Posts informations  
5 - What HTTP verbs will make available?
    * GET
    * POST
    * PUT
    * DELETE
6 - What are the full URL for each one?
    * GET https://localhost:5000/posts
    * GET id https://localhost:5000/posts/1
    * POST id https://localhost:5000/posts/
    * PUT id https://localhost:5000/posts/1
    * DELETE id https://localhost:5000/posts/1
"""
posts = [
    {
        "title": "My history",
        "author": "Jhon Lenon"
    },
    {
        "title": "New sony device",
        "author": "Gavin lewis",
    },
    {
        "title": "Release of the year",
        "author": "Jess Bezos",
    },
]
# Default Route - GET http://localhost:5000
@app.route("/")
def get_posts():
    return jsonify(posts)


# Route - GET c/ id http://localhost:5000/posts/1
@app.route("/post/<int:index>", methods=["GET"])
def get_post_by_id(index):
    return jsonify(posts[index])

# New post - POST http://localhost:5000/post
@app.route("/post", methods=["POST"])
def new_post():
    post = request.get_json()
    posts.append(post)

    return jsonify(post, 200)


# Change an existing post - PUT http://localhost:5000/post/2
@app.route("/post/<int:index>", methods=["PUT"])
def change_post(index):
    changed_post = request.get_json()
    posts[index].update(changed_post)

    return jsonify(posts[index], 200)


# Delete a post - DELETE http://localhost:5000/post/1
@app.route("/post/<int:index>", methods=["DELETE"])
def delete_post(index):
    try:
        if posts[index] is not None:
            del posts[index]
            return jsonify(f"The post {posts[index]} was successfully deleted.", 200)
    except:
        return jsonify("Couldn't find the post for deletion.", 404)


app.run(port=5000, host='localhost', debug=True)
