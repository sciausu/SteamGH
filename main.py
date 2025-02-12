import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

steamApiKey = os.getenv("STEAM_API_KEY")
print(steamApiKey)
