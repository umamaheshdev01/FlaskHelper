from llm import generate

def summarise_voice(text):
    res = generate("Please summarise the text and send me :  ",text)
    return res