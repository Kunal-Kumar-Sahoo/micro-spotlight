from abc import ABC, abstractmethod
from langgraph.graph import Graph

class BaseAgent(ABC):
    def __init__(self, llm_manager, vector_store_manager):
        self.llm = llm_manager.get_llm()
        self.vector_store = vector_store_manager
    
    @abstractmethod
    def create_graph(self):
        pass
    
    @abstractmethod
    def process_query(self, query: str):
        pass