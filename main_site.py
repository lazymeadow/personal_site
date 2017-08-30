from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)
css_bundle = Bundle('style.less', output='style.css', filters=['less'], depends=('**/*.less'))
assets.register('css', css_bundle)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3579)
