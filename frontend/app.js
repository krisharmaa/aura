const form = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatbox = document.getElementById('chatbox');
const subtitle = document.getElementById('subtitle');

// Animate subtitle like a typewriter
function typeSubtitle(text) {
  let i = 0;
  subtitle.textContent = '';
  const interval = setInterval(() => {
    if (i < text.length) {
      subtitle.textContent += text.charAt(i);
      i++;
    } else {
      clearInterval(interval);
    }
  }, 100);
}

typeSubtitle("type anything...");

// Append a message to the chatbox
function appendMessage(label, text, className) {
  const msg = document.createElement('div');
  msg.className = `message ${className}`;
  msg.textContent = `${label}: `;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;

  if (className === 'ai') {
    let i = 0;
    const typingInterval = setInterval(() => {
      if (i < text.length) {
        msg.textContent += text.charAt(i);
        i++;
        chatbox.scrollTop = chatbox.scrollHeight;
      } else {
        clearInterval(typingInterval);
      }
    }, 30);
  } else {
    msg.textContent += text;
  }
}

// Fetch AI response from the backend
async function fetchAuraResponse(prompt) {
  try {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: prompt })
    });

    if (!res.ok) throw new Error("Response not OK");

    const data = await res.json();
    return data.response || "Hmm... something went wrong.";
  } catch (err) {
    console.error("Error fetching response:", err);
    return "Oops, I couldn't reach Aura.";
  }
}

// Handle form submission
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = userInput.value.trim();
  if (!input) return;

  appendMessage("You", input, "user");
  userInput.value = '';
  userInput.disabled = true;

  const aiReply = await fetchAuraResponse(input);
  appendMessage("Aura", aiReply, "ai");

  userInput.disabled = false;
  userInput.focus();
});
