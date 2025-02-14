import requests
import xml.etree.ElementTree as ET
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .rag_pipeline import generate_summary
from backend.src.generate_embeddings import add_embeddings_to_chromadb


router = APIRouter()

# Pydantic model for the incoming request body
class QueryRequest(BaseModel):
    query: str  # Expecting a "query" field in the request body

def fetch_arxiv_papers(query: str, max_results: int = 5):
    """
    Fetches research papers from the ArXiv API based on the user query.
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch data from ArXiv API.")

    # Parse XML response
    root = ET.fromstring(response.text)

    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
        link = entry.find("{http://www.w3.org/2005/Atom}id").text  # This is the correct ID (URL)

        papers.append({
            "title": title,
            "summary": summary,
            "link": link
        })

    return papers

# Updated POST endpoint to receive the query parameter in the request body
@router.post("/summarize/")
async def summarize_paper(request: QueryRequest):
    try:
        query = request.query
        papers = fetch_arxiv_papers(query, max_results=5)
        summaries = []

        for paper in papers:
            add_embeddings_to_chromadb(paper['summary'], paper['title'])
            summary = generate_summary(paper['summary'])
            summaries.append({
                "title": paper["title"],
                "summary": summary,
                "link": paper["link"]
            })

        return {"summaries": summaries}

    except Exception as e:
        # Log the error on the backend to get more information in the terminal
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")
