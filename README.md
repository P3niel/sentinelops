# SentinelOps

> Outil de monitoring local simple et autonome, conçu comme projet vitrine DevOps par [Kami](https://www.linkedin.com/in/ton-lien/).

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)  
![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)  
![CI/CD](https://img.shields.io/badge/github%20actions-deploy-success?logo=githubactions)  
![License](https://img.shields.io/badge/license-MIT-green)

## Objectif

**SentinelOps** est une application de surveillance système conçue pour :

- Mettre en pratique les fondamentaux DevOps (monitoring, containerisation, CI/CD)
- Détecter les anomalies système (CPU, RAM, stockage)
- Générer des rapports HTML exploitables
- Envoyer des notifications mail en cas de détection
- Proposer une interface de visualisation simple

## Stack technique

| Élément         | Technologie            |
|----------------|------------------------|
| Langage        | Python 3.12            |
| Web Framework  | Flask                  |
| Monitoring     | psutil                 |
| Notifications  | SMTP (Mailtrap)        |
| Interface      | HTML, TailwindCSS      |
| Conteneurisation | Docker, Docker Compose |
| CI/CD          | GitHub Actions         |

## Lancement rapide en local

```bash
# 1. Cloner le dépôt
git clone https://github.com/P3niel/sentinelops.git
cd sentinelops

# 2. Copier et remplir le fichier d’environnement
cp .env.example .env

# 3. Lancer le service
make up

# 4. Ouvrir l'interface web
http://localhost:5000/ui/status
```

## Extrait de notification email

```
Objet : Alerte SentinelOps

Horodatage : 2025-04-07 21:42:01
Type : RAM critique
Message : Utilisation RAM > 85%
Hôte : dojo-local
IP : 192.168.0.21
```

## Variables d’environnement clés (.env)

```ini
FLASK_SECRET_KEY=your-secret-key
SMTP_HOST=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USER=...
SMTP_PASS=...
FROM_EMAIL=alert@sentinelops.io
TO_EMAIL=admin@votresite.dev
```

## Bénéfices et impact (ROI)

| Fonctionnalité                    | Impact direct                                      |
|----------------------------------|----------------------------------------------------|
| Surveillance locale intelligente | Moins de pannes silencieuses, diagnostic accéléré |
| Alertes automatiques             | Réaction rapide < 2 minutes                       |
| Rapports HTML générés            | Traçabilité claire, utile pour audits             |
| Pipeline CI/CD automatisé        | Réduction des erreurs humaines                    |
| Déploiement Dockerisé            | Portabilité immédiate                             |
| Projet pédagogique & vitrine     | Valorisation GitHub / LinkedIn                    |

> Temps économisé estimé : ~4h/semaine  
> Cas d’usage idéal : lab personnel, démo DevOps, surveillance réseau locale

## Routes disponibles

| Méthode | Endpoint               | Description                          |
|---------|------------------------|--------------------------------------|
| GET     | `/`                    | API de base                          |
| GET     | `/status`             | État système complet                 |
| GET     | `/detect`             | Liste des anomalies détectées        |
| GET     | `/respond`            | Réaction automatique                 |
| GET     | `/events`             | Historique des événements            |
| GET     | `/report/generate`    | Génération d’un rapport HTML         |
| GET     | `/about`              | Page de présentation du projet       |
| GET     | `/ui/status`          | Interface utilisateur : état système|
| POST    | `/ui/test/fake-alert` | Déclenchement manuel d’une alerte    |

## Démonstration hébergée

Il est possible de tester SentinelOps directement via une instance accessible en ligne :

```
http://<votre-ip-publique>:5000/about
```

## Test unitaire des routes

```bash
python test_route.py
```

## Auteur

Kami – Étudiant Tek2, orienté DevOps et infrastructure  
[LinkedIn](https://www.linkedin.com/in/ton-lien/) | [GitHub](https://github.com/P3niel)

## Licence

Projet sous licence MIT — contributions bienvenues.