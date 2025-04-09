# init_users.py

import sqlite3
from flask_bcrypt import Bcrypt
from pathlib import Path

bcrypt = Bcrypt()
db_path = Path("users.db")

# Supprime la base existante si elle existe déjà (facultatif)
if db_path.exists():
    db_path.unlink()

# Création de la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Table utilisateurs
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Mot de passe hashé
password_hash = bcrypt.generate_password_hash("kami14").decode("utf-8")

# Insertion utilisateur admin
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", password_hash))

conn.commit()
conn.close()

print("✅ Utilisateur admin créé avec succès (user: admin / pass: kami14)")
