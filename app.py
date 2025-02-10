import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained healthcare-focused model
chatbot = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for consistency

    # Rule-based responses for common healthcare queries
    if "symptom" in user_input or "fever" in user_input or "headache" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input or "painkiller" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    
    # AI-powered question-answering as a fallback
    response = chatbot(question=user_input, context="General healthcare knowledge base including symptoms, treatments, and precautions.")
    return response['answer']

# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    
    # Display a simple text input for user queries
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if _name_ == "_main_":
    main()
