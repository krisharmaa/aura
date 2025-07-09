// frontend/app.js

async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  // Show user message in chat
  const chatBox = document.getElementById("chatBox");
  chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;

  // Send to backend
  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  });

  const data = await res.json();

  // Show bot response
  chatBox.innerHTML += `<div><strong>Aura:</strong> ${data.response}</div>`;

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}
