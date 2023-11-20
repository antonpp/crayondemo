from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    country = request.args.get("country")
    if country:
        return f"Welcome to {country}!!!!"
    else:
        return "Please provide a country as input."

if __name__ == "__main__":
    app.run(port=8080)
