import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Hugging Face Token
HF_TOKEN = os.getenv("HF_TOKEN")

# Model Configurations
MODELS = {
    "text_classification": {
        "model_name": "distilbert-base-uncased-finetuned-sst-2-english",
        "display_name": "Text Classification (Sentiment Analysis)",
        "task": "text-classification"
    },
    "ner": {
        "model_name": "dbmdz/bert-large-cased-finetuned-conll03-english", 
        "display_name": "Named Entity Recognition",
        "task": "ner"
    },
    "question_answering": {
        "model_name": "distilbert-base-cased-distilled-squad",
        "display_name": "Question Answering", 
        "task": "question-answering"
    },
    "summarization": {
        "model_name": "facebook/bart-large-cnn",
        "display_name": "Text Summarization",
        "task": "summarization"
    },
    "text_generation": {
        "model_name": "gpt2",
        "display_name": "Text Generation",
        "task": "text-generation"
    }
}

# Streamlit Page Configuration
PAGE_CONFIG = {
    "page_title": "NLP Eğitim Platformu",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}