#### Slack Dependency Downloader "SDD - v1.0"
#### Author: João Marcelo - jmfutrica@gmail.com
#### All code in github.com/futrica

# importing librares to use in program:

#it's comes with python3.3 
import urllib.request
#you can get it in https://pypi.python.org/pypi/beautifulsoup4
from bs4 import BeautifulSoup 
                              

# opening the url
response = urllib.request.urlopen(
    "http://slackbuilds.org/repository/14.1/multimedia/vlc/?search=vlc")
html = response.read()

# transforming this string in an object BeautifulSoup
soup = BeautifulSoup(html)

p = str(soup.find_all("p"))
n = p.find("This requires")

print("Verificando dependências")
if  n != -1:
    print("Listando dependências encontradas:")
    p1 = p[n+14:]
    p1 = p1[0:p1.index('</p>')]
    p1 = BeautifulSoup(p1)
    text = str(p1.get_text())
    #print(text)
    links = []
    for link in p1.find_all('a'):
        links.append("http://slackbuilds.org" + link.get('href'))
    print(links)
 
else:
    print("Não há dependências")


