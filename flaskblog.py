from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Suraj Wate',
        'title': 'First Blog Post',
        'content': 'This is the first example post content for the blog app.',
        'date_posted': 'August 25, 2021'
    },
    {
        'author': 'Kushal Wate',
        'title': 'Second Blog Post',
        'content': 'This is the first example of second post content for the blog app.',
        'date_posted': 'August 26, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) 

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)