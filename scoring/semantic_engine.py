# Day 12

from sentence_transformers import SentenceTransformer, util

# Load a lightweight pre-trained model (MiniLM is fast for 360+ matches)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_semantic_similarity(resume_text, jd_text):
    """
    Day 12 Logic: Uses Transformer embeddings to measure deep similarity.
    """
    # 1. Convert text to mathematical vectors (Embeddings)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    # 2. Compute Cosine Similarity (The 'angle' between the two vectors)
    # Result is between 0.0 and 1.0
    cosine_scores = util.cos_sim(resume_embedding, jd_embedding)
    
    return float(cosine_scores[0][0])