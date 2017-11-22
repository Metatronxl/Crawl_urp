import urllib
import urllib2
import requests
from bs4 import BeautifulSoup


username = '2014141463228'
password = '132618'
search_user = '2014141463105'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
postData = {
    'zjh':username,
    'mm':password
}

searchData = {
    'LS_XH':search_user,
    'resultPage':'http://zhjw.scu.edu.cn:80/reportFiles/cj/cj_zwcjd.jsp?'
}




def login():

    s = requests.session()
    loginURL = "http://zhjw.scu.edu.cn/loginAction.do"
    afterURL = "http://zhjw.scu.edu.cn/setReportParams"
    #get cookie
    login = s.post(loginURL,data=postData,headers=headers)
    response = s.post(afterURL,data=searchData,cookies=login.cookies,headers = headers)

    response =  response.content.decode('GBK').encode('utf-8')
    content = BeautifulSoup(response,'lxml')
    return  content

    # print login.content.decode('GBK').encode('utf-8')

def getData():
    content = login()
    tags = content.find_all('tr')
    for tag in tags:
        if tag.find_all(name='td',attrs={"class":"report1_2_1"}):
            print tag.get_text()




if __name__ == '__main__':
    getData()
