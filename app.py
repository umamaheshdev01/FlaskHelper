from flask import Flask,request,jsonify
from youtube import summarise_youtube
from pine import store,similarity
from  voice import summarise_voice
from quiz import quizmaker
from chatPdf import process_pdf_and_ask_question

app = Flask(__name__)

@app.route('/youtube',methods=["POST"])
def youtube_sumarizer():
    data = request.json
    c = data.get('classId')
    k = data.get('url')
    res = summarise_youtube(k)
    store([res],str(c),{"url":k})
    return jsonify({
        "res":res
    })

@app.route('/voice',methods=["POST"])
def voice_sumarizer():
    data = request.json
    c = data.get('classId')
    k = data.get('text')
    res = summarise_voice(k)
    store([res],str(c),{})
    return jsonify({
        "res":res
    })

@app.route('/search',methods=["POST"])
def finder():
    data = request.json
    c = data.get('classId')
    k = data.get('query')
    res = similarity(text=k,namespace=str(c))
    return jsonify({
        "res":res
    })


@app.route('/quiz',methods=["POST"])
def quiz():
    data = request.json
    c = data.get('classId')
    k = data.get('topic')
    d = data.get('difficulty')
    res = quizmaker(d,c,topic=k)
    return res

@app.route('/pdf-question', methods=["POST"])
def pdf_question():
    data = request.json
    pdf_files = data.get("url")
    user_question = data.get('question')
    
    if not pdf_files or not user_question:
        return jsonify({"error": "No files or question provided"}), 400

    pdf_files = [pdf_file for pdf_file in pdf_files]  # Convert file paths to file-like objects if necessary
    
    try:
        answer = process_pdf_and_ask_question(pdf_files, user_question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
