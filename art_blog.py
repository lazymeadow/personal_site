from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from sqlalchemy import desc

from models.art_blog import db, Post

app = Flask(__name__)

# TODO make application configurations, so this isn't hardcoded for dev
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqldb://audrey:wjae98RY3@audreymavra-mysql.c9jbxcitzkqw.us-west-2.rds.amazonaws.com:3306/personal_site'

db.init_app(app)
assets = Environment(app)
css_bundle = Bundle('style.less', output='style.css', filters=['less'], depends=('**/*.less'))
assets.register('css', css_bundle)


@app.route('/')
def index():
    try:
        posts = db.session.query(Post).order_by(desc(Post.published)).all()

        return render_template("art_blog/index.html", posts=posts)
    except Exception as e:
        print e
	return 'There was an error retrieving the blog.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=24816)
