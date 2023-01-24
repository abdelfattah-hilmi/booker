from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from models.venue import Venue


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db":"Tranzac_db",
    "host":"localhost",
    "username":"root",
    "password":"root",
    "port": 27017
}

db = MongoEngine(app)


def create_venue(title,rating):
    Venue(title=title,rating=rating).save()


@app.route('/', methods=['GET','Post'])
def main_endpoint():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            venue_title = request_data["title"]
            venue_rating = request_data["rating"]
            create_venue(venue_title,venue_rating)
            return request_data,201
        except:
            return 400


    else:
        venues = jsonify( Venue.objects() )
        return venues

    
if __name__ == '__main__':
    app.run(debug=True)
    # create_venue()
    