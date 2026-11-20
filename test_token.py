import os
import requests
from dotenv import load_dotenv

load_dotenv()  # lit le fichier .env
token = os.getenv("HF_TOKEN")

response = requests.get(
    "https://huggingface.co/api/whoami-v2",
    headers={"Authorization": f"Bearer {token}"},
)

print("Code :", response.status_code)
print("Compte :", response.json().get("name"))