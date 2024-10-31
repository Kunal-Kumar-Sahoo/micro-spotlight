from agents.base_agent import BaseAgent
from langchain.prompts import PromptTemplate
from langgraph.graph import Graph, StateGraph
from typing import Dict, Any


class LocalRAGAgent(BaseAgent):
    def __init__(self, llm_manager, vector_store_manager):
        super().__init__(llm_manager, vector_store_manager)
        self.graph = self.create_graph()
    
    def create_graph(self):
        workflow = StateGraph(StateGraph.basic_schema())

        def retrieve(state: Dict[str, Any]) -> Dict[str, Any]:
            query = state["input"]
            docs = self.vector_store.similarity_search(query)
            return {"input": query, "docs": docs}
        
        def generate_answer(state: Dict[str, Any]) -> Dict[str, Any]:
            template = """Answer the question based on the following context:
            Context: {context}
            Question: {question}
            Answer: """
            
            prompt = PromptTemplate(
                template=template,
                input_variables=["context", "question"]
            )
            
            context = "\n".join([doc.page_content for doc in state["docs"]])
            final_prompt = prompt.format(context=context, question=state["input"])
            
            response = self.llm(final_prompt)
            return {"input": state["input"], "response": response, "source": "local"}
        
        # Add nodes
        workflow.add_node("retrieve", retrieve)
        workflow.add_node("generate", generate_answer)
        
        # Add edges
        workflow.set_entry_point("retrieve")
        workflow.add_edge("retrieve", "generate")
        workflow.set_finish_point("generate")
        
        return workflow.compile()
    
    def process_query(self, query: str):
        return self.graph.invoke({"input": query})