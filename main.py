from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from exporter import save_to_file


app = Flask("SuperScraper")

db = {}  # fake DB를 만들어서 웹에서 scraper 가 빠르게 돌아가는 것처럼 만들기


@app.route("/")  # decorator(@)는 밑에 함수만을 본다. a ="Hello" 이런 식으로 쓰면 에러가 난다.
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        JobDB = db.get(word)
        if JobDB:
            jobs = JobDB
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
        # job마다 html로 랜더링하기
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="127.0.0.1")
