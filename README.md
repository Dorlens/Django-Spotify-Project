# Random Music Generator with Thumbs Up/Down Feature

A web application that generates a random music track from Spotify and allows users to rate the track with a thumbs-up or thumbs-down. The application stores user ratings and tracks in a PostgreSQL database.

## Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **API**: Spotify API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/project-name.git
    cd project-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On macOS/Linux
    .\env\Scripts\activate   # On Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL database and configure your database in `settings.py`.

5. Run migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

8. Open `http://127.0.0.1:8000` in your browser to use the app.

## Usage

- Get a random music track from Spotify on each visit.
- Rate the track with thumbs-up or thumbs-down.
- Admin panel available at `http://127.0.0.1:8000/admin` to manage tracks and ratings.
- 
- ## License

MIT License