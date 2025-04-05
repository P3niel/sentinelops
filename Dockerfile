# 🐍 Image de base minimaliste
FROM python:3.12-slim

# 🧑‍💻 Ajout d'un user non-root
RUN useradd -ms /bin/bash sentinel

# 📁 Répertoire de travail
WORKDIR /home/sentinel/app

# 🔁 Copie du code dans le conteneur
COPY . .

# 📦 Installation des dépendances
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 📂 Création des répertoires persistants
RUN mkdir -p logs static/reports

# 🎯 Attribution des droits au user
RUN chown -R sentinel:sentinel /home/sentinel

# 👤 Switch vers l'utilisateur non-root
USER sentinel

# 🌐 Port exposé
EXPOSE 5000

# 🚀 Lancement de l'app Flask
CMD ["python", "api.py"]
