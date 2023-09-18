from flask import Flask, render_template, request, redirect, send_file
from extractors.rmw import extract_rmw_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}  #사용자캐쉬 설정 a사용자 keyword검색값 가짜 db에 저장


@app.route("/")
def home():
  return render_template("home.html", name="nico")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")

  if keyword in db:
    jobs = db[keyword]
  else:
    rmw = extract_rmw_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = rmw + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")
