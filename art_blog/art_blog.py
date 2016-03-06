from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql-mysqldb://root:banana@localhost:3306'
db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    return render_template("art_blog/index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
