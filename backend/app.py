from flask import Flask,jsonify
from flask_cors import CORS

app= Flask(__name__)

CORS(app,origins='*')

@app.route("/",methods=['GET'])
def home():
    return jsonify({
        "success": True,
        "message": "DOC-AI Backend is running..."
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "success": True,
        "status": "healthy"
    })



if __name__ == "__main__":
    app.run(debug=True, port=5000)