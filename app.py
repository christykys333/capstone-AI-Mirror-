from flask import Flask, render_template, request, jsonify
import requests
import cv2
import base64
from PIL import Image
import io

app = Flask(__name__)

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image capture and upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), 400
    
    image_file = request.files['image']
    image_data = image_file.read()

    # Convert image to base64
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    # Send image to API
    response = requests.post('https://pre.cm/API.htm', json={'image': encoded_image})

    # Return API response
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
