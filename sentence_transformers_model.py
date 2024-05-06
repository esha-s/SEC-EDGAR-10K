from sentence_transformers import SentenceTransformer
sentences = ["10k_text_placeholder"]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
