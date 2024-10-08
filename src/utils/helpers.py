from flask import jsonify

def json_format(message, status = 200):
    return jsonify({
        "message": message,
    }), status
