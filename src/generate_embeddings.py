import chromadb
from sentence_transformers import SentenceTransformer
import uuid  # To generate unique IDs

# Initialize ChromaDB client and model for embeddings
client = chromadb.Client()
collection = client.create_collection("papers")
model = SentenceTransformer('all-MiniLM-L6-v2')  # Example: Use sentence-transformers to generate embeddings

def generate_embeddings(text: str):
    return model.encode(text).tolist()  # Convert to list format for ChromaDB compatibility

def add_embeddings_to_chromadb(paper_text: str, title: str):
    """
    Add the embeddings of the paper to the ChromaDB collection with a unique ID.
    """
    embeddings = generate_embeddings(paper_text)
    
    # Generate a unique ID for the paper (e.g., using its title or UUID)
    paper_id = str(uuid.uuid4())  # Generate a unique ID (UUID in this case)

    collection.add(
        ids=[paper_id],  # Add unique ID for the document
        documents=[paper_text],  # Adding the text of the paper
        metadatas=[{"title": title}],  # Metadata for identification
        embeddings=embeddings
    )
