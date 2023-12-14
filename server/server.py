#making a backend lightweight flask server

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image(): #this function uses our saved model to classify images
    print("Received a POST request to /classify_image")
    image_data = request.form['image_data']
    print("Received image data:", image_data)

    response = jsonify(util.classify_image(image_data)) #imported image data in request object from flask module (in base64 encodded string)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    print("Processing completed.")


if __name__ == "__main__":
    print("Starting Python Flask Server For Friends Celebrity Image Classification")

    util.load_saved_artifacts()
    #^load artifacts into saved memory to make predictions
    app.run(port=5000)
