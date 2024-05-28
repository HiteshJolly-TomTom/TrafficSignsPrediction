from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
import os
from model.predictor import predict_traffic_signs

app = Flask(__name__)
CORS(app)

# Configure file uploads
shapefiles = UploadSet('shapefiles', DOCUMENTS)
app.config['UPLOADED_SHAPEFILES_DEST'] = 'uploads'
configure_uploads(app, shapefiles)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        filename = shapefiles.save(request.files['file'])
        filepath = os.path.join(app.config['UPLOADED_SHAPEFILES_DEST'], filename)
        result = predict_traffic_signs(filepath)
        return jsonify(result=result)
    return jsonify(error="No file uploaded"), 400

if __name__ == '__main__':
    app.run(debug=True)
