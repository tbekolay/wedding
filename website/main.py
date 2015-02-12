from flask import Flask, render_template, request
from google.appengine.ext import ndb

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals.update(zip=zip)

# primary secondary
# #fed136 #fec503
# #971b2f #a24f56
# #ac1735 #b92442


class RSVP(ndb.Model):
    # --- 1
    name = ndb.StringProperty()
    partner = ndb.StringProperty()
    married = ndb.BooleanProperty()
    coming = ndb.BooleanProperty()
    # --- 2A
    marriage_advice = ndb.TextProperty()
    # --- 2B
    marriage_observations = ndb.TextProperty()
    # --- 3
    impression = ndb.TextProperty()
    # --- 4
    card_game = ndb.StringProperty()
    tradition = ndb.StringProperty()
    temperature = ndb.StringProperty()
    car_name = ndb.StringProperty()
    next_country = ndb.StringProperty()
    book_recommend = ndb.StringProperty()
    # --- 5
    my_receive_affection = ndb.StringProperty()
    my_give_affection = ndb.StringProperty()
    # --- 6
    partner_receive_affection = ndb.StringProperty()
    partner_give_affection = ndb.StringProperty()
    # --- 7
    age = ndb.StringProperty()
    siblings = ndb.StringProperty()
    places_lived = ndb.StringProperty()
    cities_lived = ndb.StringProperty()
    broken_bones = ndb.StringProperty()
    shoe_size = ndb.StringProperty()
    glasses = ndb.StringProperty()
    science_grade = ndb.StringProperty()
    wage = ndb.StringProperty()
    morning_night = ndb.StringProperty()
    accomodation = ndb.StringProperty()
    # --- 8
    wine = ndb.StringProperty()
    hot_beverage = ndb.StringProperty()
    bread = ndb.StringProperty()
    cake = ndb.StringProperty()
    allergies = ndb.TextProperty()
    # --- 9
    other = ndb.TextProperty()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    just_submitted = request.method == 'POST'

    if just_submitted:
        rsvp = RSVP()
        for key in request.form:
            val = request.form[key]
            if key == 'wage':
                print val
            if isinstance(getattr(RSVP, key.replace('-', '_')),
                          ndb.BooleanProperty):
                val = bool(val)
            setattr(rsvp, key.replace('-', '_'), val)
        rsvp.put()
    return render_template('index.html', just_submitted=just_submitted)


@app.errorhandler(404)
def page_404(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def page_500(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
