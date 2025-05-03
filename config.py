# config.py - Configuration settings for the financial assistant
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application settings
APP_NAME = "Financial Investment Assistant"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Data settings
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
VECTOR_DB_DIR = os.path.join(DATA_DIR, "vector_db")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Create directories if they don't exist
for directory in [DATA_DIR, VECTOR_DB_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR]:
    os.makedirs(directory, exist_ok=True)

# Web scraping settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# News sources configuration
NEWS_SOURCES = [
    {
        "name": "BloombergHT",
        "url": "https://www.bloomberght.com/piyasalar",
        "article_selector": ".card.card--news",
        "title_selector": "h3.card__title",
        "url_selector": "a.card__link",
        "base_url": "https://www.bloomberght.com"
    },
    {
        "name": "Investing.com TR",
        "url": "https://tr.investing.com/news/stock-market-news",
        "article_selector": ".largeTitle article",
        "title_selector": ".title",
        "url_selector": "a",
        "base_url": "https://tr.investing.com"
    }
]

# Model settings
EMBEDDING_MODEL = "dbmdz/bert-base-turkish-cased"
LLM_MODEL = "meta-llama/Llama-3-8b-hf"  # Example model, adjust based on availability
DEVICE = "cuda" if os.getenv("USE_GPU", "False").lower() == "true" else "cpu"

# RAG settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RETRIEVAL = 5

# API keys (stored in .env file)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# UI settings
PAGE_TITLE = "Financial Investment Assistant"
PAGE_ICON = "💰"
THEME = "light"