from bson import ObjectId  # Nécessaire pour manipuler ObjectId
from config import db  # Connection à la base MongoDB

emprunts = db["emprunts"]  # Utiliser la collection "emprunts" au lieu de "abonnes"

# Fonction pour obtenir tous les emprunts
def obtenir_emprunts():
    emprunts_list = list(emprunts.find())  # Récupère tous les emprunts
    for emprunt in emprunts_list:
        emprunt['_id'] = str(emprunt['_id'])  # Convertit ObjectId en chaîne
        # Vous pouvez ajouter ici la conversion pour les IDs liés aux livres et abonnés si nécessaire
    return emprunts_list

# Fonction pour ajouter un emprunt
def ajouter_emprunts(data):
    return emprunts.insert_one(data)

# Fonction pour modifier un emprunt
def modifier_emprunts(emprunt_id, data):
    if not ObjectId.is_valid(emprunt_id):
        raise ValueError("ID invalide.")
    # Met à jour les champs de l'emprunt spécifié
    return emprunts.update_one({"_id": ObjectId(emprunt_id)}, {"$set": data})

# Fonction pour supprimer un emprunt
def supprimer_emprunts(emprunt_id):
    if not ObjectId.is_valid(emprunt_id):
        raise ValueError("ID invalide.")
    # Supprime l'emprunt correspondant
    return emprunts.delete_one({"_id": ObjectId(emprunt_id)})
