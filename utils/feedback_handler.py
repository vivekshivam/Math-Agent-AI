def save_feedback(question, response, feedback):
    with open("data/feedback_log.txt", "a") as f:
        f.write(f"Q: {question}\nResponse: {response}\nFeedback: {feedback}\n---\n")
