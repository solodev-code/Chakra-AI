Chakar AI

Your Personal AI Assistant for Chat, Voice, Search, Automation & AI Tasks

Chakar AI is a Python-based intelligent personal assistant that combines AI conversation, voice interaction, real-time search, desktop automation, image generation, and task-oriented assistance in one application.

Chat → Understand → Search → Decide → Execute → Respond

✨ Features

🤖 AI Chat — Natural-language conversations and questions

🎯 Task-Oriented Assistance — Understand commands and perform supported tasks

🎙️ Speech-to-Text — Interact with Chakar using voice

🔊 Text-to-Speech — Receive spoken responses

🌐 Real-Time Search — Search the web for current information

⚙️ Desktop Automation — Execute supported computer actions

🖼️ Image Generation — Generate images using AI services

💬 Chat History — Store conversation data

🖥️ PyQt5 GUI — Desktop graphical interface

🌍 Translation — Translate supported text between languages

🎵 Media / YouTube Tasks — Perform supported media searches and actions

🧠 What Can Chakar AI Do?

💬 Conversation

What is Artificial Intelligence?
Explain Python.
How does Django work?
Give me project ideas.
Help me learn machine learning.

🎯 Task Execution

Open Chrome.
Open VS Code.
Open Calculator.
Search Google for Python tutorials.
Search YouTube for Django tutorials.

🎙️ Voice Interaction

"Hey Chakar, open Chrome."
"Search for Python tutorials."
"Tell me about machine learning."

🏗️ Architecture

                         ┌───────────────────┐
                         │       USER        │
                         └─────────┬─────────┘
                                   │
                          Text / Voice Input
                                   │
                                   ▼
                         ┌───────────────────┐
                         │       GUI         │
                         │     Frontend      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Command Processing│
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
                 AI Chat       Real-Time       Automation
                    │            Search            │
                    ▼              ▼               ▼
                 AI APIs       Web Search       Desktop
                    │            Engine           Tasks
                    └──────────────┼──────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │     Response      │
                         └─────────┬─────────┘
                                   │
                              ┌────┴────┐
                              ▼         ▼
                            Text      Voice

📁 Project Structure

Chakar-AI/
│
├── .vscode/
│   └── settings.json
│
├── Backend/
│   ├── Automation.py
│   ├── Chatbot.py
│   ├── gpt.py
│   ├── ImageGeneration.py
│   ├── Model.py
│   ├── RealtimeSearchEngine.py
│   ├── SpeechToText.py
│   └── TextToSpeech.py
│
├── Data/
│   ├── Chatlog.json
│   └── Voice.html
│
├── Frontend/
│   ├── Files/
│   │   ├── Database.data
│   │   ├── ImageGeneration.data
│   │   ├── Mic.data
│   │   ├── Responses.data
│   │   └── Status.data
│   │
│   ├── Graphics/
│   │   ├── Chats.png
│   │   ├── Close.png
│   │   ├── Home.png
│   │   ├── Jarvis.gif
│   │   ├── Maximize.png
│   │   ├── Mic_off.png
│   │   ├── Mic_on.png
│   │   ├── Minimize.png
│   │   ├── Minimize2.png
│   │   └── Settings.png
│   │
│   └── GUI.py
│
├── .env
├── Main.py
├── Requirements.txt
└── README.md

__pycache__ and .venv are local/generated files and should normally not be committed to GitHub.

🧩 Backend Modules

File

Purpose

Automation.py

Desktop and task automation

Chatbot.py

Chatbot and conversation logic

gpt.py

AI/LLM functionality

ImageGeneration.py

AI image generation

Model.py

Model-related functionality

RealtimeSearchEngine.py

Real-time web search

SpeechToText.py

Voice-to-text processing

TextToSpeech.py

Text-to-speech processing

🖥️ Frontend

The desktop interface is implemented in:

Frontend/GUI.py

Visual assets are stored in:

Frontend/Graphics/

Examples include:

Home.png

Chats.png

Settings.png

Mic_on.png

Mic_off.png

Jarvis.gif

Close.png

Minimize.png

Maximize.png

🗂️ Data

Application data is stored in the Data/ directory.

Data/
├── Chatlog.json
└── Voice.html

Chatlog.json is used for chat/conversation data.

🛠️ Technology Stack

Language

Python

AI / LLM

Groq

