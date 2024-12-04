from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.abonne_model import ajouter_abonne, obtenir_abonnes, modifier_abonne, supprimer_abonne

abonne_bp = Blueprint('abonne_bp', __name__)

@abonne_bp.route("/getabonnes", methods=["GET"])
def list_abonnes():
    abonnés = obtenir_abonnes()
    return jsonify(abonnés)  # Retourne la liste des abonnés avec _id comme chaîne


@abonne_bp.route("/add", methods=["POST"])
def add_abonne():
    data = request.json
    ajouter_abonne(data)
    return jsonify({"message": "Abonné ajouté avec succès!"})


@abonne_bp.route("/abonnes/<abonne_id>", methods=["PUT"])
def update_abonne(abonne_id):
    try:
        
        data = request.json
        result = modifier_abonne(ObjectId(abonne_id), data)
        if result.matched_count > 0:
            return jsonify({"message": "Abonné mis à jour avec succès!"})
        else:
            return jsonify({"message": "Abonné introuvable!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@abonne_bp.route("/supprimer/<abonne_id>", methods=["DELETE"])
def delete_abonne(abonne_id):
    try:
        supprimer_abonne(abonne_id)
        return jsonify({"message": "Abonné supprimé avec succès!"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
