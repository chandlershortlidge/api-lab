import os
from dotenv import load_dotenv

# Load environment variables from a .env file in the project root
load_dotenv()

SPOTIFY_CLIENT_ID = "d27240c3a55143ff8bdf61b5bb37ced9"
SPOTIFY_CLIENT_SECRET = "86a310cc943544cc820418bcf8836a26"


SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
