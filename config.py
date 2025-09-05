
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
