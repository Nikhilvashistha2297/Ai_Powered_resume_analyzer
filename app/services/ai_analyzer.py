import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're an expert resume reviewer."},
            {"role": "user", "content": f"Please review the following resume:\n{text}"}
        ]
    )

    return {"ai_feedback": response.choices[0].message.content}

