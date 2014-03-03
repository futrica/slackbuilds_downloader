from dependency import Dependency
#it's comes with python3.3
import urllib.request
#you can get it in https://pypi.python.org/pypi/beautifulsoup4
from bs4 import BeautifulSoup

file = Dependency(
    "http://slackbuilds.org/repository/14.1/multimedia/vlc/?search=vlc")

dependencies = file.set_dep()

for x in dependencies:
    x.to_string()

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
for x in dependencies:
    z = x.set_dep()
    if z != []:
        for y in z:
            dependencies.append(y)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
for x in dependencies:
    x.to_string()
