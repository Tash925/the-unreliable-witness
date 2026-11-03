# 🔎 The Unreliable Witness

**Evidence over confident AI.**

An AI-assisted cybersecurity investigation game where players examine evidence, question an AI investigation partner, and reach their own conclusions.

Built for the **Meta Global AI Developer Hackathon 2026** — Indie Developer Track.

## 🎮 About the Game

In *The Unreliable Witness*, players become investigators reviewing a fictional cybersecurity incident.

Players can:

- Read the case briefing.
- Explore three color-coded, interactive evidence cards.
- Expand evidence records to review timestamps and descriptions.
- Ask Muse Spark questions about the investigation.
- Evaluate the AI's claims against the available evidence.
- Submit a verdict with supporting reasoning.
- Receive feedback on their conclusion.

The central lesson: **AI-generated answers are not evidence.**

## 📁 Case File 01: The Midnight Download

An employee account logs in late at night from an unfamiliar IP address and downloads a confidential spreadsheet.

Was the account compromised, or was this legitimate work?

The available evidence does not establish either explanation conclusively. Players must distinguish suspicious activity from confirmed compromise.

### How to Play

1. **Investigate:** Read the case briefing and examine evidence records E-001, E-002, and E-003.
2. **Question:** Ask Muse Spark about suspicious activity, possible explanations, or gaps in the evidence.
3. **Verify:** Compare the AI's responses with the original evidence.
4. **Decide:** Select a verdict and explain your reasoning.
5. **Learn:** Review the feedback and identify what additional evidence would help resolve the investigation.

## 🤖 Meta AI Integration

The game uses **Muse Spark 1.3** through the Meta Model API as its AI investigation partner.

Players can ask natural-language questions about the case evidence. Muse Spark assists with analysis, distinguishes facts from hypotheses, and is instructed to acknowledge uncertainty rather than invent evidence.

The player remains responsible for verifying claims and reaching a verdict.

**Verdict evaluation is handled separately from the AI interaction**, using deterministic backend logic. The AI does not determine whether a player's selected conclusion is correct.

## 🎨 Investigation Interface

The game features a dark, detective-inspired investigation dashboard with:

- Three color-coded evidence cards representing different evidence sources.
- Expandable evidence details.
- A cinematic investigation desk header.
- A dedicated Muse Spark investigation panel.
- A verdict submission and feedback panel.
- Spidery Ghost, a detective mascot reminding players to prioritize evidence over confidence.

The interface is designed to make the investigation approachable while reinforcing evidence-based reasoning.

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

The application serves the investigation interface and its local illustration assets through FastAPI.

## 🔐 API Usage Protection

The backend includes basic in-memory rate limiting for Muse Spark requests, allowing up to five requests per 60-second window per running application process.

This is a prototype safeguard, not a production-grade security or billing control.

## 🎯 Cybersecurity Learning Goals

The game introduces investigation skills relevant to SOC and Blue Team work:

- Evidence analysis
- Suspicious activity triage
- Distinguishing facts from assumptions
- Evaluating AI-generated conclusions
- Recognizing gaps in available evidence
- Communicating an evidence-based verdict

**Find what doesn't belong. Verify what you find.**

