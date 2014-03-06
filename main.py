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
##print("fazendo download build")
##f = subprocess.Popen(["wget", "-c",file.down_links[1]])
##f.communicate()
##name = file.name + ".tar.gz"
##print("extraindo")
##f = subprocess.Popen(["/bin/tar", "-xf", name])
##f.communicate()
##folder = file.name + "/"
##print("fazendo download source")
##z = subprocess.Popen(["wget", "-c","-P", folder, file.down_links[0]])
##z.communicate()
##print(" ")
##print("dando permissão")
##folder = file.name + "/"
##build = file.name + ".SlackBuild"
##p = subprocess.Popen(["chmod", "+x",folder, build])
##p.communicate()

##
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
##
##print("Instalando Dependências: ")
##print(" ")

i = len(dependencies) -1
while (i >= 0):
##    print("Dependência: ", dependencies[i].name)
##    print("fazendo download da build..... ")
##    p = subprocess.Popen(["wget", "-c",dependencies[i].down_links[1]])
##    p.communicate()
##    print("Complete")
##    
##    print("extraindo ..." , dependencies[i].name)
##    name = dependencies[i].name + ".tar.gz"
##    q = subprocess.Popen(["/bin/tar", "-xf", name])
##    q.communicate()
##    print("Complete")
##
##    print("fazendo download do source... ", dependencies[i].name)
##    folder = dependencies[i].name + "/"
##    p = subprocess.Popen(["wget", "-c","-P", folder, dependencies[i].down_links[0]])
##    p.communicate()
##    print("Complete")
##
##    print("dando permissões... ", dependencies[i].name)
##    folder = dependencies[i].name + "/"
##    build = dependencies[i].name + ".SlackBuild"
##    p = subprocess.Popen(["chmod", "+x",folder, build])
##    p.communicate()
##    print("Complete")

    print("compilando a build... ", dependencies[i].name)
    folder = dependencies[i].name + "/"
    build =  dependencies[i].name + ".SlackBuild"
    p = subprocess.Popen(["/bin/sh" , build],cwd=folder)
    p.communicate()
    print("Complete")
    i -= 1
