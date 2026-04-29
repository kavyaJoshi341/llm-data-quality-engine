from src.rag.vector_store import index, stored_texts
import numpy as np

def retrieve_similar(query_embedding, k=2):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [stored_texts[i] for i in I[0] if i < len(stored_texts)]