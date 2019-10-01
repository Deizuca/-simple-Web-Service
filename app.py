#importing Flask for creating App server
from flask import Flask, request
#importing json 
import json
import os
import os.path
import sys
#importing beautiful soup, requests for web scraping
from bs4 import BeautifulSoup
import urllib.request
import requests

app = Flask(__name__)


# a Python object (dict), to be able to return it to a json object later:
systeminfo = {
  "Python version": (sys.version),
  "Json Version": json.__version__ ,
}


@app.route("/")
def main():
    return 'Server Works!'

#returns pong
@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

#returns service version and system information. Returns json object
@app.route('/system', methods=['GET'])
def system():
    return (json.dumps(systeminfo))

# scraping info from web page
# the mediainfo/<id> will allow for the user to enter any id, and it will pull the specific information for the specific id
# returns a JSON object with image filename, size, dimensions and image title.
@app.route('/mediainfo/<id>', methods=['GET'])
def mediainfo(id):
    url = ('https://www.pond5.com/photo/' + id)
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    imageInfo = soup.find_all('img')
    
    #gets the information of the image dimensions
    Dimensions = soup.findAll(class_='u-text12px u-text10px:4Oem u-weightSemibold u-textLineHeightMatch u-paddingV20px u-paddingT0px:40em u-paddingB0px:40em')
   
    #creates an array for the dimensions
    my_list = []

    for i in Dimensions:
        my_list.append(i.contents)
        print(id)
       
        
    # a Python object (dict), to be able to return it to a json object later:
    media = {
        'Title': imageInfo[0]['src'],
        'Dimensions': my_list,
    }
    return(json.dumps(media))
   
   

#to run the server
if __name__ == "__main__":
    app.run(debug=True, port=80)

