from flask import Flask, request, render_template
import os
from utils.analyzer import analyze_log

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    suspicious = None
    total = None
    unique = None
    chart_data = None
    threat_levels = None
    attacks = None

    if request.method == "POST":
        file = request.files["logfile"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        result, suspicious, total, unique, threat_levels, attacks = analyze_log(path)

        # Top 5 IP
        top = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:5])

        chart_data = {
            "labels": list(top.keys()),
            "values": list(top.values())
        }

    return render_template(
        "index.html",
        result=result,
        suspicious=suspicious,
        total=total,
        unique=unique,
        suspicious_count=len(suspicious) if suspicious else 0,
        chart_data=chart_data,
        threat_levels=threat_levels,
        attacks=attacks
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))