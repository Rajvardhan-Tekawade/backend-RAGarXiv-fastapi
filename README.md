Backend (FastAPI)

Academic Paper Summarizer Backend (RAG + FastAPI) (for the IIT Kanpur+BoltIOT AI&ML internship project)

This is the backend service for Ragarxiv, an academic paper summarizer that retrieves research papers from arXiv and generates concise summaries using Hugging Face's facebook/bart-large-cnn model. It utilizes FastAPI for API development, ChromaDB as a vector database, and Hugging Face Transformers for NLP-based summarization.


---

Installation and Setup

1. Clone the Repository

git clone https://github.com/Rajvardhan-Tekawade/backend-RAGarXiv-fastapi
cd backend

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3. Install Dependencies

pip install -r requirements.txt

This will install all necessary libraries, including FastAPI, Uvicorn, ChromaDB, and Transformers.

4. Set Up Environment Variables

1. Create a .env file inside the src/ directory.


2. Add the following details (get your Hugging Face API token as described below):

HUGGINGFACE_API_KEY=your_huggingface_api_key



5. Get Your Own Hugging Face API Key

1. Go to Hugging Face.


2. Sign in or create an account.


3. Generate a new API token with "read" access.


4. Copy the token and add it to your .env file.



6. Run the FastAPI Server

uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

The backend should now be running at:
http://127.0.0.1:8000/docs (Swagger UI)
http://127.0.0.1:8000/redoc (Alternative API docs)


---

Endpoints

POST /summarize/ → Accepts a research query and returns summarized academic papers.

GET /papers/ → Fetches academic papers from arXiv and stores embeddings in ChromaDB.



---

FAQ

Do I need to manually download bart-large-cnn?

No, the facebook/bart-large-cnn model will be automatically downloaded the first time you run the script. If the server has internet access, it will fetch and cache the model.
