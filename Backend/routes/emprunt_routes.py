from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.emprunt_model import ajouter_emprunts, obtenir_emprunts, modifier_emprunts, supprimer_emprunts

emprunt_bp = Blueprint('emprunt_bp', __name__)

# Route pour obtenir la liste des emprunts
@emprunt_bp.route("/getemprunts", methods=["GET"])
def list_emprunts():
    emprunts = obtenir_emprunts()  # Récupère la liste des emprunts
    return jsonify(emprunts)  # Retourne la liste des emprunts avec _id comme chaîne


# Route pour ajouter un emprunt
@emprunt_bp.route("/addemprunts", methods=["POST"])
def add_emprunt():
    data = request.json  # Récupère les données envoyées en POST
    ajouter_emprunts(data)  # Ajoute l'emprunt dans la base de données
    return jsonify({"message": "Emprunt ajouté avec succès!"})


# Route pour mettre à jour un emprunt
@emprunt_bp.route("/emprunts/<emprunt_id>", methods=["PUT"])
def update_emprunt(emprunt_id):
    try:
        data = request.json
        result = modifier_emprunts(ObjectId(emprunt_id), data)  # Mise à jour de l'emprunt
        if result.matched_count > 0:
            return jsonify({"message": "Emprunt mis à jour avec succès!"})
        else:
            return jsonify({"message": "Emprunt introuvable!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route pour supprimer un emprunt
@emprunt_bp.route("/supprimeremprent/<emprunt_id>", methods=["DELETE"])
def delete_emprunt(emprunt_id):
    try:
        supprimer_emprunts(emprunt_id)  # Supprime l'emprunt
        return jsonify({"message": "Emprunt supprimé avec succès!"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
