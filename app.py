import os
from flask import Flask, request, render_template
from utils.kb_search import search_kb
from utils.web_search import web_search_and_generate
from utils.feedback_handler import save_feedback
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    question = ""
    if request.method == "POST":
        question = request.form["question"]
        result = search_kb(question)
        if not result:
            result = web_search_and_generate(question)
    return render_template("index.html", result=result, question=question)

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.form
    save_feedback(data["question"], data["response"], data["feedback"])
    return "Thanks for your feedback!"

if __name__ == "__main__":
    app.run(debug=True)
