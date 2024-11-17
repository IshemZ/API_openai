from openai import OpenAI
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
API_KEY_OPEN_AI = os.getenv("API_KEY_OPEN_AI")

# Configure le client avec ta clé API
client = OpenAI(api_key=API_KEY_OPEN_AI)

# Lister les modèles disponibles
#models = client.models.list()
#print(models)

