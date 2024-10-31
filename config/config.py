import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Ollama Configuration
    OLLAMA_BASE_URL = "http://localhost:11434"
    OLLAMA_EMBED_MODEL = "nomic-embed-text"
    OLLAMA_LLM_MODEL = "mistral"
    
    # Vector Store Configuration
    CHROMA_PERSIST_DIR = "./chroma_db"
    
    # Web Search Configuration
    MAX_SEARCH_RESULTS = 5
    
    # Document Processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200