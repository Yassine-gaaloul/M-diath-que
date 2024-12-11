from bson import ObjectId  
from config import db  

emprunts = db["emprunts"]  


def obtenir_emprunts():
    emprunts_list = list(emprunts.find())  
    for emprunt in emprunts_list:
        emprunt['_id'] = str(emprunt['_id'])  
        
    return emprunts_list


def ajouter_emprunts(data):
    return emprunts.insert_one(data)


def modifier_emprunts(emprunt_id, data):
    if not ObjectId.is_valid(emprunt_id):
        raise ValueError("ID invalide.")
    
    return emprunts.update_one({"_id": ObjectId(emprunt_id)}, {"$set": data})


def supprimer_emprunts(emprunt_id):
    if not ObjectId.is_valid(emprunt_id):
        raise ValueError("ID invalide.")

    return emprunts.delete_one({"_id": ObjectId(emprunt_id)})
