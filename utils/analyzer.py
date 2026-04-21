from collections import Counter

def classify_threat(count):
    if count > 10:
        return "HIGH"
    elif count > 5:
        return "MEDIUM"
    else:
        return "LOW"

def analyze_log(filepath):
    ips = []
    attacks = {}

    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if parts:
                ip = parts[0]
                ips.append(ip)

                # Detect attack
                if "/admin" in line:
                    attacks[ip] = "Admin Scan"
                elif "/login" in line:
                    attacks[ip] = "Brute Force"

    counter = Counter(ips)

    suspicious = {ip: c for ip, c in counter.items() if c > 5}
    threat_levels = {ip: classify_threat(c) for ip, c in counter.items()}

    total = len(ips)
    unique = len(counter)

    return counter, suspicious, total, unique, threat_levels, attacks