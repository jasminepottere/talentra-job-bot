from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/apply', methods=['POST'])
def apply():
    try:
        data = request.get_json(force=True)  # 🔥 Fix: force JSON parsing
        print("Received preferences:", data)

        jobs = [
            {
                "title": "Frontend Developer",
                "company": "Google",
                "location": data.get("location", "Remote"),
                "salary": data.get("salary", "$120k+")
            },
            {
                "title": "Product Manager",
                "company": "Netflix",
                "location": data.get("location", "Remote"),
                "salary": data.get("salary", "$140k+")
            }
        ]

        return jsonify({"status": "success", "jobs": jobs})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
