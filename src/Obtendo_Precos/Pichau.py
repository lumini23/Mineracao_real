from bs4 import BeautifulSoup
import requests
import re
from ferramentas import cleanPrice,cleanMemory,cleanName
PICHAU ={}
page = "1"
def findName(array_text):
    for x in range(3,len(array_text)-3):
        nome = cleanName(array_text[x],array_text[x+1],array_text[x+2])
        if nome != None:
            return nome 

def findMemory(array_text):
    x = 0
    for x in range(len(array_text)):
        memoria = cleanMemory(array_text[x],array_text[x-1])
        if memoria != None:
            return memoria

class getInfo():
    def __init__(self,page):
        self.headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
        self.URL = "https://www.pichau.com.br/hardware/placa-de-video?page="+page
        self.site = requests.get(self.URL, headers=self.headers)
        self.soup = BeautifulSoup(self.site.content,'html.parser')
        body = self.soup.body
        div1 = body.contents[2]
        main = div1.contents[1]
        div2 = main.contents[1]
        div3 = div2.contents[0]
        div4 = div3.contents[0]
        self.page = div4 
    def getHeading(self,index):  
        html = self.soup.h2
        for x in range(index):
            html = html.find_next("h2")
        return html
    def getPrice(self,index):
        div4 = self.page
        div5 = div4.contents[2] 
        div6 = div5.contents[index]
        a1 = div6.contents[0]
        div7 = a1.contents[0]
        div8 = div7.contents[1]
        div9 = div8.contents[1]
        if div9.get_text() != "Esgotado":
            div10 = div9.contents[0]
            div11 = div10.contents[0]
            div12 = div11.contents[1]
            preco = div12.get_text()
            valor = cleanPrice(preco,",")
            return valor
        else:
            return "Produto indisponivel"
    def getLastPage(self):
        div4 = self.page
        nav1 = div4.contents[3]
        ul1 = nav1.contents[0]
        li1 = ul1.contents[7]
        button1 = li1.contents[0]
        page = button1.get_text()
        page = int(page)
        return page
info = getInfo('1')
def makeDictionary(page):
    z = len(PICHAU)
    x = len(PICHAU)
    info = getInfo(page)
    w = 0
    html = info.getHeading(w)
    while (z < (48 + z)) and (html != None):
        heading = html.text
        heading_array = heading.split()
        nome = findName(heading_array)
        memoria = findMemory(heading_array)
        preco = info.getPrice(w)
        if nome != None: 
            PICHAU[x] = x
            y = {}
            y['nome'] = nome
            y['memoria'] = memoria
            y['preco'] = preco
            PICHAU[x] = y
            x = x + 1
        z = z+ 1
        w = w + 1
        html = info.getHeading(w)
            
def attDictionary():
    page = info.getLastPage()
    indisponivel = False
    print("atualizando dicionario...")
    for x in range(1,page+1):
        if indisponivel == False:
            string = str(x)
            makeDictionary(string)
        if PICHAU[len(PICHAU)-1]['preco'] == "Produto indisponivel":
            indisponivel = True
attDictionary()

for item in PICHAU:
    print("\nitem: ",item)
    print(PICHAU[item])