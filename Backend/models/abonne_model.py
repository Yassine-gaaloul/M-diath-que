from bson import ObjectId  # Nécessaire pour manipuler ObjectId
from config import db  # Connection à la base MongoDB

abonnes = db["abonnes"]


def obtenir_abonnes():
    abonnés = list(abonnes.find())  # Récupère tous les documents
    for abonne in abonnés:
        abonne['_id'] = str(abonne['_id'])  # Convertit ObjectId en chaîne
    return abonnés


def ajouter_abonne(data):
    return abonnes.insert_one(data)


def modifier_abonne(abonne_id, data):
    if not ObjectId.is_valid(abonne_id):
        raise ValueError("ID invalide.")
    # Met à jour les champs de l'abonné spécifié
    return abonnes.update_one({"_id": abonne_id}, {"$set": data})


def supprimer_abonne(abonne_id):
    if not ObjectId.is_valid(abonne_id):
        raise ValueError("ID invalide.")
    # Supprime l'abonné correspondant
    return abonnes.delete_one({"_id": ObjectId(abonne_id)})
