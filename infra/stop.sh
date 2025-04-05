#!/bin/bash
echo "🛑 Arrêt du conteneur SentinelOps..."
docker-compose -f infra/docker-compose.yml down
