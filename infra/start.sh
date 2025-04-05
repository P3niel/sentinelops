#!/bin/bash

docker rm -f sentinelops 2>/dev/null

echo "🔁 Build & lancement du conteneur SentinelOps (depuis infra)..."
docker-compose -f infra/docker-compose.yml up --build -d
docker-compose -f infra/docker-compose.yml logs -f
