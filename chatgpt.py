from pine import generate_embeddings,similarity
from llm import generate

def rungpt(question,namespace):
    k = similarity(question,namespace)
    return generate(k,question+''+'Answer on your own if u dont find answer')
    
 


