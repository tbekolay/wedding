from flask import Flask, flash, g, redirect, render_template

# from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals.update(zip=zip)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # form = RSVPForm()
    # if form.validate_on_submit():
    #     flash('Login requested for OpenID="%s", remember_me=%s' %
    #           (form.openid.data, str(form.remember_me.data)))
    #     return redirect('/index')
    # return render_template('index.html', just_submitted=False)
    return render_template('placeholder.html')


@app.errorhandler(404)
def page_404(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def page_500(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
