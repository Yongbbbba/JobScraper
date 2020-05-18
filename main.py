from flask import Flask, render_template, request, redirect
from scraper import get_jobs


app = Flask("SuperScraper")


@app.route("/")  # decorator(@)는 밑에 함수만을 본다. a ="Hello" 이런 식으로 쓰면 에러가 난다.
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)


app.run(host="127.0.0.1")
