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

messages = [
    {"role": "system", "content": "Tu es un chatbot qui est un assistant dans la vie de tout les jours."},
]
while True:
    user_input = input("Vous: ")
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages
    )

    assistant_response = response.choices[0].message["content"]
    print(f"Assistant: {assistant_response}")
    messages.append({"role": "assistant", "content": assistant_response})