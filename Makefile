.PHONY: up down rebuild stop logs rm clean report restart fix free-port

# 📦 Nom du service
SERVICE=sentinelops

# 🧠 Chemin absolu vers la racine du projet
ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

# 🔧 Entrer dans le bon dossier avant chaque commande
up:
	cd $(ROOT_DIR) && docker-compose up -d --build

down:
	cd $(ROOT_DIR) && docker-compose down

rebuild:
	cd $(ROOT_DIR) && docker-compose down
	cd $(ROOT_DIR) && docker-compose build
	cd $(ROOT_DIR) && docker-compose up -d

stop:
	docker stop $(SERVICE)

logs:
	docker logs -f $(SERVICE)

rm:
	docker rm -f $(SERVICE)

clean:
	docker rm -f $$(docker ps -a --filter "ancestor=sentinelops" --format "{{.ID}}") || true

report:
	docker exec $(SERVICE) python static/reports/generate_report.py

restart:
	docker-compose restart

free-port:
	@echo "🔐 Demande d'accès root pour libérer le port 5000..."
	@sudo true
	@pid=$$(sudo lsof -ti tcp:5000); \
	if [ -n "$$pid" ]; then \
		echo "🛑 Processus trouvé sur le port 5000 (PID=$$pid). Arrêt..."; \
		sudo kill -9 $$pid; \
		echo "✅ Port 5000 libéré."; \
	else \
		echo "✅ Aucun processus sur le port 5000."; \
	fi

fix:
	@$(MAKE) down
	@$(MAKE) free-port
	@$(MAKE) up

# ⚙️ Vérifie qui occupe un port (par défaut : 5000)
check-port:
	@PORT=5000; \
	echo "🔍 Vérification du port $$PORT..."; \
	pid=$$(sudo lsof -ti tcp:$$PORT); \
	if [ -n "$$pid" ]; then \
		echo "🛑 Port $$PORT utilisé par le PID $$pid :"; \
		sudo lsof -n -i :$$PORT | grep LISTEN; \
		read -p '💣 Voulez-vous tuer ce processus ? (y/N) ' confirm; \
		if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
			sudo kill -9 $$pid && echo "✅ Processus $$pid tué."; \
		else \
			echo "❌ Annulé, le port reste occupé."; \
		fi; \
	else \
		echo "✅ Aucun processus ne bloque le port $$PORT."; \
	fi

check-port-ci:
	@PORT=5000; \
	echo "🤖 CI ➜ Libération automatique du port $$PORT..."; \
	pid=$$(sudo lsof -ti tcp:$$PORT); \
	if [ -n "$$pid" ]; then \
		if systemctl is-active --quiet sentinelapi.service; then \
			echo '🛑 Service systemd détecté ➜ arrêt...'; \
			sudo systemctl stop sentinelapi.service; \
		fi; \
		sudo kill -9 $$pid && echo "✅ Port $$PORT libéré (PID $$pid tué)."; \
	else \
		echo "✅ Port $$PORT libre."; \
	fi