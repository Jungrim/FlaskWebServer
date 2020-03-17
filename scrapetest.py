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
    '''
    api 서버에서 데이터 가져오기
    URL = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"
    request = urllib.request.Request(URL)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    jsonResult = json.loads(result)
    print(jsonResult)
    '''

    '''
    title 가져오기
    예외처리 포함한 예제
    title = getTitle('http://ncov.mohw.go.kr/')
    if title == None:
        print('TItle could not be found')
    else:
        print(type(title))
    test = {"title" : title.string}
    '''
    html = urlopen('http://ncov.mohw.go.kr/')
    bs = BeautifulSoup(html,'html.parser')
    numList = bs.findAll('span',{'class':'num'})
    resultList = []
    for n in numList[:4]:
        resultList.append(n.get_text())
    resultList[0] = resultList[0][4:]

    resJSON = {"accumulate" : resultList[0], "Cure": resultList[1], "underTreatment":resultList[2], "Dead":resultList[3]}

    return resJSON

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True)
    app.run(debug=True)


