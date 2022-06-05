import requests
from bs4 import BeautifulSoup

SongName = input("Enter the song name: ")
Website = "https://search.azlyrics.com/search.php?q="
URL = Website + SongName

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

elements = soup.find_all("table", {"class" : "table table-condensed"})[0]
element = elements.find_all("b")

Links = []
for a in elements.find_all('a', href=True):
    Links.append(a['href']) 

for j in range(0,10,2):
    print(j // 2 + 1,end=".")
    for i in range(2):
        print(element[i+j].text, end=" ")
    print()

SongNum = int(input("which song do you want: "))
URL = Links[SongNum - 1]
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

elements = soup.find_all("div", {"class" : "col-xs-12 col-lg-8 text-center"})[0]
element = elements.find_all("div")[5]

print(element.text)

