from langchain_ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
    # Comment out or remove the Bedrock embeddings
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    # Use Ollama embeddings instead
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings