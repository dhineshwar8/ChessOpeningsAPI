# ♟️ Chess Openings Explorer API
no use for chess players `: |

A simple Flask-based REST API that lets you explore chess openings from a CSV dataset. It supports filtering by moves (PGN), ECO codes, and finding the longest openings.

---

## 📦 Features

- 🔍 Search chess openings by their starting moves (`pgn`)
- 📚 Filter by **ECO code**
- ⏳ List the **longest openings** by number of moves
- 🧾 Returns data in JSON format

---

## 📁 Dataset

The dataset is a CSV file containing chess openings with the following fields:

- `eco_volume` – ECO classification volume (e.g., A, B, C, D, E)
- `eco` – ECO code (e.g., B20, C45)
- `name` – Name of the chess opening
- `pgn` – Moves in PGN notation
- `uci` – Moves in UCI format
- `epd` – Position in EPD format

> Make sure the CSV file is named **`openings (1).csv`** and placed in the root directory.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chess-openings-api.git
cd chess-openings-api
```

### 2. Install Dependencies

```bash
pip install flask pandas
```

### 3. Run the Server

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`

---

## 📡 API Endpoints

### ✅ Base Route

```http
GET /
```
Returns a welcome message.

---

### 📖 All Openings

```http
GET /openings
```
Returns the first 100 openings.

---

### 🔍 Search by Opening Move

```http
GET /search?move=1. e4
```

Returns all openings starting with `1. e4`.

---

### 🏷️ Filter by ECO Code

```http
GET /eco?code=C20
```

Returns openings with ECO code `C20`.

---

### 📏 Longest Openings

```http
GET /longest
```

Returns the top 10 openings with the most moves.

---

## 🛠 Tech Stack

- Python 3.x
- Flask
- SQLite
- Pandas

---

## 📂 Folder Structure

```
chess_openings_api/
├── app.py
├── openings.csv
├── openings.db (auto-generated)
├── README.md
```

---

## 💡 Future Improvements

- Add pagination to `/openings`
- Add frontend UI using Flask templates or React
- Deploy to Render / Replit / Vercel

---

## 🧠 Credits

- Chess opening dataset (source: [Lichess](https://lichess.org/))
- PGN & ECO standard references

---

