# 📬 Email Spam Classification using TF-IDF & Naive Bayes

A Machine Learning project that classifies email messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and a deployed Streamlit web interface.

---

## 🚀 Live Application

Run locally:
streamlit run app.py

📖 Project Overview

Email spam detection is a classic NLP problem in text classification.

This project implements a complete ML pipeline:

Text preprocessing

Feature engineering using TF-IDF

Multinomial Naive Bayes classification

Model serialization using Pickle

Interactive Streamlit Web App

The system predicts whether an email message is:

🚨 Spam

✅ Ham (Not Spam)

🧠 Machine Learning Pipeline
1️⃣ Data Preprocessing

Convert text to lowercase

Remove numbers

Remove punctuation

Clean unwanted characters

2️⃣ Feature Engineering

TF-IDF Vectorization

Converts text into numerical feature vectors

Captures word importance

3️⃣ Model Used

Multinomial Naive Bayes

Suitable for text classification problems

Fast and efficient for large vocabularies

4️⃣ Class Balancing

Spam and Ham classes were balanced before training to prevent bias.

📊 Dataset

SMS Spam Collection Dataset

Cleaned and structured

Stored inside dataset/spam.csv

Dataset format:

Label	Text
spam	Free entry in 2 a wkly comp...
ham	Hey, are we meeting today?
📂 Project Structure
Email-Spam-Classification-ML/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── dataset/
│   └── spam.csv
├── models/
│   └── spam_classifier.pkl
├── screenshots/
│   └── app_preview.png
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/Email-Spam-Classification-ML.git
cd Email-Spam-Classification-ML
2️⃣ Install Dependencies
pip install -r requirements.txt
🏋️ Model Training

To train the model:

python train_model.py

This generates:

models/spam_classifier.pkl
🌐 Run Web App
streamlit run app.py

Open browser:

http://localhost:8501
🖥 Application Preview

📈 Evaluation Metrics

Model performance evaluated using:

Precision

Recall

F1-Score

Classification Report

Naive Bayes performs efficiently for spam detection due to probabilistic modeling of word frequencies.

🛠 Technologies Used

Python

Scikit-learn

Pandas

TF-IDF Vectorizer

Multinomial Naive Bayes

Streamlit

Pickle

🎯 Key Learning Outcomes

✔ NLP preprocessing
✔ Text vectorization
✔ ML pipeline building
✔ Model persistence
✔ Web deployment using Streamlit
✔ Real-world text classification problem

🔮 Future Improvements

Add Confusion Matrix Visualization

Try Logistic Regression / SVM

Upgrade to Deep Learning (LSTM / BERT)

Deploy on Streamlit Cloud

Add REST API version
