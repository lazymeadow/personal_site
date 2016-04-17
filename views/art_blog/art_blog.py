# create art_blog blueprint, import to main_site.py

from calendar import timegm
from datetime import datetime

from dateutil.parser import parse
from flask import render_template, Blueprint
from sqlalchemy import desc

blog = Blueprint('art_blog', __name__)

from models.art_blog import Post, db

from main_site import app
blog.static_folder = app.static_folder


def convert_date(date):
    if date[26] == ':':
        date = date[:26] + date[27:]
        return datetime.utcfromtimestamp(timegm(parse(date).timetuple()))


@blog.route('/', methods=['GET'], subdomain='blog')
def index():
    try:
        posts = db.session.query(Post).order_by(desc(Post.published)).all()

        return render_template("art_blog/index.html", posts=posts)
    except Exception as e:
        print e
