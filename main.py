from flask import *
import requests

app=Flask(__name__)

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    images="<img src="+response ['icon_url'] + " alt='Chucks image'>"
    return "<strong>Random joke from chuck norris: </strong>" + response['value'] + images

