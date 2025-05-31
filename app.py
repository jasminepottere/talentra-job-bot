from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Webflow to fetch from here

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Received form data:", data)
    # 🔁 You can run your LinkedIn bot here with this data
    return {"status": "received"}

@app.route('/get-jobs', methods=['GET'])
def get_jobs():
    mock_jobs = [
        {
            "id": 1,
            "title": "UX Designer",
            "company": "Figma",
            "location": "Remote",
            "salary": "$110K–$135K",
            "tags": ["Remote", "Design", "Figma"]
        },
        {
            "id": 2,
            "title": "Product Manager",
            "company": "Notion",
            "location": "New York",
            "salary": "$130K–$160K",
            "tags": ["Hybrid", "PM", "Notion"]
        },
        {
            "id": 3,
            "title": "Frontend Engineer",
            "company": "Airbnb",
            "location": "San Francisco",
            "salary": "$150K–$180K",
            "tags": ["React", "Remote", "Frontend"]
        }
    ]
    return jsonify(mock_jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# added get-jobs route

