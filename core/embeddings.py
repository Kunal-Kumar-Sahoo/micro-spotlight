from langchain_ollama import OllamaEmbeddings
from config.config import Config

class EmbeddingManager:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(
            model=Config.OLLAMA_EMBED_MODEL,
            base_url=Config.OLLAMA_BASE_URL
        )
    
    def get_embeddings(self):
        return self.embeddings