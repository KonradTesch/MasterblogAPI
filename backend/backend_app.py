from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def validate_post_data(post_data):
    """
    Checks if the post has all required keys and valid values and not more.
    :param post_data:
    :return:
    """
    return post_data.get("title") and post_data.get("content") and len(post_data.keys()) == 3


@app.route('/api/posts', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'POST':
        print(f" type: {request.content_type}")
        if request.content_type != 'application/json':
            return jsonify({"error": "Missing or wrong content type"}), 415

        new_post = request.get_json()

        new_id = max(post["id"] for post in POSTS) + 1
        new_post["id"] = new_id
        if not validate_post_data(new_post):
            return jsonify({"error": "Invalid blog-post data"}), 400

        POSTS.append(new_post)

        return jsonify(new_post), 201
    else:
        #GET request
        return jsonify(POSTS)


@app.route('/api/posts/<int:id_to_delete>', methods=['DELETE'])
def delete_post(id_to_delete):
    if request.method == 'DELETE':
        for post in POSTS:
            if post["id"] == id_to_delete:
                print(f"remove {post}")
                POSTS.remove(post)
                return jsonify({"mesage": f"Post with id {id_to_delete} has been deleted successfully."}), 200
        return jsonify({"error": f"A post with the id {id_to_delete} doesn't exist"}), 404

    return None



@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
