from flask import Flask, flash, redirect, render_template

from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.errorhandler(404)
def page_404(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_500(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
