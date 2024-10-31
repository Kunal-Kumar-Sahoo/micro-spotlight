from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from config.config import Config

class LLMManager:
    def __init__(self):
        self.llm = OllamaLLM(
            model=Config.OLLAMA_LLM_MODEL,
            base_url=Config.OLLAMA_BASE_URL,
            callback_manager=[StreamingStdOutCallbackHandler()],
            temperature=0.7
        )
    
    def get_llm(self):
        return self.llm