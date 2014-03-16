from dependency import Dependency
#it's comes with python3.3
#já vem com o python3.3
import urllib.request
#you can get it in https://pypi.python.org/pypi/beautifulsoup4
#você pode baixar em https://pypi.python.org/pypi/beautifulsoup4
from bs4 import BeautifulSoup
#you can get it in https://pypi.python.org/pypi/pyutilib.subprocess/3.2
#você pode pegar isso em https://pypi.python.org/pypi/pyutilib.subprocess/3.2
import subprocess

#create a instance of class Dependency
#cria uma instância da classe Dependency
s = input()
file = Dependency(s)

#list all dependencies from file
#lista todas dependências do arquivo
dependencies = file.set_dep()

print("Procurando arquivo ... ")
print("Arquivo encontrado: ", file.name)
print(" ")
print("fazendo download build")
num = len(file.down_links) -1
f = subprocess.Popen(["wget", "-c",file.down_links[num]])

f.wait()
name = file.name + ".tar.gz"
print("extraindo")
f = subprocess.Popen(["/bin/tar", "-xf", name])
f.wait()
folder = file.name + "/"
print("fazendo download source")
z = subprocess.Popen(["wget", "-c","-P", folder, file.down_links[0]])
z.wait()
print(" ")
print("dando permissão")
folder = file.name + "/"
build = file.name + ".SlackBuild"
p = subprocess.Popen(["chmod", "+x",folder, build])
p.wait()


print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#print dependencies
#imprime dependências
print(" ")
print("Listando dependências:")
for x in dependencies:
    z = x.set_dep()
    if z != []:
        for y in z:
            dependencies.append(y)
            
for x in dependencies:
    x.to_string()
    print(" ")
    


print(" ")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(" ")

print("Instalando Dependências: ")
print(" ")
#download, extract, give permission, compile and install dependencies
#baixa, extrai, dá permissão, compila e instala dependências
i = len(dependencies) -1
while (i >= 0):
    print("Dependência: ", dependencies[i].name)
    print("fazendo download da build..... ")
    p = subprocess.Popen(["wget", "-c",dependencies[i].down_links[1]])
    p.wait()
    print("Complete")

    print("extraindo ..." , dependencies[i].name)
    name = dependencies[i].name + ".tar.gz"
    p = subprocess.Popen(["/bin/tar", "-xf", name])
    p.wait()
    print("Complete")


    print("fazendo download do source... ", dependencies[i].name)
    folder = dependencies[i].name + "/"
    p = subprocess.Popen(["wget", "-c","-P", folder, dependencies[i].down_links[0]])
    p.wait()
    print("Complete")

    print("dando permissões... ", dependencies[i].name)
    folder = dependencies[i].name + "/"
    build = dependencies[i].name + ".SlackBuild"
    p = subprocess.Popen(["chmod", "+x",folder, build])
    p.wait()
    print("Complete")

    print("compilando a build... ", dependencies[i].name)
    folder = dependencies[i].name + "/"
    build =  dependencies[i].name + ".SlackBuild"
    p = subprocess.Popen(["/bin/sh" , build],cwd=folder)
    p.wait()
    print("Complete")

    print("instalando... ", dependencies[i].name)
    exe = dependencies[i].name + "*.tgz"
    p = subprocess.Popen(["/sbin/installpkg" , exe],cwd="/tmp")
    p.wait()
    print("Complete")
    i -= 1
    print(" ")

#compile file
#compila o arquivo
print("compilando a build do arquivo: ", file.name)
folder = file.name + "/"
build =  file.name + ".SlackBuild"
p = subprocess.Popen(["/bin/sh" , build],cwd=folder)
p.wait()
print("Complete")
print(" ")
#install file
#instala o arquivo
print("instalando a build do arquivo... ", file.name)
exe = file.name + "*.tgz"
p = subprocess.Popen(["/sbin/installpkg" , exe],cwd="/tmp")
p.wait()
print("Complete")
print(" ")
print("Arquivo instalado com sucesso! ")

    
