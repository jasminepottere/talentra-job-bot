from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/apply', methods=['POST'])
def apply():
    data = request.json
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
