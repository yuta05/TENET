import re
import os
from langchain_core.tools import tool
from app.services.cs_agents.utils import VectorStoreRetriever
from app.core.config import settings
import openai

# policy.txt ファイルを読み込む
def load_policy():
    policy_path = os.path.join(os.path.dirname(__file__), 'policy.txt')
    with open(policy_path, 'r') as file:
        policy_content = file.read()
    return policy_content

policy_text = load_policy()

docs = [{"page_content": txt} for txt in re.split(r"(?=\n##)", policy_text)]

retriever = VectorStoreRetriever.from_docs(docs, openai.Client(api_key=settings.OPENAI_API_KEY))

@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes performing other 'write' events."""
    k = 2  # 取得するドキュメントの数
    if k > len(docs):
        k = len(docs)
    results = retriever.query(query, k=k)
    return "\n\n".join([doc["page_content"] for doc in results])