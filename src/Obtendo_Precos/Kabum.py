from bs4 import BeautifulSoup
import requests
import re 


def getHeading():
    URL = "https://www.kabum.com.br/hardware/placa-de-video-vga?pagina=1&ordem=5&limite=30&prime=false&marcas=[]&tipo_produto=[]&filtro=[]"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')
    heading = soup.find_all("a",class_="sc-fzoLsD gnrNhT item-nome")
    print(heading)

def getName():
    return 0
def getPrice():
    return 0
def getMemory():
    return 0
getHeading()