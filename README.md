# MarAppi

Flask REST API for managing categories, places and reviews for tourism in Santa Marta.

Essentials
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Marshmallow
- Alembic

Quick start (PowerShell)
1. Activate virtualenv:
```powershell
.\venv\Scripts\Activate;
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
```
3. Set env and run:
```powershell
$env:FLASK_APP = 'app:create_app'
$env:FLASK_ENV = 'development'
flask run
```

Database migrations (Flask-Migrate)
- Initialize migrations (only once):
```powershell
$env:FLASK_APP = 'app:create_app'
flask db init
```
- Create a migration from models:
```powershell
flask db migrate -m "Initial migration"
```
- Apply migrations:
```powershell
flask db upgrade
```

Common endpoints
- `POST /api/categories`  — Create category
- `GET /api/categories`   — List categories
- `GET /api/categories/<id>` — Get category
- `PUT/PATCH /api/categories/<id>` — Update category
- `DELETE /api/categories/<id>` — Delete category
- `POST /api/places`      — Create place
- `GET /api/places`       — List places
- `GET /api/places/<id>`  — Get place
- `PUT/PATCH /api/places/<id>` — Update place
- `DELETE /api/places/<id>` — Delete place
- `POST /api/reviews`     — Create review
- `GET /api/reviews/place/<place_id>` — List reviews for a place
- `GET /api/reviews/<id>` — Get review
- `PUT/PATCH /api/reviews/<id>` — Update review
- `DELETE /api/reviews/<id>` — Delete review

Reset local DB (development):
```powershell
Remove-Item .\marappi.db
```

- Use `flask db` commands after installing `Flask-Migrate` to manage schema changes.

Connecting to the local SQLite database from VS Code
---------------------------------------------------

- **Database file path**: the SQLite database is a file in the project at
	`instance\marappi.db` (absolute path example on Windows:
	`C:\Users\Lizarazo\Desktop\marappi_backend\instance\marappi.db`).

- **How to connect**: open your VS Code Database extension (or `SQLTools`) and
	select `SQLite` as server/driver. For the "Database Path" use either the
	absolute path above or the workspace variable:
	`${workspaceFolder}\\instance\\marappi.db`.

- **Example `settings.json` (SQLTools)**: add this to `.vscode/settings.json`
	so the connection appears automatically:

```json
{
	"sqltools.connections": [
		{
			"name": "MarAppi (local)",
			"driver": "SQLite",
			"database": "${workspaceFolder}\\instance\\marappi.db"
		}
	]
}
```

- **Using other SQLite viewers**: the `SQLite` extension (by alexcvzz) or
	external tools like "DB Browser for SQLite" also work — just open the
	`instance\marappi.db` file.

- **Notes and tips**:
	- You do not need host/port/user/password for SQLite — only the file path.
	- If `flask run` is active it may lock the file; stop the server or connect
		in read-only mode if your extension supports it.
	- If you prefer to keep migrations under version control, include
		`migrations/` in the repo (recommended). If you removed `migrations/` from
		`.gitignore`, you can commit the generated files so teammates can apply
		the same schema.

Seeding the database (development)
---------------------------------

For development you can populate the DB with example data using the seed
script included in the project. It will delete existing rows in the
`reviews`, `places` and `categories` tables and insert sample entries.

Run the seed script from the project root (make sure your virtualenv is
activated):

Windows (cmd.exe / PowerShell):
```bat
set FLASK_APP=app:create_app
python -m seeds.seed
```

Use this seed script only in development; do not run it against production data.

Clearing seeded data
--------------------

If you want to remove the example data inserted by the seed script, a small
helper is provided: `seeds/clear.py`. It deletes rows from `reviews`,
`places` and `categories` (in that order) using the app's SQLAlchemy session.

Run it like this:

Windows (cmd.exe / PowerShell):
```bat
set FLASK_APP=app:create_app
python -m seeds.clear
```

Remember to backup your DB first if it contains any important data:
```bat
copy instance\marappi.db instance\marappi.db.bak
```
All contributions are welcome!