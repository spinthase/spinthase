from flask import Flask, render_template, request, redirect, url_for
from datetime import date, datetime
import os

from database import db
from models import GuestbookEntry

app = Flask(__name__)


# identifies database as guestbook.db, otherwise creates guestbook.db
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'guestbook.db')

app.config.from_object(Config)
db.init_app(app)


# generating tables within guestbook database
with app.app_context():
    db.create_all()


# routing HTML pages to their correct URLs
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/guestbook")
def guestbook():
    guestbook = GuestbookEntry.query.all()
    return render_template("guestbook.html", guestbook=guestbook)


# receiving name/comment data from guestbook.html, and creating a guestbook entry with that data
@app.route("/add_entry", methods=['POST'])
def add_entry():
    name = request.form['name']
    comment = request.form['comment']
    entry = GuestbookEntry(name=name, comment=comment)

    db.session.add(entry)
    db.session.commit()

    return redirect(url_for("guestbook"))