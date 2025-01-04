from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.chicken_diseases_classification.utils.common import decodeImage
from src.chicken_diseases_classification.pipeline.predict import PredicationPipeline


os.putenv('LANG', 'en_us.UTF-8')
os.putenv('LC_ALL', 'en_us.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredicationPipeline(self.filename)


@app.route("/", methods =["GET"])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods =["GET","POST"])
@cross_origin()
def trainRoute():
    os.system('python main.py')
    return "Training done Sucessfully"


@app.route("/predict", methods =["POST"])
@cross_origin()
def predictionRoute():
    image = request.json['image']
    decodeImage(image, c1App.filename)
    result = c1App.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    c1App = ClientApp()
    app.run(host ='0.0.0.0', port = 5000)
