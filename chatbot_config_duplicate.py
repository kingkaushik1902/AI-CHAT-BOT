# Chatbot Configuration Template

# OpenAI API Key
OPENAI_API_KEY = "USE YOUR OPENAI KEY"

# Assistant ID
ASSISTANT_ID = "USE YOUR KEY"

# Flask Server Configuration
FLASK_CONFIG = {
    "host": "localhost",  # Host for the Flask server
    "port": 5000,         # Port for the Flask server
    "debug": True         # Debug mode (True/False)
}

# MongoDB Configuration
MONGODB_CONFIG = {
    "uri": "mongodb://localhost:27017",  # MongoDB URI
    "database_name": "chatbot",          # Name of your MongoDB database
    "collection_name": "chat_history"   # Name of the collection for chat history
}

# Default Chatbot Settings
CHATBOT_SETTINGS = {
    "max_tokens": 150,    # Maximum tokens for the AI response
    "temperature": 0.7,   # Creativity level (0.0 to 1.0)
    "top_p": 1.0          # Sampling probability
}
