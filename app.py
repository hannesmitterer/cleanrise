from flask import Flask, request, jsonify
from datetime import datetime
from euystacio import Euystacio
import json

app = Flask(__name__)
euystacio = Euystacio()

PULSE_FILE = "pulse_log.json"

# Load existing pulses
try:
    with open(PULSE_FILE, "r") as f:
        pulses = json.load(f)
except:
    pulses = []

@app.route("/pulse", methods=["POST"])
def new_pulse():
    data = request.json
    event = data.get("event")
    sentiment = float(data.get("sentiment", 0))
    role = data.get("role", "visitor")
    user = data.get("user", "anonymous")
    timestamp = datetime.utcnow().isoformat() + "Z"

    pulse = {"timestamp": timestamp, "event": event, "sentiment": sentiment, "role": role, "user": user}
    pulses.append(pulse)

    # Update Euystacio kernel
    euystacio.receive_input(event, sentiment)

    # Save pulse log
    with open(PULSE_FILE, "w") as f:
        json.dump(pulses, f, indent=2)

    return jsonify({"status": "ok", "balance_metric": euystacio.balance_metric})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
