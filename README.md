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
3. . Clone the repository.
    . Create a file named `spotifyApi_Info.py` inside the `spotify/music_app/` directory.
    . Add your Spotify API credentials in the `spotifyApi_Info.py` file:

   ```python
   SPOTIFY_API_KEY = "your_spotify_api_key_here
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up PostgreSQL database and configure your database in `settings.py`.

6. Run migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```

9. Open `http://127.0.0.1:8000` in your browser to use the app.

## Usage

- Get a random music track from Spotify on each visit.
- Rate the track with thumbs-up or thumbs-down.
- Admin panel available at `http://127.0.0.1:8000/admin` to manage tracks and ratings.
- 
- ## License

MIT License
