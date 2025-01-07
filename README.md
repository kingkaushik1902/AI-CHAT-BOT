
# HRMS Chatbot Application

## Overview
The HRMS Chatbot Application is an AI-powered chatbot designed to streamline HR-related tasks such as querying leave balance, applying for leaves, and retrieving attendance records. Built using OpenAI's GPT models, the chatbot integrates with a Flask backend and MongoDB database, offering a modern, user-friendly interface for seamless interaction.

## Features
- **HRMS Functionalities**:
  - Query leave balance.
  - Apply for leaves with custom reasons.
  - Retrieve attendance records.
- **General Chatbot Capabilities**:
  - Responds to general queries using OpenAI's GPT models.
  - Supports multilingual inputs for enhanced accessibility.
- **Modern Frontend**:
  - Responsive design using HTML, CSS, and JavaScript.
  - Clean and intuitive UI with dynamic message handling.
- **Backend Integration**:
  - Flask-based backend to handle user requests.
  - MongoDB for storing HR data and chat history.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: MongoDB
- **AI Model**: OpenAI GPT (e.g., `gpt-3.5-turbo`, `gpt-4`)
- **Other Tools**: OpenAI API, Flask-CORS

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HRMS-Chatbot
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure MongoDB is running on your local machine or a specified server.
5. Set up your OpenAI API key in the `chatbot_config.py` file:
   ```python
   OPENAI_API_KEY = "your_openai_api_key"
   ```

## Running the Application
1. Start the Flask backend:
   ```bash
   python app.py
   ```
2. Open the `index.html` file in your browser.
3. Interact with the chatbot for HRMS queries or general questions.

## Usage Examples
- **Leave Balance Query**:
  - User: "What is my leave balance?"
  - Bot: "You have 12 days of leave remaining."
- **Leave Application**:
  - User: "Apply for leave on January 5 for a personal reason."
  - Bot: "Your leave request for January 5 has been submitted for approval."

## Project Structure
```
HRMS-Chatbot/
│
├── app.py              # Flask backend
├── chatbot_config.py   # Configuration file for API keys and database
├── index.html          # Frontend HTML file
├── style.css           # Frontend CSS file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── ...
```

## Future Enhancements
- Add authentication for employees.
- Implement advanced analytics for HR data.
- Enable file uploads for resumes or documents during recruitment.

## Contributors
- **Your Name** - Developer and Designer

## License
This project is licensed under the MIT License. See the LICENSE file for details.
