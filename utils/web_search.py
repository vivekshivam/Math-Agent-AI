from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def web_search_and_generate(question):
    # Perform Google search via Serper API
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {"q": question}
    response = requests.post(url, headers=headers, json=data)
    search_results = response.json()

    context = "\n".join([item["snippet"] for item in search_results.get("organic", [])])

    # Prepare prompt
    prompt = f"""
You are a helpful math professor.
Answer the following math question step by step.

Question: {question}

Context (from search): {context}
"""

    # NEW SDK format
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4o" if you have access
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return completion.choices[0].message.content.strip()
