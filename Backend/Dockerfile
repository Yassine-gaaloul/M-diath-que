# Choisir une image de base qui contient Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier le fichier requirements.txt dans le container
COPY requirements.txt .

# Installer les dépendances Python depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du backend dans le container
COPY . .

# Exposer le port sur lequel Flask sera accessible
EXPOSE 5000

# Définir la commande pour lancer l'application Flask
CMD ["python", "app.py"]
