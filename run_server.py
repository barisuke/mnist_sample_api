import joblib
import flask
import numpy as np

# initialize our Flask application and pre-trained model
app = flask.Flask(__name__)
model = joblib.load("./trained-model/sample-model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    # ensure an feature was properly uploaded to our endpoint
    if flask.request.method == "POST":
        #print(flask.request.get_json())
        if flask.request.get_json().get("feature"):
            # read feature from json
            feature = flask.request.get_json().get("feature")
            # preprocess for classification
            # list  -> np.ndarray
            feature = np.array(feature).reshape((1, -1))

            # classify the input feature
            response["prediction"] = model.predict(feature).tolist()

            # indicate that the request was a success
            response["success"] = True
    # return the data dictionary as a JSON response
    return flask.jsonify(response)


if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run()