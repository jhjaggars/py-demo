import os

from cloudevents.http import from_http
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    event = from_http(request.headers, request.get_data())

    app.logger.warning(event)

# you can access cloudevent fields as seen below
    print(
        f"Found {event['id']} from {event['source']} with type "
        f"{event['type']} and specversion {event['specversion']}"
    )

    return "", 204

if __name__ == "__main__":
    app.run(debug=True,
            host=os.environ.get("HOSTNAME", "0.0.0.0"),
            port=int(os.environ.get("PORT", 3000)))
