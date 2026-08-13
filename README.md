# CodeAlpha URL Shortener

A simple URL shortener backend built with Flask and SQLite. The application accepts long URLs through a REST API, generates unique short codes, stores the URL mappings in a database, and redirects users from the generated short URL to the original URL.

## Features
- Create short URLs through a REST API
- Generate unique 6-character short codes
- Store URL mappings using SQLite and SQLAlchemy
- Redirect short URLs to their original destinations
- Track the number of times a short URL is accessed
- Validate submitted URLs
- Return appropriate error responses for invalid or missing URLs
- Handle requests for non-existent short codes

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- REST API

## Project Structure

- **app.py** — Flask application and API routes
- **models.py** — URL database model
- **extensions.py** — SQLAlchemy configuration
- `requirements.txt` — Python dependencies
- `.gitignore` — Files excluded from Git
- `README.md` — Project documentation
- `LICENSE` — MIT License
