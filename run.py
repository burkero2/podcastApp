import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_title="About")


@app.route("/podcast")
def podcast():
    return render_template("podcast.html", page_title="Podcasts")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/archive")
def archive():
    return render_template("archive.html", page_title="Archive")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), 
        debug = True)
    