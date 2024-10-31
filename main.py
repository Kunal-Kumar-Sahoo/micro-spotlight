import argparse
import asyncio
from core.llm import LLMManager
from core.embeddings import EmbeddingManager
from core.vector_store import VectorStoreManager
from core.document_loader import DocumentLoader
from agents.local_rag_agent import LocalRAGAgent
from agents.web_search_agent import WebSearchAgent

import os
os.environ["USER_AGENT"] = "RAGApplication/1.0"

class RAGApplication:
    def __init__(self):
        self.llm_manager = LLMManager()
        self.embedding_manager = EmbeddingManager()
        self.vector_store_manager = VectorStoreManager(self.embedding_manager)
        self.document_loader = DocumentLoader()
        
        self.local_agent = LocalRAGAgent(self.llm_manager, self.vector_store_manager)
        self.web_agent = WebSearchAgent(self.llm_manager, self.vector_store_manager)
    
    def load_documents(self, directory):
        documents = self.document_loader.load_documents(directory)
        self.vector_store_manager.add_documents(documents)
    
    async def process_query(self, query):
        # First try local RAG
        local_result = self.local_agent.process_query(query)
        
        # If local response is not confident, try web search
        if "I don't know" in local_result["response"] or "I'm not sure" in local_result["response"]:
            web_result = await self.web_agent.process_query(query)
            return web_result["response"]
        
        return local_result["response"]

def main():
    parser = argparse.ArgumentParser(description="RAG CLI Application")
    parser.add_argument("--docs", help="Directory containing documents")
    parser.add_argument("--query", help="Query to process")
    
    args = parser.parse_args()
    
    app = RAGApplication()
    
    if args.docs:
        app.load_documents(args.docs)
    
    if args.query:
        response = asyncio.run(app.process_query(args.query))
        print(f"\nAnswer: {response}")
    else:
        # Interactive mode
        while True:
            query = input("\nEnter your question (or 'quit' to exit): ")
            if query.lower() == 'quit':
                break
            
            response = asyncio.run(app.process_query(query))
            print(f"\nAnswer: {response}")

if __name__ == "__main__":
    main()