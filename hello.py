from flask import Flask
from flask import render_template


app = Flask(__name__)
db = {
        "a":"blog post 1", 
        "b":"Pogoda na południu",
        "c":"Pogoda na północy"
    }


@app.route("/")
def hello_world():
    return render_template("index.html", db = db)


@app.route("/test")
def another_hello():
    return "<p>Hello Fortnite!</p>"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/post/<blog_key>')
def show_post_str(blog_key):
    blog_post = db[blog_key]
    return render_template("blog_post.html", blog_post = blog_post)