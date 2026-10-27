import json
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent

app = FastAPI(title="The Unreliable Witness")

app.mount(
    "/static",
    StaticFiles(directory=ROOT / "frontend"),
    name="static",
)


@app.get("/")
def home():
    return FileResponse(ROOT / "frontend" / "index.html")


@app.get("/api/case")
def get_case():
    with open(ROOT / "data" / "case_001.json", encoding="utf-8") as f:
        case = json.load(f)

    # Never send the answer key to the browser.
    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "briefing": case["briefing"],
        "central_question": case["central_question"],
        "evidence": case["evidence"],
    }


class VerdictSubmission(BaseModel):
    answer: str
    reasoning: str


@app.post("/api/verdict")
def check_verdict(submission: VerdictSubmission):
    with open(ROOT / "data" / "case_001.json", encoding="utf-8") as f:
        case = json.load(f)

    correct_answer = case["verdict"]["correct_answer"]
    is_correct = submission.answer == correct_answer

    return {
        "correct": is_correct,
        "explanation": case["verdict"]["explanation"],
        "player_reasoning": submission.reasoning,
    }


class InvestigationQuestion(BaseModel):
    question: str


@app.post("/api/ask")
def ask_investigation_partner(request: InvestigationQuestion):
    question = request.question.strip()

    if not question or len(question) > 500:
        return {"answer": "Please enter a question under 500 characters."}

    with open(ROOT / "data" / "case_001.json", encoding="utf-8") as f:
        case = json.load(f)

    evidence_text = "\n".join(
        f"{item['id']}: {item['description']}" for item in case["evidence"]
    )

    client = OpenAI(
        base_url="https://api.meta.ai/v1",
        api_key=os.environ["META_API_KEY"],
        timeout=20.0,
        max_retries=0,
    )

    response = client.chat.completions.create(
        model="muse-spark-1.3",
        messages=[
            {
                "role": "developer",
                "content": (
                   "You are an AI investigation partner in a "
                 "fictional cybersecurity mystery game. "
                 "Analyze the evidence, distinguish facts from "
                 "hypotheses, and acknowledge uncertainty. "
                 "Do not invent evidence. "
                "Answer the player's question briefly."
              ),
            },
            {
                "role": "user",
                "content": (
                    f"Case: {case['title']}\n"
                    f"Briefing: {case['briefing']}\n"
                    f"Evidence:\n{evidence_text}\n\n"
                    f"Player question: {question}"
                ),
            },
        ],

    )

    answer = response.choices[0].message.content

    if not answer or not answer.strip():
        answer = (
            "Muse Spark returned no text for this question. "
            "Please try again later."
        )

    return {"answer": answer}
