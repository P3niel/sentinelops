import subprocess

# 🛡️ Liste des services critiques à surveiller
CRITICAL_SERVICES = ["sshd", "docker", "cron"]

def check_service_status(service_name):
    try:
        result = subprocess.run(["systemctl", "is-active", service_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                check=False)
        return result.stdout.strip() == "active"
    except Exception as e:
        return False

def get_failing_services():
    failing = []
    for service in CRITICAL_SERVICES:
        if not check_service_status(service):
            failing.append(service)
    return failing
