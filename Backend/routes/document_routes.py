from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.document_model import ajouter_livre, obtenir_livres, modifier_livre, supprimer_livre

livre_bp = Blueprint('livre_bp', __name__)  # Nom du Blueprint pour les livres

# Route pour obtenir tous les livres
@livre_bp.route("/getlivres", methods=["GET"])
def list_livres():
    livres = obtenir_livres()  # Liste tous les livres
    return jsonify(livres)

# Route pour ajouter un nouveau livre
@livre_bp.route("/addLivres", methods=["POST"])
def add_livre():
    data = request.json
    try:
        # Appel de la fonction d'ajout de livre
        ajouter_livre(data)
        return jsonify({"message": "Livre ajouté avec succès!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Gérer les erreurs comme un doublon de titre
    except Exception as e:
        return jsonify({"error": "Erreur interne, veuillez réessayer."}), 500

# Route pour modifier un livre
@livre_bp.route("/livres/<livre_id>", methods=["PUT"])
def update_livre(livre_id):
    try:
        data = request.json

        # Supprimer le champ `_id` s'il existe dans les données envoyées
        if "_id" in data:
            del data["_id"]

        # Appeler la fonction pour modifier le livre
        result = modifier_livre(ObjectId(livre_id), data)

        # Retourner une réponse appropriée
        if result.modified_count > 0:
            return jsonify({"message": "Livre mis à jour avec succès"}), 200
        else:
            return jsonify({"message": "Aucune mise à jour effectuée"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route pour supprimer un livre
@livre_bp.route("/supprimerlivre/<livre_id>", methods=["DELETE"])
def delete_livre(livre_id):
    try:
        supprimer_livre(livre_id)
        return jsonify({"message": "Livre supprimé avec succès!"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
