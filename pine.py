from pinecone import Pinecone
import google.generativeai as genai

genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")
pc = Pinecone(api_key="4f3dd80b-1c86-4be6-90b4-7f0f21b6bc06")


def generate_embeddings(text):
    result = genai.embed_content(
    model="models/text-embedding-004", 
    content=text,
    task_type="retrieval_document")
    embeddings = result['embedding']
    return embeddings
        
        
def store(text,namespace,metadata):
    index = pc.Index("classroom")
    vectors = []
    for i in text:
        vectors.append({
            "id" : str(i),
            "vectors" : generate_embeddings(text=i),
            "metadata" : metadata
        })
    index.upsert(vectors=vectors,namespace=namespace)
    print('Embeding Generation Done')


def similarity(text,namespace):
    index = pc.Index("classroom")
    query_results1 = index.query(
    namespace=namespace,
    vector=generate_embeddings(text=text),
    top_k=2,
    include_values=True
    )
    return str(query_results1.matches[0].id)+' '+str(query_results1.matches[1].id)