Cohere

AI model APIs

Voice & Audio

Edge TTS

Pygame

Speech-to-text components

Automation

AppOpener

PyWhatKit

Keyboard

Selenium

WebDriver Manager

Web

Requests

BeautifulSoup

Google Search

Selenium

GUI

PyQt5

Pillow

Rich

Utilities

python-dotenv

mtranslate

📦 Requirements

The project dependencies are listed in Requirements.txt.

python-dotenv
groq
AppOpener
pywhatkit
beautifulsoup4
Pillow
rich
requests
keyboard
cohere
googlesearch-python
selenium
mtranslate
pygame
edge-tts
PyQt5
webdriver-manager

🚀 Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/chakar-ai.git
cd chakar-ai

2. Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate

3. Install dependencies

pip install -r Requirements.txt

4. Configure environment variables

Create a .env file in the project root.

Example:

GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key

Use the variable names required by your actual source code.

5. Run Chakar AI

python Main.py

🔐 Environment & Security

Never publish API keys or other secrets.

Recommended .gitignore:

.venv/
venv/
__pycache__/
*.pyc
.env

Before pushing to GitHub, make sure .env is not tracked:

git status

If .env was previously committed, remove it from Git tracking and rotate the exposed API keys.

🔄 How Chakar AI Works

USER
  │
  ▼
Text / Voice Input
  │
  ▼
GUI
  │
  ▼
Command Processing
  │
  ├──────────────┬──────────────┐
  ▼              ▼              ▼
Chat           Search       Automation
  │              │              │
  ▼              ▼              ▼
AI API        Web Search     Desktop Task
  │              │              │
  └──────────────┼──────────────┘
                 ▼
             Response
                 │
           ┌─────┴─────┐
           ▼           ▼
         Text        Speech

💡 Example Commands

AI Chat

Hello Chakar.
What is artificial intelligence?
Explain machine learning.
Help me learn Python.
Give me project ideas.

Computer Tasks

Open Chrome.
Open VS Code.
Open Calculator.
Open Notepad.

Web Search

Search Google for Python tutorials.
Search YouTube for Django tutorials.
Find information about artificial intelligence.

Translation

Translate "Hello, how are you?" into Hindi.

🔮 Future Roadmap

🧠 Intelligence

Long-term memory

Better context awareness

Conversation memory

Intent classification

Multi-step task planning

Agent workflows

💻 Computer Control

File management

Application management

System monitoring

Mouse control

Keyboard control

Screenshot understanding

🌐 Online Services

Weather

News

Email

Calendar

Reminders

Maps

Additional service integrations

📚 Knowledge

PDF analysis

RAG

Personal knowledge base

Document search

Vector database

👁️ Multimodal AI

Image understanding

OCR

Screenshot analysis

Vision-based automation

Camera input

📱 Platforms

Web version

Android application

Mobile companion

Cloud synchronization

🔒 Safety

Chakar AI can interact with external services and, depending on its configuration, perform actions on the local computer.

For safe use:

Keep API keys private.

Review automation actions before using them.

Do not execute unknown code.

Keep dependencies updated.

Use a virtual environment.

Avoid giving the assistant unnecessary permissions.

⚠️ Disclaimer

Chakar AI is an educational and experimental personal AI assistant.

Some features may depend on:

Operating system

Installed applications

Internet connection

Browser configuration

Third-party APIs

API availability

Not every command is guaranteed to work on every system.

🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

git checkout -b feature/new-feature

Make your changes, test them, and submit a pull request.

📄 License

This project is currently intended for educational and personal development purposes.

If you plan to distribute the project publicly, add an appropriate open-source license after checking the licenses and terms of the project's dependencies, APIs, and included assets.

👨‍💻 Author

Your Name

GitHub: YOUR_GITHUB_URL

LinkedIn: YOUR_LINKEDIN_URL

⭐ Support

If you find Chakar AI useful or interesting, consider giving the repository a ⭐ on GitHub.

🚀 Chakar AI Vision

From Chatbot → AI Assistant → AI Agent

💬 CHAT
   ↓
🧠 UNDERSTAND
   ↓
🔎 SEARCH
   ↓
🎯 PLAN
   ↓
⚙️ EXECUTE
   ↓
🔊 RESPOND

Chakar AI — A personal AI assistant designed to chat, understand, search, and perform tasks. 🤖
