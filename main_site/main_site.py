from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

#TODO make application configurations, so this isn't hardcoded for dev
app.config['SERVER_NAME'] = 'audreymavra.localhost:3579'

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', subdomain='blog')
def blog():
    return "BLOG"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3579)
