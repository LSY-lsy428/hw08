import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List

EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_store")
vector_store = Chroma(
    client=client,
    collection_name="course_knowledge",
    embedding_function=EMBEDDING_MODEL
)

def add_text_chunks(chunks: List[str]):
    """向向量库写入文本块"""
    vector_store.add_texts(texts=chunks)

def search_similar_text(query: str, top_k: int = 3) -> List[str]:
    """根据问题检索最相似文档片段"""
    result = vector_store.similarity_search(query=query, k=top_k)
    return [doc.page_content for doc in result]
