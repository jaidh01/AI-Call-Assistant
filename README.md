# AI-Call-Assistant

A lightweight **voice-enabled chatbot** built using the **Phi-3 Mini** language model, deployed entirely on an **Azure Virtual Machine (VM)** and enhanced with voice input/output for a seamless conversational experience.

---

## 📑 Table of Contents
- Features  
- Tech Stack  
- Architecture & Usage  
- Deployment Details  
- Future Improvements  
- Installation Guide  
- Contributing  
- License & Contact  

---

## 🚀 Features
- 🎤 Voice-enabled input and output for natural, spoken interactions.  
- 💬 Text-based chat as standard fallback.  
- ⚡ Powered by the **Phi-3 Mini** model for efficient and responsive language processing.  
- 🎨 Clean, responsive UI with styled sidebar and chat window.  

---

## 🛠 Tech Stack
| Component       | Description                               |
|-----------------|-------------------------------------------|
| **Front-end**   | HTML & CSS (modern, dark-themed UI)       |
| **Back-end**    | Python (FastAPI or Flask suggested)       |
| **AI Model**    | Phi-3 Mini (Azure-hosted)                 |
| **Hosting**     | Azure VM + ngrok for tunneling            |

---

## 🧩 Architecture & Usage
1. **Voice Interaction** – Use the *Speak* button to start a voice input prompt. The app listens, transcribes, and forwards your message to the AI.  
2. **Text Fallback** – Input field and *Send* button available for text queries.  
3. **Chat Flow** – User input (voice or text) → transcribed → sent to model → response displayed (and optionally spoken back).  

---

## ☁️ Deployment Details
- Hosted on an **Azure Virtual Machine**, offering full control over environment and resources.  
- Uses **ngrok** to expose the local server temporarily for external access.  
- Built to be easily containerized with **Docker** and scalable with load balancers.  

---

## 🔮 Future Improvements
- 🔒 Add authentication (OAuth2 / Firebase Auth / JWT)  
- 🗄️ Store conversation logs in PostgreSQL / MongoDB  
- ⏳ Streaming responses to display model replies as they generate  
- 🗣️ Improve voice quality and naturalness (e.g., Eleven Labs TTS)  
- 🐳 Dockerize + orchestrate with a load balancer  

---

## ⚙️ Installation Guide

```bash
# 1. Clone the repo
git clone https://github.com/jaidh01/AI-Call-Assistant.git
cd AI-Call-Assistant

# 2. Set up your environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure Environment Variables
# Create a .env file and add your Azure credentials:
# AZURE_OPENAI_ENDPOINT=your_endpoint_here
# AZURE_OPENAI_KEY=your_api_key_here

# 4. Run the App
python main.py

# 5. (Optional) Expose with ngrok
ngrok http 8000

# 6. Open in Browser
# Navigate to http://localhost:8000 or your ngrok URL
```
## 🤝 Contributing

Contributions are welcome! 🎉  

- Report issues or request features  
- Submit pull requests with enhancements  
- Help improve documentation  
