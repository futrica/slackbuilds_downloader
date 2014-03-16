#it's comes with python3.3
#já vem com o python3.3
import urllib.request
#you can get it in https://pypi.python.org/pypi/beautifulsoup4
#link para download dessa biblioteca https://pypi.python.org/pypi/beautifulsoup4
from bs4 import BeautifulSoup 

class Dependency:
    #define how class will be
    #define como a classe deve ser com o método init
    def __init__(self, link,  name = "", html = "", links = [], down_links = [],
                 download = False , extracted = False, install = False):
        self.html = self.set_html(link)
        self.name = self.set_name()
        self.link = link
        self.links = self.set_links(link)
        self.down_links = self.set_download_link(self.html)
        self.download = download
        self.extracted = extracted
        self.install = install
    #extract the html     
    #extrai o html  
    def set_html(self, link):
        response = urllib.request.urlopen(link)
        url = response.read()
        # transforming this string in an object BeautifulSoup
        soup = BeautifulSoup(url)
        self.html = soup
        return self.html
    #extract the name
    #extrai o nome
    def set_name(self):
        p = str(self.html.title.string)
        p = p[p.find("-")+2:]
        return p
    #look for links into html
    #procura os links no html
    def set_links(self, link):
        p = str(self.html.find_all("p"))
        n = p.find("This requires")

        if  n != -1:
            p1 = p[n+14:]
            p1 = p1[0:p1.index('</p>')]
            p1 = BeautifulSoup(p1)
            text = str(p1.get_text())
            links = []
            for link in p1.find_all('a'):
                url = "http://slackbuilds.org" + link.get('href')
                links.append(url)
            return links 
        else:
            return []
    #look for dependencies
    #procura as dependencias
    def set_dep(self):
        dep = []
        for x in self.links:
            dep.append(Dependency (x))
        return dep
    #print to console
    #imprime no console           
    def to_string(self):
        print("Arquivo: ", self.name)
        #print(self.html)
        print("Em: ",self.link)
        #print(self.download)
        #print(self.extracted)
        #print(self.install)

    #catch links to download
    #pega os links para download
    def set_download_link(self, html):
        p = str(self.html.find_all("div", class_="section center"))
        p = BeautifulSoup(p)
        down_links = []
        for link in p.find_all('a'): 
            r = str(link.get("href"))
            if r.endswith((".gz", ".tgz", ".bz2", ".xz", ".deb")) :
                down_links.append(r)
        return down_links
