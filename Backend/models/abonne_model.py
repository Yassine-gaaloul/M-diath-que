from bson import ObjectId  
from config import db  

abonnes = db["abonnes"]


def obtenir_abonnes():
    abonnés = list(abonnes.find())  
    for abonne in abonnés:
        abonne['_id'] = str(abonne['_id'])  
    return abonnés


def ajouter_abonne(data):
    return abonnes.insert_one(data)


def modifier_abonne(abonne_id, data):
    if not ObjectId.is_valid(abonne_id):
        raise ValueError("ID invalide.")
    
    return abonnes.update_one({"_id": abonne_id}, {"$set": data})


def supprimer_abonne(abonne_id):
    if not ObjectId.is_valid(abonne_id):
        raise ValueError("ID invalide.")
    
    return abonnes.delete_one({"_id": ObjectId(abonne_id)})
