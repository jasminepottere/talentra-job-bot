from flask import Flask, request, jsonify
from linkedin_bot import run_bot  # make sure this script exists and is correct

app = Flask(__name__)

@app.route('/apply', methods=['POST'])
def apply():
    data = request.json
    print("Received preferences:", data)

    try:
        # Trigger real scraping logic
        jobs = run_bot(
            keywords=data.get("keywords", ""),
            location=data.get("location", ""),
            salary=data.get("salary", ""),
            remote_only=data.get("remoteOnly", False)
        )

        return jsonify({"status": "success", "jobs": jobs})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
