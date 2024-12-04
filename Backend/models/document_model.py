from bson import ObjectId  # Nécessaire pour manipuler ObjectId
from config import db  # Connexion à la base MongoDB

livres = db["livre"]  # Collection "livres"

# Récupère tous les livres
def obtenir_livres(filtre=None):
    if filtre is None:
        livres_list = list(livres.find())  # Récupère tous les documents
    else:
        livres_list = list(livres.find(filtre))  # Récupère les documents selon un filtre
    for livre in livres_list:
        livre['_id'] = str(livre['_id'])  # Convertit ObjectId en chaîne
    return livres_list

# Ajoute un nouveau livre
def ajouter_livre(data):
    # Vérifier si le titre existe déjà
    titre = data.get("titre")
    existing_livre = livres.find_one({"titre": titre})
    if existing_livre:
        raise ValueError(f"Un livre avec le titre '{titre}' existe déjà.")
    
    # Si le titre est unique, ajouter le livre
    return livres.insert_one(data)

# Modifie un livre existant
def modifier_livre(livre_id, data):
    if not ObjectId.is_valid(livre_id):
        raise ValueError("ID invalide.")
    return livres.update_one({"_id": ObjectId(livre_id)}, {"$set": data})

# Supprime un livre
def supprimer_livre(livre_id):
    if not ObjectId.is_valid(livre_id):
        raise ValueError("ID invalide.")
    # Supprime le livre correspondant
    return livres.delete_one({"_id": ObjectId(livre_id)})
