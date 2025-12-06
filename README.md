# MarAppi Backend

Minimal Flask REST API for managing categories, places and reviews for tourism in Santa Marta.

Essentials
- Python 3.8+
- Virtual environment recommended
- Dependencies listed in `requirements.txt` (Flask, Flask-SQLAlchemy)

Quick start (PowerShell)
1. Activate virtualenv:
```powershell
.\venv\Scripts\Activate;
```
2. Install dependencies:
```powershell
pip install -r requirements.txt;
```
3. Set env and run:
```powershell
$env:FLASK_APP = 'app:create_app'
$env:FLASK_ENV = 'development'
flask run
```

Common endpoints
- `POST /api/categories`  — Create category (JSON: `{ "name": "Beaches" }`)
- `GET /api/categories`   — List categories
- `POST /api/places`      — Create place (JSON: `{ "name": "Park", "category_id": 1 }`)
- `GET /api/places`       — List places
- `POST /api/reviews`     — Create review (JSON: `{ "content": "Great", "rating": 5, "place_id": 1 }`)
- `GET /api/reviews/place/<place_id>` — List reviews for a place

Reset local DB (development):
```powershell
Remove-Item .\marappi.db
```

Still working on more features and documentation.