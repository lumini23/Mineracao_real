from bs4 import BeautifulSoup
import requests
import re 

def not_daniel(href):
    return href and not re.compile("daniel").search(href)


def getHeading():
    URL = "https://www.kabum.com.br/hardware/placa-de-video-vga?pagina=1&ordem=5&limite=30&prime=false&marcas=[]&tipo_produto=[]&filtro=[]"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')
    heading = soup.find("a",class_="sc-fzoLsD gnrNhT item-nome")
    heading2 = soup.find_all("a",class_=re.compile("item-nome"))
    heading3 = soup.select("a.sc-fzoLsD.gnrNhT.item-nome")
    tabela = soup.find('a', class_="sc-fzoLsD gnrNhT item-nome")       
    print(soup.find(href="/produto/95122/placa-de-v-deo-evga-nvidia-geforce-gt-1030-sc-2gb-gddr5-02g-p4-6338-kr"))
    print(soup.find('div',class_="listagem-produtos"))

def getName():
    return 0
def getPrice():
    return 0
def getMemory():
    return 0
getHeading()