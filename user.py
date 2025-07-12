from flask import Flask, jsonify, request
from app import app, db

# view user
@app.route("/api/view/user/", methods=['GET'])
def view_user():
    try:
        cursor = db.cursor()
        cursor.execute("""
            SELECT *
            FROM users
            ORDER BY user_id
            """
        )
        msg = cursor.fetchall()
        return jsonify(msg), 200
    except Exception as e:
        return jsonify({'success':False, 'error':str(e)}), 400

# add user
@app.route("/api/add/user/", methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        cursor = db.cursor()

        username = data.get('username')
        pw_hash = data.get('pw_hash')

        cursor.execute("""
            INSERT INTO users (username, pw_hash)
            VALUE (%s, %s)
            """, (username, pw_hash)
        )
        db.commit()

        return jsonify({'success':True}), 201
    except Exception as e:
        return jsonify({'success':False, 'error':str(e)}), 400
