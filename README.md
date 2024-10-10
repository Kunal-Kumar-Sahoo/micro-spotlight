# $\mu$-llm

$\mu$-llm is an open-source project that mimics the behavior of macOS's Spotlight. It provides a powerful local search and question-answering system that leverages both local documents and internet resources using an Agentic AI approach.

## Features

- **Local Document Search**: Searches through specified directories and subdirectories for relevant information.
- **Internet Fallback**: If local information is insufficient, fetches answers from the internet.
- **Knowledge Graph Integration**: Uses a knowledge graph to store and retrieve information efficiently.
- **Vector Embeddings**: Utilizes vector embeddings for semantic search capabilities.
- **Microservices Architecture**: Designed with scalability in mind using a microservices pattern.
- **CLI and REST API**: Offers both a command-line interface and a REST API for flexible integration.
- **Docker Support**: Easy deployment using Docker containers.
- **Package Manager Installation**: Can be installed via package managers like APT or DNF.
- **File Change Monitoring**: Automatically updates the knowledge graph when local documents change.
- **Open-Source Friendly**: Simple file structure to facilitate easy contributions.
- **Robust Logging**: Comprehensive logging of all important metrics and operations.

## Architecture

$\mu$-llm is built using a microservices architecture with the following components:

1. **Backend Service**: Flask-based REST API for handling queries and orchestrating the search process.
2. **CLI Service**: Command-line interface for user interactions.
3. **Knowledge Graph Service**: Manages the knowledge graph and vector embeddings.
4. **File Watcher Service**: Monitors file changes in specified directories.
5. **Internet Search Service**: Handles fetching information from the internet when needed.

## Technologies Used

- **Backend Framework**: Flask
- **Language Model**: Quantized DataGemma model via Ollama
- **Knowledge Graph**: Neo4j
- **Vector Embeddings**: FAISS
- **AI Libraries**: LlamaIndex and LangChain
- **Containerization**: Docker
