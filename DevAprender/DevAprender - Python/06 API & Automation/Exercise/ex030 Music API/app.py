"""
1 - Set the objective of the API
    Exemple: We will build an API of music, where i can consult, change, create and delete musics using the API
2 - What will be the URL?
    Exemple: Local application → ("https://localhost:5000")
    cloud →  (www.domain.com/api)
3 - Endpoints
    you must make available the endpoints for each functionality
    > /posts/1...2
    > /create/....
4 - What resources the API will make available?
    → Information about the songs
5 - What HTTP verbs will make available?
    * GET
    * POST
    * PUT
    * DELETE
6 - What are the full URL for each one?
    * GET https://localhost:5000/musics
    * GET id https://localhost:5000/musics/1
    * POST id https://localhost:5000/musics
    * PUT id https://localhost:5000/musics/1
    * DELETE id https://localhost:5000/musics/1
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

musics = [
    {
        "Music": "Osaka",
        "Genre": "Trap",
    },
    {
        "Music": "Blue Pill",
        "Genre": "Trap",
    },
    {
        "Music": "Saturno",
        "Genre": "Trap",
    },
]

# Default Route - GET http://localhost:5000
@app.route("/musics", methpds=["GET"])
def get_musics():
    return jsonify(musics)

# Route - GET c/ id http://localhost:5000/music/1
@app.route("/music/<int:index>", methods=["GET"])
def get_music_by_id(index):
    return jsonify(musics[index])

# New post - POST http://localhost:5000/music
@app.route("/music", methods=["POST"])
def new_music():
    music = request.get_json()
    musics.append(music)

    return jsonify(music, 200)


# Change an existing post - PUT http://localhost:5000/music/2
@app.route("/music/<int:index>", methods=["PUT"])
def change_music(index):
    changed_music = request.get_json()
    musics[index].update(changed_music)

    return jsonify(musics[index], 200)


# Delete a post - DELETE http://localhost:5000/music/1
@app.route("/music/<int:index>", methods=["DELETE"])
def delete_music(index):
    try:
        if musics[index] is not None:
            del musics[index]
            return jsonify(f"The music {musics[index]} was successfully deleted.", 200)
    except:
        return jsonify("Couldn't find the music for deletion.")


app.run(port=5000, host='localhost', debug=True)