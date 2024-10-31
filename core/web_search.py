from duckduckgo_search import DDGS
from langchain_community.document_loaders import WebBaseLoader
from config.config import Config

class WebSearchManager:
    def __init__(self):
        self.ddgs = DDGS()
    
    def search(self, query):
        results = []
        for r in self.ddgs.text(query, max_results=Config.MAX_SEARCH_RESULTS):
            results.append(r)
        return results
    
    async def load_web_pages(self, urls):
        loader = WebBaseLoader(urls)
        return await loader.aload()