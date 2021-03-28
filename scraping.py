import requests
from bs4 import BeautifulSoup

def scrap_url(url):
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content,"html.parser")
    paras = soup.find_all('p')
    string = ''
    for par in paras:
        string = string + par.get_text()
    return string
