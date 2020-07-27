import string
import secrets # for random token generation

from datetime import datetime

from .extensions import db

class Link(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(8), unique = True)
    visits = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, **kwargs): # keyword argument coz while using flask sqlalchemy when class is a model you pass in columns that you want to set in the beginning
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link() #random generation here

    def generate_short_link(self):
        #characters = string.digits + string.ascii_letters
        short_url = secrets.token_hex(4)

        link = self.query.filter_by(short_url = short_url).first()

        if link: #if it is already present
            return self.generate_short_link()

        return short_url

    
