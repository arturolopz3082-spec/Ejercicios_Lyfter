import json

from flask import Flask
from flask import request, jsonify, Response
app = Flask(__name__)

shows_list = [
    {
        'title': '3 body problem',
        'genre': 'Sci-Fi'
    },
    {
        'title': 'Severance',
        'genre': 'Thriller'
    },
    {
        'title': 'Black Knight',
        'genre': 'Sci-Fi'
    }
]

@app.route("/shows")
def shows():
    filtered_shows = shows_list
    genre_filter = request.args.get('genre')
    if genre_filter:
        filtered_shows = list(
            filter (lambda show: show['genre'] == genre_filter, filtered_shows)
        )
    return {'data': filtered_shows}

@app.route("/echo", methods=['POST'])
def echo():
    request_body = request.json
    return {'request_body': request_body}

comments_list = [
    "Genial video, entendí todo a la perfección",
    "Me encantó el intro jajajaja"
]

@app.route("/comment", methods=['POST'])
def post_comment():
    comment_content = request.form.get("comment_content")
    if not comment_content:
        return jsonify(message= "no empty comments allowed"), 400

    comments_list.append(comment_content)
    return comments_list

user_list = [
    {
        "email" : "action.bronson@gmail.com",
        "password" : "123@a!"
    }
]

@app.route("/register", methods=['POST'])
def register_user():
    try:
        if "email" not in request.json:
            raise ValueError('Email missing from the body')
        if "password" not in request.json:
            raise ValueError('Password missing from the body')

        user_list.append(
            {
                "email" : request.json["email"],
                "password" : request.json["password"]
            }
        )
        return user_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 400


@app.route('/view-token')
def view_token():
    token = request.headers.get('token', '')
    return token

@app.route('/hello')
def hello():
    response_body = json.dumps({'msg': 'Hello World!'})
    return Response(response_body, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='localhost',debug=True)