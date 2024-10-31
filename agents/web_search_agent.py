from agents.base_agent import BaseAgent
from core.web_search import WebSearchManager
from langchain.prompts import PromptTemplate
from langgraph.graph import Graph, StateGraph
from typing import Dict, Any

class WebSearchAgent(BaseAgent):
    def __init__(self, llm_manager, vector_store_manager):
        super().__init__(llm_manager, vector_store_manager)
        self.web_search = WebSearchManager()
        self.graph = self.create_graph()
    
    def create_graph(self):
        workflow = StateGraph(StateGraph.basic_schema())
        
        def search_web(state: Dict[str, Any]) -> Dict[str, Any]:
            query = state["input"]
            results = self.web_search.search(query)
            return {"input": query, "results": results}
        
        def process_results(state: Dict[str, Any]) -> Dict[str, Any]:
            template = """Based on the following search results, answer the question:
            Search Results: {results}
            Question: {question}
            Answer: """
            
            prompt = PromptTemplate(
                template=template,
                input_variables=["results", "question"]
            )
            
            results_text = "\n".join([r["body"] for r in state["results"]])
            final_prompt = prompt.format(results=results_text, question=state["input"])
            
            response = self.llm(final_prompt)
            return {"input": state["input"], "response": response, "source": "web"}
        
        # Add nodes
        workflow.add_node("search", search_web)
        workflow.add_node("process", process_results)
        
        # Add edges
        workflow.set_entry_point("search")
        workflow.add_edge("search", "process")
        workflow.set_finish_point("process")
        
        return workflow.compile()
    
    def process_query(self, query: str):
        return self.graph.invoke({"input": query})