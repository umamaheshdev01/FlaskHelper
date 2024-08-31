import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")
from llm import generate



def extract_transcript(url):

    video_id = url.split("v=")[1].split("&")[0]
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = " ".join([entry["text"] for entry in transcript_text])
    return transcript

def summarise_youtube(url):
    trans  = extract_transcript(url)
    res = generate("This is the transcript of the youtube video please summarise it ",trans)
    return res






