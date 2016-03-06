import json

from flask import Flask, render_template
from flask_assets import Environment, Bundle
from dateutil.parser import parse
from calendar import timegm
from datetime import datetime
from lib import db, db_add
from models.art_blog import Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:banana@localhost:3306/personal_site'
db.init_app(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


def convert_date(date):
    if date[26] == ':':
        date = date[:26] + date[27:]
        return datetime.utcfromtimestamp(timegm(parse(date).timetuple()))


@app.route('/')
def index():
    '''
    # keeping for when creating posts is necessary, so as not to rewrite
    with open('misc/output.json') as file1:
        entries = json.loads(file1.read())
        for entry in entries:
            new_post = Post()
            new_post.title = entries[entry]['title']
            new_post.published = convert_date(entries[entry]['published'])
            new_post.updated = convert_date(entries[entry]['updated'])
            new_post.content = entries[entry]['content']
            for comment in entries[entry]['comments']:
                new_comment = Comment()
                new_comment.author = comment['author']
                new_comment.published = convert_date(comment['published'])
                new_comment.updated = convert_date(comment['updated'])
                new_comment.content = comment['content']
                new_comment.post_id = new_post.id
                new_post.comments.append(new_comment)
            db_add(new_post)
    '''
    posts = db.session.query(Post).all()


    return render_template("art_blog/index.html", posts=posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
