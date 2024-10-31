from langchain_chroma import Chroma
from config.config import Config

class VectorStoreManager:
    def __init__(self, embedding_manager):
        self.embedding_function = embedding_manager.get_embeddings()
        self.vector_store = Chroma(
            persist_directory=Config.CHROMA_PERSIST_DIR,
            embedding_function=self.embedding_function
        )
    
    def add_documents(self, documents):
        return self.vector_store.add_documents(documents)
    
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)