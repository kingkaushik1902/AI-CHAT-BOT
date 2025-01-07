document.addEventListener("DOMContentLoaded", () => {
  const userInput = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");
  const chatbox = document.getElementById("chatbox");

  const appendMessage = (sender, message) => {
    const messageDiv = document.createElement("div");
    messageDiv.className = sender === "user" ? "message user" : "message bot";
    const timestamp = new Date().toLocaleTimeString();
    messageDiv.innerHTML = `
      <div class="message-content">${message}</div>
      <div class="timestamp">${timestamp}</div>
    `;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll
  };

  const showTypingIndicator = () => {
    const typingDiv = document.createElement("div");
    typingDiv.id = "typing-indicator";
    typingDiv.className = "message bot typing";
    typingDiv.innerHTML = `
      <div class="message-content">The bot is typing...</div>
    `;
    chatbox.appendChild(typingDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
  };

  const removeTypingIndicator = () => {
    const typingDiv = document.getElementById("typing-indicator");
    if (typingDiv) {
      chatbox.removeChild(typingDiv);
    }
  };

  const sendMessage = async () => {
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("user", message);
    userInput.value = ""; // Clear input field

    showTypingIndicator();

    try {
      const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      removeTypingIndicator();

      if (response.ok) {
        appendMessage("bot", data.response);
      } else {
        appendMessage("bot", `Error: ${data.error}`);
      }
    } catch (error) {
      removeTypingIndicator();
      appendMessage("bot", "Error connecting to server.");
    }
  };

  const autoReply = () => {
    setTimeout(() => {
      appendMessage("bot", "If you have more questions, feel free to ask!");
    }, 5000);
  };

  sendBtn.addEventListener("click", () => {
    sendMessage();
    autoReply();
  });

  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      sendMessage();
      autoReply();
    }
  });

  // Greeting message on load
  appendMessage("bot", "Welcome to the Alcantara Chatbot! How can I assist you today?");
});
