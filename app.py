import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from chatbot_config import OPENAI_API_KEY, FLASK_CONFIG, MONGODB_CONFIG
import logging
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = openai.OpenAI()

ASSISTANT_ID = "USE YOUR ASSISTANT KEY"

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# MongoDB connection
client_mongo = MongoClient(MONGODB_CONFIG["uri"])
db = client_mongo[MONGODB_CONFIG["database_name"]]
employees_collection = db["employees"]
attendance_collection = db["attendance"]
leave_requests_collection = db["leave_requests"]
chat_collection = db[MONGODB_CONFIG["collection_name"]]

# HRMS
@app.route("/leave_balance", methods=["POST"])
def leave_balance():
    try:
        employee_id = request.json.get("employee_id")
        if not employee_id:
            return jsonify({"error": "Employee ID is required"}), 400

        # Fetch employee details from the database
        employee = employees_collection.find_one({"_id": employee_id})
        if not employee:
            return jsonify({"error": "Employee not found"}), 404

        return jsonify({"leave_balance": employee["leave_balance"]})

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/apply_leave", methods=["POST"])
def apply_leave():
    try:
        data = request.json
        employee_id = data.get("employee_id")
        leave_date = data.get("leave_date")
        reason = data.get("reason")

        if not (employee_id and leave_date and reason):
            return jsonify({"error": "Employee ID, leave date, and reason are required"}), 400

        # Add leave request to the database
        leave_requests_collection.insert_one({
            "employee_id": employee_id,
            "leave_date": leave_date,
            "reason": reason,
            "status": "Pending"
        })

        return jsonify({"message": "Leave request submitted successfully"})

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        if "leave balance" in user_message.lower():
            # Simulate fetching leave balance
            employee_id = "1"  # Hardcoded employee ID for testing
            return leave_balance()

        if "apply for leave" in user_message.lower():
            # Simulate leave application
            return apply_leave()

        # General chatbot queries using OpenAI Assistant
        thread = client.beta.threads.create()
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message,
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID,
        )

        if run.status != "completed":
            return jsonify({"error": "Assistant run failed"}), 500

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        bot_response = next(
            (msg.content[0].text.value for msg in messages if msg.role == "assistant" and msg.content[0].type == "text"),
            None
        )

        if not bot_response:
            return jsonify({"error": "No response from assistant"}), 500

        return jsonify({"response": bot_response})

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host=FLASK_CONFIG["host"], port=FLASK_CONFIG["port"], debug=FLASK_CONFIG["debug"])
