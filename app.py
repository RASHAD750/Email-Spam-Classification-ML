import streamlit as st
import pickle
import re
import string

# Load model
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# UI
st.title("📬 Spam vs. Ham Email Classifier")
st.write("Enter an email message below. The model will predict whether it is spam or ham.")

input_text = st.text_area("✉️ Email Content")

if st.button("Classify"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        cleaned = preprocess(input_text)
        prediction = model.predict([cleaned])[0]
        if prediction == "spam":
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is HAM (not spam).")
