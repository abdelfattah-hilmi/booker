from flask import Flask
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


def create_venue():
    Venue(title="hello",rating=5).save()


@app.route('/')
def main_endpoint():
    return ''' <h1> Hello world </h1>
    <h4> this is a place holder </h4>
    '''

if __name__ == '__main__':
    app.run(debug=True)
    # create_venue()
    