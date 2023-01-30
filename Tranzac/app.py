from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from models.venue import Venue
import requests
# from bson import ObjectId


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db":"Tranzac_db",
    "host":"localhost",
    "username":"root",
    "password":"root",
    "port": 27017
}

db = MongoEngine(app)


def create_venue(title:str,rating:int)->None:
    Venue(title=title,rating=rating).save()

def verify_access_jwt(url:str,token:str)->bool:
    ''' this fuction returns True if the given jwt is verified from the Users service, and False if jwt is invalid(does not correspond to an autheticated user) '''

    response = requests.post(url,{
        "token":token
    })

    return True if response.status.code == 200 else False




@app.get('/')
def main_endpoint():
    return "Hello there! This is the transac service",200



@app.route('/venues', methods=['GET','Post'])
def list_create_venues():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            venue_title = request_data["title"]
            venue_rating = request_data["rating"]
            create_venue(venue_title,venue_rating)
            return request_data,201
        except:
            return "Value Error",400


    else:
        venues = jsonify( Venue.objects )
        return venues


@app.get('/venues/<int:id>')
def get_venue(id):
    venues = Venue.objects
    return (jsonify(venues[id]) if id < len(venues) else "The requested object does not exist",404)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    