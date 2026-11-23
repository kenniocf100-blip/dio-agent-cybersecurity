from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def connect_db():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (username TEXT, password TEXT)")
    connection.execute(
        "INSERT INTO users VALUES (?, ?)",
        ("admin", "correct-horse-battery"),
    )
    return connection

@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", ""))
    password = str(data.get("password", ""))

    # INTENCIONALMENTE VULNERÁVEL: concatenação de entrada na consulta SQL.
    query = (
        "SELECT username FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    connection = connect_db()
    try:
        row = connection.execute(query).fetchone()
    except sqlite3.Error:
        return jsonify({"error": "invalid query"}), 400
    finally:
        connection.close()

    return (jsonify({"authenticated": True}), 200) if row else (
        jsonify({"authenticated": False}), 401
    )

if __name__ == "__main__":
    # Somente laboratório local. Não exponha esta aplicação à rede.
    app.run(host="127.0.0.1", port=5001, debug=False)
