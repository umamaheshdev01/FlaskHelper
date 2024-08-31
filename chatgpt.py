from pine import generate_embeddings,similarity
from llm import generate

def rungpt(question,namespace):
    k = similarity(question,namespace)
    return k
    
 


