from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

from models.art_blog import db

app = Flask(__name__)

# TODO make application configurations, so this isn't hardcoded for dev
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqldb://audrey:wjae98RY3@audreymavra-mysql.c9jbxcitzkqw.us-west-2.rds.amazonaws.com:3306/personal_site'

db.init_app(app)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3579)
