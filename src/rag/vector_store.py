import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

stored_texts = []

def add_to_index(embedding, text):
    index.add(np.array([embedding]).astype("float32"))
    stored_texts.append(text)