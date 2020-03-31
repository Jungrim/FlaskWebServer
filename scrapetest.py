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
    beforeList = bs.findAll('span', {'class': 'before'})
    liveDate = bs.findAll('span', {'class': 'livedate'})

    resultList = []
    beforeResultList = []

    #확진자, 완치, 치료, 사망 인원수
    for n in numList[:4]:
        resultList.append(n.get_text())
    resultList[0] = resultList[0][4:]

    #전일대비 확진자, 완치, 치료, 사망 인원수
    for n in beforeList[:4]:
        beforeResultList.append(n.get_text())
    beforeResultList[0] = beforeResultList[0][5:]
    print(beforeResultList)

    # 실시간 업데이트 기준 날짜
    liveDateText =  liveDate[0].get_text()

    resJSON = {"liveDate" : liveDateText, "accumulate" : resultList[0], "accumulateBefore" : beforeResultList[0], "cure": resultList[1], "cureBefore": beforeResultList[1], "underTreatment":resultList[2], "underTreatmentBefore" : beforeResultList[2], "dead":resultList[3],"deadBefore" : beforeResultList[3]}

    return resJSON

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)


