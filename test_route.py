import requests

BASE_URL = "http://localhost:5000"

ROUTES = {
    "/": "API en ligne",
    "/status": "Données système",
    "/detect": "Anomalies détectées",
    "/respond": "Réponse automatique",
    "/events": "Logs d’événements",
    "/report/generate": "Génération de rapport",
    "/about": "Page à propos",
    "/ui/status": "UI statut système",
    "/ui/test": "UI test notification"
}

def test_route(path, description):
    url = f"{BASE_URL}{path}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {path:<20} ({description})")
        else:
            print(f"❌ {path:<20} ({description}) — Code: {response.status_code}")
    except Exception as e:
        print(f"❌ {path:<20} ({description}) — Erreur: {e}")

if __name__ == "__main__":
    print("🧪 Test des routes SentinelOps :\n")
    for route, desc in ROUTES.items():
        test_route(route, desc)
