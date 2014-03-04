from dependency import Dependency
#it's comes with python3.3
import urllib.request
#you can get it in https://pypi.python.org/pypi/beautifulsoup4
from bs4 import BeautifulSoup
import subprocess


file = Dependency(
    "http://slackbuilds.org/repository/14.1/multimedia/vlc/?search=vlc")

dependencies = file.set_dep()

##print("Procurando arquivo ... ")
##print("Arquivo encontrado: ", file.name)
##print(" ")
##print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
##
##print(" ")
##print("Listando dependências:")
##for x in dependencies:
##    z = x.set_dep()
##    if z != []:
##        for y in z:
##            dependencies.append(y)
##            
##for x in dependencies:
##    x.to_string()
##    print(" ")
##
##print(" ")
##print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
##print(" ")

print("Instalando Dependências: ")
print(" ")
i = len(dependencies) -1

while (i >= 0):
    print("Dependência: ", dependencies[i].name)
    print("fazendo download dos arquivos..... ")
    for k in range(2):
        if k == 0:
            p = subprocess.Popen(["wget", "-c","-P","depen",dependencies[i].down_links[k]])
            if p.communicate():
                print("Source ... Complete")
        else:
            p = subprocess.Popen(["wget", "-c","-P","depen",dependencies[i].down_links[k]])
            if p.communicate():
                print("Build ... Complete")
    i -= 1
    print(" ")
    

