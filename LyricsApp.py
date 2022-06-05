from pickle import GLOBAL
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests
from bs4 import BeautifulSoup

Website = "https://search.azlyrics.com/search.php?q="

def Top5():
    SongName = e.get()
    clear()

    URL = Website + SongName
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    elements = soup.find_all("table", {"class" : "table table-condensed"})[0]
    element = elements.find_all("b")

    global Links
    Links = []
    for a in elements.find_all('a', href=True):
        Links.append(a['href'])
    
    songname1Button = Button(root, text = element[0].text + "  " + element[1].text,width = 40, command = lambda: get_lyrics(0), bg = '#404040' , fg = '#ffffff')
    songname2Button = Button(root, text = element[2].text + "  " + element[3].text,width = 40, command = lambda: get_lyrics(1), bg = '#404040' , fg = '#ffffff')
    songname3Button = Button(root, text = element[4].text + "  " + element[5].text,width = 40, command = lambda: get_lyrics(2), bg = '#404040' , fg = '#ffffff')
    songname4Button = Button(root, text = element[6].text + "  " + element[7].text,width = 40, command = lambda: get_lyrics(3), bg = '#404040' , fg = '#ffffff')
    songname5Button = Button(root, text = element[8].text + "  " + element[9].text,width = 40, command = lambda: get_lyrics(4), bg = '#404040' , fg = '#ffffff')
    spaceLabel = Label(root, text = "", bg = '#212121' , fg = '#212121')
    quitButton = Button(root, text="Quit", command = quit, bg = '#404040' , fg = '#ffffff')


    songname1Button.pack()
    songname2Button.pack()
    songname3Button.pack()
    songname4Button.pack()
    songname5Button.pack()
    spaceLabel.pack()
    quitButton.pack()

def get_lyrics(LinkNumber):

    clear()
    URL = Links[LinkNumber]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("div", {"class" : "col-xs-12 col-lg-8 text-center"})[0]

    lyricsLabel = ScrolledText(root, width = 66, height = 20, bg = '#404040' , fg = '#ffffff')
    spaceLabel = Label(root, text = "", bg = '#212121' , fg = '#212121')
    quitButton = Button(root, text="Quit", command = quit, bg = '#404040' , fg = '#ffffff')

    lyricsLabel.insert('end', elements.find_all("div")[5].text)

    lyricsLabel.pack()
    spaceLabel.pack()
    quitButton.pack()

def clear():
    list = root.pack_slaves()
    for l in list:
        l.destroy()

def quit():
    root.quit()

root = Tk()
root.title("Lyrics")
root.iconbitmap()
root.configure(background='#212121')
root.geometry("400x400")

e = Entry(root, width = 66, bg = '#404040' , fg = '#ffffff')
e.pack()

searchButton = Button(root, text="Search", command = Top5, bg = '#404040' , fg = '#ffffff')
spaceLabel = Label(root, text = "", bg = '#212121' , fg = '#212121')
quitButton = Button(root, text="Quit", command = quit, bg = '#404040' , fg = '#ffffff')

searchButton.pack()
spaceLabel.pack()
quitButton.pack()

root.mainloop()