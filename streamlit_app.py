import streamlit as st
from dotenv import load_dotenv
import os
from utils.kb_search import search_kb
from utils.web_search import web_search_and_generate
from utils.feedback_handler import save_feedback

load_dotenv()

st.set_page_config(page_title="Math AI Agent", page_icon="🧠", layout="centered")
st.title("🤖 Math AI Agent")
st.markdown("Enter your math question below. The agent will first try the Knowledge Base, then fallback to GPT-4 if needed.")

# Input
question = st.text_input("📌 Enter your question:")

# Initialize session state variables
if "last_result" not in st.session_state:
    st.session_state.last_result = ""
if "last_question" not in st.session_state:
    st.session_state.last_question = ""

# Get Answer
if st.button("Get Answer"):
    if question.strip():
        answer = search_kb(question)
        if answer:
            st.success("📚 Answer from Knowledge Base:")
        else:
            st.info("🤖 Not found in KB. Asking GPT-4...")
            answer = web_search_and_generate(question)

        st.markdown(answer)
        st.session_state.last_question = question
        st.session_state.last_result = answer
    else:
        st.warning("Please enter a valid question.")

# Feedback Section
st.markdown("---")
st.subheader("💬 Feedback")
feedback = st.text_area("What did you think of the answer?")

if st.button("Submit Feedback"):
    if feedback:
        prev_q = st.session_state.get("last_question", "")
        prev_r = st.session_state.get("last_result", "")
        if prev_q and prev_r:
            save_feedback(prev_q, prev_r, feedback)
            st.success("✅ Feedback submitted!")
        else:
            st.error("⚠️ Please generate an answer before submitting feedback.")
    else:
        st.warning("Please enter your feedback.")
