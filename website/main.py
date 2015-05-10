from flask import Flask, render_template, request, Response
from google.appengine.ext import ndb

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals.update(zip=zip)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_404(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def page_500(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
