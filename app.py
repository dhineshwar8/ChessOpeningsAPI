from flask import Flask, request, jsonify
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "openings.db"
CSV_FILE = "openings.csv"

# -------------------------------------
# Initialize database and load data
# -------------------------------------
def init_db():
    if os.path.exists(DB_NAME):
        return
    df = pd.read_csv(CSV_FILE)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS openings")
    cursor.execute("""
        CREATE TABLE openings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            eco_volume TEXT,
            eco TEXT,
            name TEXT,
            pgn TEXT,
            uci TEXT,
            epd TEXT
        )
    """)
    df.to_sql("openings", conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

init_db()

# -------------------------------------
# Utility: Run SQL query
# -------------------------------------
def run_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results

# -------------------------------------
# Routes
# -------------------------------------

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Chess Openings API!"})

@app.route("/openings", methods=["GET"])
def get_all_openings():
    return jsonify(run_query("SELECT * FROM openings LIMIT 100"))

@app.route("/search", methods=["GET"])
def search_by_move():
    move = request.args.get("move", default="1. e4")
    return jsonify(run_query("SELECT * FROM openings WHERE pgn LIKE ? LIMIT 50", (f"{move}%",)))

@app.route("/eco", methods=["GET"])
def search_by_eco():
    eco = request.args.get("code")
    if not eco:
        return jsonify({"error": "Please provide ?code= parameter"}), 400
    return jsonify(run_query("SELECT * FROM openings WHERE eco = ?", (eco,)))

@app.route("/longest", methods=["GET"])
def get_longest():
    return jsonify(run_query("""
        SELECT name, pgn,
               LENGTH(pgn) - LENGTH(REPLACE(pgn, ' ', '')) + 1 AS move_count
        FROM openings
        ORDER BY move_count DESC
        LIMIT 10
    """))

# -------------------------------------
# Run the Flask app
# -------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
