import mongoengine as me

class Venue(me.Document):
    title = me.StringField(required=True)
    rating = me.IntField(min_value=0,max_value=10)
    