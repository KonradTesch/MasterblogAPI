from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

def get_post_by_id(post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return post

    return None


def validate_post_data(post_data):
    """
    Checks if the post has all required keys and valid values and not more.
    :param post_data:
    :return:
    """
    return post_data.get("title") and post_data.get("content") and len(post_data.keys()) == 3


@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'POST':
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
        sort = request.args.get('sort')
        direction = request.args.get('direction')

        if sort in ["title", "content"] and (not direction or direction in ["asc", "desc"]):
            sorted_list = sorted(POSTS, key=lambda post: post[sort].lower(), reverse=(direction == "desc"))
            return jsonify(sorted_list)
        elif sort and sort not in ["title", "content"]:
            #sort is not None but invalid
            return jsonify({"error": "Invalid parameter: sort"}), 400
        elif direction and direction not in ["asc", "desc"]:
            # direction is not None but invalid
            return jsonify({"error": "Invalid parameter: direction"}), 400


        #GET request
        return jsonify(POSTS)


@app.route('/api/posts/<int:post_id>', methods=['DELETE', 'PUT'])
def handle_post_id(post_id):
    if request.method == 'DELETE':
        post_to_delete = get_post_by_id(post_id)
        if post_to_delete:
            return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200

        #No post was found
        return jsonify({"error": f"A post with the id {post_id} doesn't exist"}), 404
    else:
        'PUT request'
        if request.content_type != 'application/json':
            return jsonify({"error": "Missing or wrong content type"}), 415

        post_to_update = get_post_by_id(post_id)
        updated_post = request.get_json()

        for post in POSTS:
            if post["id"] == post_id:
                if updated_post.get("title"):
                    post["title"] = updated_post["title"]
                if updated_post.get("content"):
                    post["content"] = updated_post["content"]
                return jsonify(post), 200

        # No post was found
        return jsonify({"error": f"A post with the id {post_id} doesn't exist"}), 404


@app.route('/api/posts/search', methods=['GET'])
def handle_posts_search():
    title = request.args.get('title')
    content = request.args.get('content')

    results= []
    if not title and not content:
        return jsonify(results), 200

    for post in POSTS:
        if (not title or title in post["title"]) and (not content or content in post["content"]):
            results.append(post)

    return jsonify(results), 200


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
