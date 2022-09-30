from flask import Flask, render_template, session
from flask_assets import Environment
from flask_yamli18n import YAMLI18N
import util.assets

app = Flask(__name__)
app.secret_key = "whocalls secret key"
assets = Environment(app)
assets.register(util.assets.bundles)
y18n = YAMLI18N(app)
t = y18n.t  # for short

app.jinja_env.filters['trans'] = t

@app.before_request
def load_lang():
    session['lang'] = 'th'
    # if 'lang' not in session:
        # session['lang'] = 'th'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return  "<h1>About</h1>"


if __name__ == "__main__":
    app.run(debug=True)