from flask import Flask, request, jsonify
import easyocr
from PIL import Image
import io
import numpy as np

app = Flask(__name__)
reader = easyocr.Reader(['en'], gpu=False)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Ripely OCR</title></head>
        <body style="font-family: Arial; text-align: center; padding-top: 50px;">
            <h1>Ripely OCR is Active 🥬</h1>
            <p>Upload your grocery receipt to <code>/scan</code> via a POST request.</p>
        </body>
    </html>
    '''


@app.route('/scan', methods=['POST'])
def scan():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        image_file = request.files['image']
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image_np = np.array(image)

        result = reader.readtext(image_np, detail=0)
        return jsonify({
            'status': 'success',
            'items_detected': [item.strip() for item in result if item.strip()]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
