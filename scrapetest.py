from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from flask import Flask
import urllib
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

@app.route('/')
def home():
    URL = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"
    request = urllib.request.Request(URL)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    jsonResult = json.loads(result)
    print(jsonResult)
    print('test')
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('TItle could not be found')
    else:
        print(title)
    return jsonResult

if __name__ == '__main__':
    app.run(debug=True)


