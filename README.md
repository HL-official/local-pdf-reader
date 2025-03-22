# Local PDF Reader with RAG

A local PDF reader that uses Retrieval-Augmented Generation (RAG) to answer questions about your PDF documents. The system uses:
- ChromaDB for vector storage
- Ollama (with Mistral model) for text generation
- LangChain for the RAG implementation

## Prerequisites

1. Python 3.9 or higher
2. [Ollama](https://ollama.ai) installed and running
3. Required Ollama models:
   - nomic-embed-text (for embeddings)
   - mistral (for text generation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HL-official/local-pdf-reader.git
cd local-pdf-reader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Ollama server:
```bash
ollama serve
```

4. Pull required models:
```bash
ollama pull nomic-embed-text
ollama pull mistral
```

## Usage

1. Place your PDF files in the `data` directory

2. Load documents into the vector database:
```bash
python3 load.py
```

3. Query your documents:
```bash
python3 Rag.py "your question here"
```

The output will show:
- Your query
- The AI-generated answer
- Source references to specific parts of the PDFs

