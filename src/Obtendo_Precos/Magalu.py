from bs4 import BeautifulSoup
import requests
import re
from ferramentas import number_array_to_value,check_array,cleanName,cleanMemory


MAGALU = {}


def getName(array_text):
    for x in range(3,len(array_text)//2):
        nome = cleanName(array_text[x],array_text[x+1],array_text[x+2])
        if nome != None:
            return nome   
        
def getPrice(array_text):
    first = True
    primeiro = True
    x = 0
    text = ""
    for x in range(6,len(array_text)):
        if re.search(pattern="vistaou",string=array_text[x]) != None:
            text = array_text[x-2]
            first = False
    if first == True:
        for x in  range(6,len(array_text)):
            if (re.search(pattern="por",string=array_text[x]) != None) and (primeiro == True):
                primeiro = False
                text = array_text[x+1]
    if (first == False) or (primeiro == False):
        array = [None]*len(text)
        for x in range(len(text)):
            array[x] = text[x]
        if check_array(array,",") == True:
            array.remove(",")    
        for x in range(len(array)):
            if array[x] == ".":
                posicao = x
        if (posicao + 2) != len(array):
            count = 0
            extra = len(array) - (posicao+2) 
            x = len(array)-1
            while count < extra:
                array.pop(x)
                x = x - 1
                count = count + 1
        for x in range(len(array)):
            if x != posicao:
                array[x] = float(array[x])
        preco = number_array_to_value(array,posicao)
        return preco
    else:
        return "Produto indisponivel"

def getMemory(array_text):
    for x in range(3,len(array_text)):
        memoria = cleanMemory(array_text[x],array_text[x-1])
        if memoria != None:
            return memoria
            
        

def makeDictionary():
    URL = "https://www.magazineluiza.com.br/placa-de-video/informatica/s/in/pcvd/brand---asus--nvidia/?sfilters=0"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')  
    x = len(MAGALU)

    for tag in soup.find_all('a',attrs={"name":"linkToProduct"}):
        heading = tag.text
        heading_array = heading.split()
        nome = getName(heading_array)
        memoria = getMemory(heading_array)
        preco = getPrice(heading_array)
        if nome != None: 
            MAGALU[x] = x
            y = {}
            y['nome'] = nome
            y['memoria'] = memoria
            y['preco'] = preco
            MAGALU[x] = y
            x = x + 1
makeDictionary()