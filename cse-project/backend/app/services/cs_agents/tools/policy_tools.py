import re
import requests
from langchain_core.tools import tool
from app.services.cs_agents.utils import VectorStoreRetriever
from app.core.config import settings
import openai
response = requests.get(
    "https://storage.googleapis.com/benchmarks-artifacts/travel-db/swiss_faq.md"
)
response.raise_for_status()
faq_text = response.text

docs = [{"page_content": txt} for txt in re.split(r"(?=\n##)", faq_text)]

retriever = VectorStoreRetriever.from_docs(docs, openai.Client(api_key=settings.OPENAI_API_KEY))

@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes performing other 'write' events."""
    docs = retriever.query(query, k=2)
    return "\n\n".join([doc["page_content"] for doc in docs])
