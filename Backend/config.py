from pymongo import MongoClient

# Connexion MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["mediatheque_db"]
