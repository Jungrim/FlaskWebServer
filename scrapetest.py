from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from flask import Flask
import urllib
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():

    html = urlopen('http://ncov.mohw.go.kr/')
    bs = BeautifulSoup(html,'html.parser')
    numList = bs.findAll('span',{'class':'num'})
    resultList = []
    for n in numList[:4]:
        resultList.append(n.get_text())
    resultList[0] = resultList[0][4:]

    resJSON = {"accumulate" : resultList[0], "cure": resultList[1], "underTreatment":resultList[2], "dead":resultList[3]}

    return resJSON

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)


