from flask import Flask, jsonify  # Flask creates the web app, jsonify returns JSON responses

app = Flask(__name__)  # create the application object


@app.route("/")  # home page, also used by the pipeline health check
def home():
    return "Hello from my DevOps web app!"  # plain text response with HTTP 200


@app.route("/health")  # dedicated health endpoint for monitoring
def health():
    return jsonify(status="ok")  # returns {"status": "ok"}


if __name__ == "__main__":
    # host 0.0.0.0 so the app is reachable from outside the Docker container
    app.run(host="0.0.0.0", port=8000)
