from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from file_proc import pievinot, lasit
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Gmail email'
app.config['MAIL_PASSWORD'] = 'You\'re Gmail password here'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/send_message', methods=["POST"])
def send_message():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form.get("message")
    msg = Message(subject, sender=email,
                  recipients=['Gmail here!'])
    msg.body = message
    mail.send(msg)
    pievinot(message + "\n" + email + "\n" + subject)
    return redirect("/home")


@app.route("/lasitDatus")
def lasitDatus():
    rindinas = lasit()
    return render_template("dati.html", rindinas=rindinas)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/cv")
def cv():
    return render_template('cv.html', title='CV')


@app.route("/login")
def login():
    return render_template('login.html', title='Login')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


@app.route("/web")
def web():
    return render_template('web.html', title='Web')


@app.route("/app")
def App():
    return render_template('app.html', title='App')


@app.route("/create-article", methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Some Error"
    else:
        return render_template('create-article.html', title='Create Article')


@app.route("/posts")
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
