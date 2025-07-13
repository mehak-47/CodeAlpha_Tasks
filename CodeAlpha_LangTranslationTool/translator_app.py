import streamlit as st
from deep_translator import GoogleTranslator

# Title and subtitle
st.title("🌍 Language Translator")
st.write("Translate text from one language to another using Google Translate API!")

# User input
text = st.text_area("Enter text to translate:")

# Language dictionary
languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh-cn"
}

# Dropdowns for language selection
source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated = GoogleTranslator(source=source_lang.lower(), target=target_lang.lower()).translate(text)
        st.success(f"**Translated Text:** {translated}")

