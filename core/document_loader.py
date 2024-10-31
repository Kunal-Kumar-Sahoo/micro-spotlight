from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.config import Config
import os

class DocumentLoader:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
    
    def load_documents(self, directory_path):
        loader = DirectoryLoader(directory_path, recursive=True)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)