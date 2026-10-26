
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=os.environ["META_API_KEY"],
)

evidence = """
Fictional security incident:
09:12 - Employee receives a suspicious email.
09:18 - Five failed login attempts are recorded.
09:21 - A successful login occurs from an unfamiliar IP address.
09:25 - A sensitive file is downloaded.

No evidence currently identifies who performed the login.
"""

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
                "Do not invent evidence."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Review this evidence:\n{evidence}\n"
                "What is your initial hypothesis? "
                "What additional evidence would you investigate?"
            ),
        },
    ],
)

print("\n=== MUSE SPARK INVESTIGATION ===\n")
print(response.choices[0].message.content)
