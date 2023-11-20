from flask import Flask, request
import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="gke-dja-demo", location="europe-west4")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 2048,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    country = request.args.get("country")
    if country:
        response = model.predict(
            """Write me a 3 day trip plan for {}.""".format(country),
            **parameters
        )
        resp = response.text
        return resp
    else:
        return "Please provide a country as input."

if __name__ == "__main__":
    app.run(port=8080)
