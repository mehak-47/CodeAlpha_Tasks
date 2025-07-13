import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🌟 Sample FAQs
faqs = {
    "What is AI?": "AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that allows systems to learn and improve from experience without being explicitly programmed.",
    "What is Deep Learning?": "Deep Learning uses artificial neural networks to model and solve complex problems.",
    "How does a chatbot work?": "Chatbots understand user input using natural language processing and reply based on programmed responses or machine learning.",
    "What is Python?": "Python is a high-level programming language known for its readability and broad applications.",
    "What are neural networks?": "Neural networks are algorithms inspired by the human brain that recognize patterns and make decisions.",
    "What is natural language processing?": "NLP is a field of AI that helps machines understand and respond to human language.",
    "What is computer vision?": "Computer vision enables machines to interpret and process visual data from the world.",
    "What is supervised learning?": "Supervised learning is a machine learning technique where the model learns from labeled training data.",
    "What is unsupervised learning?": "Unsupervised learning is when the model tries to find patterns and relationships in unlabeled data.",
    "What is reinforcement learning?": "Reinforcement learning is a type of ML where agents learn by receiving rewards or penalties for actions.",
    "Is AI dangerous?": "AI is not dangerous by itself, but ethical use and control are very important.",
}

st.title("Chatty 🤖")
st.write("Hey there, My name is Chatty. I am a chatbot.")

user_question = st.text_input("Let's chat!")

if user_question:
    #Extract all questions from the dictionary (not answers)
    questions = list(faqs.keys())

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_question])

    # Get cosine similarity between user question and all FAQ questions
    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    # Find best match
    best_match_idx = similarity.argmax()
    best_score = similarity[0, best_match_idx]

    if best_score > 0.2:  # You can adjust this threshold
        best_question = questions[best_match_idx]
        answer = faqs[best_question]
        st.success(f"💬 {answer}")
    else:
        st.error("Sorry, I don't understand the question. Try rephrasing! 🙈")
