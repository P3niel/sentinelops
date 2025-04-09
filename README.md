# 🛡️ SentinelOps

> Un mini système de surveillance local codé avec amour par [Kami](https://www.linkedin.com/in/ton-lien/) — Projet DevOps vitrine

---

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)
![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)
![CI/CD](https://img.shields.io/badge/github%20actions-deploy-success?logo=githubactions)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🎯 Objectif

**SentinelOps** est une application de monitoring système conçue pour :

- 🎓 *Apprendre et mettre en pratique les bases DevOps*
- 🧠 *Détecter automatiquement des anomalies système*
- 📬 *Recevoir des alertes par mail en cas de problème*
- 💻 *Proposer une interface web simple et claire*

---

## 🧰 Stack Technique

- **Langage** : Python 3.12
- **Framework Web** : Flask
- **Monitoring** : psutil
- **Conteneurisation** : Docker + Docker Compose
- **CI/CD** : GitHub Actions
- **Notifications** : SMTP (Mailtrap)
- **Interface** : HTML, TailwindCSS, Animate.css

---

## 🚀 Démo locale

```bash
# 1. Clone le repo
git clone https://github.com/P3niel/sentinelops.git
cd sentinelops

# 2. Ajoute ton fichier .env (Mailtrap, Flask secret key...)
cp .env.example .env  # puis complète-le

# 3. Lance le tout
make up

# 4. Accède à l’interface
http://localhost:5000/ui/status

📬 Exemple de notification

🚨 Alerte SentinelOps

🕒 Timestamp : 2025-04-07 21:42:01
🧠 Type : RAM critique
💬 Message : Utilisation RAM > 85%

📍 Hôte : dojo-local
🌐 IP : 192.168.0.21

🔐 Variables d’environnement

FLASK_SECRET_KEY=your-secret-key
SMTP_HOST=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USER=xxxx
SMTP_PASS=xxxx
FROM_EMAIL=alert@sentinelops.io
TO_EMAIL=admin@votresite.dev

💰 ROI (Retour sur Investissement)
✅ Bénéfice	📈 Impact direct
🔎 Surveillance locale intelligente	Moins de pannes silencieuses
📬 Alertes automatiques	Réactivité < 2 minutes
📝 Rapports HTML	Traçabilité claire
🔄 CI/CD GitHub Actions	Zéro erreur manuelle
🐳 Dockerisation	Portabilité + démo rapide
🧠 Projet vitrine	Valorisation LinkedIn / GitHub

⏱️ Temps économisé estimé : ~4h/semaine
👨‍💻 Utilisation idéale : environnements de test, lab perso, serveurs internes
📎 Routes disponibles
Type	Endpoint	Description
GET	/	Status API
GET	/status	Infos système
GET	/detect	Anomalies détectées
GET	/respond	Réponse automatique
GET	/events	Logs détectés
GET	/report/generate	Génère un rapport HTML
GET	/about	Page vitrine du projet
GET	/ui/status	Interface live
POST	/ui/test/fake-alert	Envoie une alerte test
🧪 Test rapide

python test_route.py

🧪 Tester le projet SentinelOps

SentinelOps est un projet exécutable en local via Docker, mais propose aussi une interface de démonstration si tu veux tester rapidement sans rien installer.
🔥 Option 1 – Tester directement via l'interface (démo)

    🎯 Idéal pour comprendre l’utilité du projet sans setup technique.

🌐 Accès à la version de démonstration (hébergée) :

http://<TON-IP-PUBLIQUE>:5000/about

📍 Pages disponibles :
Page	Description
/about	Présentation interactive du projet
/ui/status	Voir l'état système en temps réel
/ui/test	Simuler une alerte et recevoir un email
/events	Voir l'historique des anomalies détectées
/report/generate	Générer un rapport HTML complet
⚙️ Option 2 – Tester localement avec Docker

    🐳 Idéal pour les développeurs ou recruteurs techniques.

Étapes d'installation :

git clone https://github.com/<ton-user>/SentinelOps.git
cd SentinelOps
cp .env.example .env    # ⚠️ Personnalise tes variables d’environnement
make up                 # Ou bien docker-compose up --build

Puis ouvre : http://localhost:5000
📬 Test d’alerte email

Depuis l’interface /ui/test, clique sur "Simuler une alerte" pour :

    Déclencher une fausse alerte système

    Envoyer un email via Mailtrap

    Vérifier le bon fonctionnement des notifications

💡 Tu peux configurer ton propre SMTP dans .env si besoin.

✅ Vérifie toutes les routes automatiquement
🧠 Auteur

Kami – Étudiant Tek2, passionné de DevOps

🔗 LinkedIn
💻 GitHub
📄 Licence

MIT — Libre de réutiliser, améliorer, contribuer 🙏