
# 🔎 The Unreliable Witness

**Evidence over confident AI.**

An AI-assisted cybersecurity investigation game where players must examine evidence, question an AI investigation partner, and reach their own conclusions.

Built for the **Meta Global AI Developer Hackathon 2026** — Indie Developer Track.

## 🎮 About the Game

In *The Unreliable Witness*, players become investigators reviewing a fictional cybersecurity incident.

Players can:

- Read the case briefing.
- Examine timestamped evidence records.
- Ask an AI investigation partner questions.
- Evaluate the AI's claims against the evidence.
- Submit a verdict with supporting reasoning.
- Receive feedback on their conclusion.

The central lesson: **AI-generated answers are not evidence.**

## 📁 Case File 01: The Midnight Download

An employee account logs in late at night from an unfamiliar IP address and downloads a confidential spreadsheet.

Was the account compromised, or was this legitimate work?

The available evidence does not establish either explanation conclusively. Players must distinguish suspicious activity from confirmed compromise.

## 🤖 Meta AI Integration

The game uses **Muse Spark 1.3** through the Meta Model API as its AI investigation partner.

Players can ask questions about the case evidence. The AI assists with analysis, but the player remains responsible for verifying claims and reaching a verdict.

Verdict evaluation is handled separately from the AI interaction.

## 🛠️ Tech Stack

- Python
- FastAPI
- HTML, CSS, JavaScript
- Meta Model API — Muse Spark 1.3
- OpenAI-compatible Python SDK
- GitHub Codespaces

## 🚀 Run Locally

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Tash925/the-unreliable-witness.git
cd the-unreliable-witness
```

Create a Python virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set your Meta API key as an environment variable:

```bash
export META_API_KEY="your_meta_api_key"
```

Never commit API keys to the repository.

Start the application:

```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000` in your browser.

## 🔐 API Usage Protection

The backend includes basic in-memory rate limiting for AI requests to reduce excessive API usage.

This is a prototype safeguard, not a production-grade security or billing control.

## 🎯 Cybersecurity Learning Goals

The game introduces investigation skills relevant to SOC and Blue Team work:

- Evidence analysis
- Suspicious activity triage
- Distinguishing facts from assumptions
- Evaluating AI-generated conclusions
- Communicating an evidence-based verdict

## 💜 DataSec Labs

*The Unreliable Witness* is **DataSec Labs Case File 02**, part of the DataSec Chronicles learning ecosystem.

**Find what doesn't belong. Verify what you find.**

