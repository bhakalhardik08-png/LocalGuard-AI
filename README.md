# 🏥 LocalGuard AI (India Edition)

An offline, privacy-first emergency medical triage and first-aid companion assistant powered completely locally by **Llama 3.2 3B**. Zero data tracking, zero API costs, and completely functional without an internet connection.

## 🚀 Vision & Key Features
- **Privacy-First Design:** All user inputs and inference tokens are processed locally using Ollama. No personal health information ever leaves the device.
- **Low-Latency Edge AI:** Optimized specifically for the compact Llama 3.2 3B model parameters, providing fast responses on standard consumer laptops or edge hardware.
- **Indian Health Infrastructure Context:** Fine-tuned via system instructions to provide support tailored for Indian environments, including references to the National Health Helpline (1075).
- **Strict Clinical Guardrails:** Engineered with explicit constraints to enforce hedging language, prevent diagnostic assumptions, issue immediate emergency warning triggers, and reject unsafe pediatric dosing calculations.

## ⚙️ Tech Stack
- **Model Engine:** Ollama (Llama 3.2 3B)
- **UI Framework:** Gradio (v6.0+)
- **Language:** Python 3.13

## 🛠️ Local Setup Instructions

### Prerequisites
1. Download and install [Ollama](https://ollama.com).
2. Pull the model locally via terminal:
   ```bash
   ollama run llama3.2
   ```

### Installation
1. Clone this repository to your machine.
2. Install the necessary lightweight application dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Launching the Application
Execute the primary execution script to launch the local web server:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:7860` to access the chat dashboard interface.
