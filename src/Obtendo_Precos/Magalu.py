from bs4 import BeautifulSoup
import requests
import re
from ferramentas import number_array_to_value,check_array,cleanName,cleanMemory


MAGALU = {}

# def getName(array_text):
#     for x in range(len(array_text)):
#         n = re.search(pattern="GTX",string=array_text[x])
#         z = re.search(pattern="RTX",string=array_text[x])
#         w = re.search(pattern="RX",string=array_text[x]) 
#         if (n or z or w) != None:
#             nome = array_text[x] + " " + array_text[x+1]
#             return nome
def getName(array_text):
    for x in range(3,len(array_text)//2):
        nome = cleanName(array_text[x],array_text[x+1],array_text[x+2])
        if nome != None:
            print(array_text)
            return nome   
        

def getPrice(array_text):
    first = True
    primeiro = True
    x = 0
    text = ""
    while x < len(array_text) and first == True:
        if array_text[x] == "vistaou":
            first = False
            text = array_text[x-2]
        x = x + 1
    if first == True:
        while x < len(array_text) and primeiro == True:
            if array_text[x] == "por":
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
            else:
                array[x] = float(array[x])
        preco = number_array_to_value(array,posicao)
        return preco
    else:
        return "Produto indisponivel"

# def getMemory(array_text):
#     first = True
#     x = 0
#     while (x < len(array_text)) and (first == True):
#         if (array_text[x] == "GTX") or (array_text[x] == "RTX") or (array_text[x] == "RX") or (array_text[x] == "gtx"):   
#             first == False 
#             for y in range(x,len(array_text)):
#                 array = array_text[y]
#                 primeiro = True
#                 z = 0
#                 while (z < len(array) - 1) and primeiro == True :
#                     if array[z] == ("G" or "g") and array[z+1] == ("B" or "b"):
#                         primeiro = False
#                         try:
#                             memoria = int(array[0])*10 + int(array[1])
#                             return memoria
#                         except:
#                             memoria = int(array[0])
#                             return memoria

#                     z = z + 1 
#         x = x + 1

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
for item in MAGALU:
    print(MAGALU[item])