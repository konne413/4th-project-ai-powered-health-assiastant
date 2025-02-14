import streamlit as st
from transformers import pipeline

# Load a pre-trained Question Answering model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    context = (
        "Healthcare is essential for well-being. If you have symptoms, consult a doctor. "
        "You can schedule appointments at hospitals or clinics. Medications should be taken as prescribed by a healthcare provider. "
        "A balanced diet, regular exercise, and mental health care are also important for overall health."
    )
    
    if "symptom" in user_input.lower():
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input.lower():
        return "Would you like me to help schedule an appointment with a doctor?"
    elif "medication" in user_input.lower():
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        result = qa_pipeline(question=user_input, context=context)
        return result["answer"]

# Streamlit web app interface
def main():
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="🩺")
    
    st.title("🩺 Healthcare Assistant Chatbot")
    st.markdown("💡 **Ask me about symptoms, medications, or appointments.**")

    user_input = st.text_area("How can I assist you today?", "")

    if st.button("Submit"):
        if user_input.strip():
            st.markdown(f"**🗣️ User:** {user_input}")
            response = healthcare_chatbot(user_input)
            st.markdown(f"**🤖 Healthcare Assistant:** {response}")
        else:
            st.warning("⚠️ Please enter a valid query.")

if __name__ == "__main__":
    main()
