from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import os
import time
import pymysql

def connect_to_db():
    for i in range(10):
        try:
            print(f"[DB] connection attempt {i}/10")
            return pymysql.connect(
                    host=os.getenv("MYSQL_HOST"),
                    user=os.getenv("MYSQL_USER"),
                    password=os.getenv("MYSQL_PASSWORD"),
                    database=os.getenv("MYSQL_DATABASE")
                    )
        except pymysql.err.OperationalError:
            print("[DB] Not ready, retrying...")
            time.sleep(2)
    raise RuntimeError("[DB] Cannot connect to DB after 10 attempts")

load_dotenv()
app = Flask(__name__)
db = connect_to_db()
CORS(app)               # FIX THIS IN RELEASE

# index
@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("""
        SELECT *
        FROM posts
        ORDER BY post_id
        """)
    msg = cursor.fetchall()
    return jsonify(msg)

from user import view_user, add_user

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
