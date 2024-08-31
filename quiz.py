from pine import similarity
from llm import generate

def quizmaker(dif,cid,topic):

    text = similarity(topic,cid) #k value change karo
    number = 5
    topic = topic
    tone = dif
    response_json = {
    "1": {
        "no": "1",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    },
    
    "2": {
        "no": "2",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    },
    
    "3": {
        "no": "3",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    }
    
    
    }

    template="""
        Data:{text}
        You are an expert MCQ maker. Given the above text, it is your job to \
        create a quiz  of {number} multiple choice questions for {topic}  in {tone} tone. 
        Make sure the questions are not repeated and check all the questions to be conforming the text as well.
        Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
        Ensure to make {number} MCQs
        ### RESPONSE_JSON EXAMPLE
        {response_json}
     """
    
    return generate(template=template,prompt='Give me quiz only abut '+topic)
     
