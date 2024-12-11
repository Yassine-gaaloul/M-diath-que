from bson import ObjectId  
from config import db  

livres = db["livre"]  

# Récupère tous les livres
def obtenir_livres(filtre=None):
    if filtre is None:
        livres_list = list(livres.find())  
    else:
        livres_list = list(livres.find(filtre))  
    for livre in livres_list:
        livre['_id'] = str(livre['_id'])  
    return livres_list

def ajouter_livre(data):

    titre = data.get("titre")
    existing_livre = livres.find_one({"titre": titre})
    if existing_livre:
        raise ValueError(f"Un livre avec le titre '{titre}' existe déjà.")
    
    
    return livres.insert_one(data)

def modifier_livre(livre_id, data):
    if not ObjectId.is_valid(livre_id):
        raise ValueError("ID invalide.")
    return livres.update_one({"_id": ObjectId(livre_id)}, {"$set": data})

def supprimer_livre(livre_id):
    if not ObjectId.is_valid(livre_id):
        raise ValueError("ID invalide.")

    return livres.delete_one({"_id": ObjectId(livre_id)})
