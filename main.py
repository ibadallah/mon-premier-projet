from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv('API_KEY')
print(f"La clé de l'API : {api_key}")

# print("\n--- Requête vers GitHub API ---")
# response = requests.get('https://api.github.com')

# if response.status_code == 200:
#     print("Requête réussie !")
#     data = response.json()
#     print(f"URL de l'api utilisateur : {data['user_url']}")
# else:
#     print(f"Erreur : {response.status_code}")

# recuperer les informations d'un utilisateur sur github

# Demander le nom d'utilisateur
username = input("Entrez un nom d'utilisateur GitHub : ")

# Faire la requête
url = f'https://api.github.com/users/{username}'
response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print(f"\n👤 Nom : {user['name']}")
    print(f"📍 Localisation : {user['location']}")
    print(f"📦 Repos publics : {user['public_repos']}")
else:
    print("❌ Utilisateur non trouvé")