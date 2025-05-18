from flask import Flask, request, render_template
from resume_parser import parse_resume
from matcher import match_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    if request.method == "POST":
        jd = request.form["jd"]
        resume_text = request.form["resume"]
        parsed_resume = parse_resume(resume_text)
        score = match_score(parsed_resume, jd)
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)