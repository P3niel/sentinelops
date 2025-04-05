# 📦 Nom du service Docker Compose
SERVICE=sentinelops

# 📁 Dossier du docker-compose
COMPOSE_FILE=infra/docker-compose.yml

# 🛠️ Build + run
up:
	docker-compose -f $(COMPOSE_FILE) up --build

# 🧹 Stop + remove container
down:
	docker-compose -f $(COMPOSE_FILE) down

# 🔁 Rebuild propre (clean + build + run)
rebuild:
	docker-compose -f $(COMPOSE_FILE) down
	docker-compose -f $(COMPOSE_FILE) build
	docker-compose -f $(COMPOSE_FILE) up

# 🔍 Logs en live
logs:
	docker logs -f $(SERVICE)

# 🛑 Stop conteneur
stop:
	docker stop $(SERVICE)

# 🚮 Supprimer conteneur
rm:
	docker rm -f $(SERVICE)

# 📝 Générer un rapport
report:
	docker exec $(SERVICE) python static/reports/generate_report.py
