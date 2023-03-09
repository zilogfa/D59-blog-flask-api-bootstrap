# Dev: Ali Jafarbeglou - Full stack blog projects - 2022
# Tech: Python, Flask, Jinja, CSS, HTML, JS, Bootstrap, API [GET, POST]

from flask import *
from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phoneNumber']
        message = request.form['msg']
        return f'<h1 style="text-align: center; font-size:3rem">Your Message successfully submitted </h1>'
        # Auto Email code needed. I/P



if __name__ == "__main__":
    app.run(debug=True)
