from flask import Flask
from functions import *

app = Flask(__name__)


@app.route("/")
def home_page():
    candidates = load_candidates(file_name)
    result = '<pre>'
    for i in candidates:
        result += f"""
            Имя кандидата - {i['name']}\n
            Позиция кандидата - {i['position']}\n
            {i['skills']}
        """
    result += '</pre>'
    return result


@app.route("/candidates/<int:uid>")
def page_profile(uid):
    candidates = get_by_pk(uid)
    url = candidates["picture"]
    result = f"<img src='{url}'>"
    result += '<pre>'
    result += f""""
        Имя кандидата - {candidates["name"]}\n
        Позиция кандидата - {candidates["position"]}\n
        {candidates['skills']}
    """
    result += '</pre>'
    return result


@app.route("/skills/<uid>")
def skills_candidate(uid):
    candidates = get_by_skills(uid)
    result = '<pre>'
    for i in candidates:
        result += f"""
            Имя кандидата - {i['name']}\n
            Позиция кандидата - {i['position']}\n
            {i['skills']}
        """
    result += '</pre>'
    return result


app.run()
