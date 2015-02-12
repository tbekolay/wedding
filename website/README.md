wedding.bekolay.org
===================

Design based on
[IronSummitMedia/startbootstrap-agency](https://github.com/IronSummitMedia/startbootstrap-agency).

Flask app based on
[Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
and run on Google App Engine with the help of
[appengine-python-flask-skeleton](https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton)

Installation
------------

First, install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
If you're using Homebrew, this can be done with

```console
brew install google-app-engine
```

The Python dependencies aren't included in this repo by default.
To install them, do

```console
pip install -r requirements.txt -t lib
```

If you're using Homebrew, then you may also need to
[create a `~/.pydistutils.cfg`](http://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both)
with the following contents:

```ini
[install]
prefix=
```

Run locally
-----------

To run the project locally, do

```console
dev_appserver.py
```

and then visit <http://localhost:8080>.

Deploy
------

Use the [Admin Console](https://appengine.google.com/)
to set up your project.

Deploy with

```console
appcfg.py -A <your-project-id> --oauth2 update .
```

and then visit <your-project-id.appspot.com>.
