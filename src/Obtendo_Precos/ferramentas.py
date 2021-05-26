import re


def arredondar(num):
    return float( '%g' % (num))

def number_array_to_value(array,posicao):
    letra = 0
    first = False
    for x in range(posicao):
        array[x] = array[x]*pow(10,posicao - 1 - x)
    for x in range(posicao + 1,len(array)):
        if (type(array[x]) == float) or (type(array[x]) == int):
            array[x] = array[x]*pow(10,posicao - x)
        elif (type(array[x]) != float) and (type(array[x]) != int) and first == False:
            letra = x
            first = True
            x = len(array)
    if letra == 0:
        valor = 0.0
        for z in range(len(array)):
            if z != posicao:
                valor = arredondar(valor + array[z])
    else:
        valor = 0.0
        for z in range(letra):
            if z != posicao:
                valor = arredondar(valor + array[z])  
    return valor

def check_array(array,item):
    teste = False
    for x in range(len(array)):
        if array[x] == item:
            teste = True
    return teste
def RTX2000(name,atribute):
    nome = None
    if re.search(pattern="2060",string=name) != None:
        nome = "RTX 2060" 
    elif re.search(pattern="2070",string=name) != None:
        nome = "RTX 2070"
    elif re.search(pattern="2080",string=name) != None:
        if re.search(pattern="TI",string=name) != None:
            nome = "RTX 2080 Ti"
        elif re.search(pattern="TI",string=atribute) != None:
            nome = "RTX 2080 Ti"
        else:
            nome = "RTX 2080"
    return nome
def RTX3000(name,atribute):
    nome = None
    if re.search(pattern="3080",string=name) != None:
        nome = "RTX 3080"
    elif re.search(pattern="3090",string=name) != None:
        nome = "RTX 3090"
    elif re.search(pattern="3060",string=name) != None:
        if re.search(pattern="TI",string=name) != None:
            nome = "RTX 3060 Ti"
        elif re.search(pattern="TI",string=atribute) != None:
            nome = "RTX 3060 Ti"
        else:
            nome = "RTX 3060"
    elif re.search(pattern="3070",string=name) != None:
        nome = "RTX 3070"
    return nome

def getModelRTX(tipo,name,atribute):
    Name = None
    if re.search(pattern="2",string=tipo) != None:
        nome = RTX2000(tipo,name)
        return nome
    elif re.search(pattern="3",string=tipo) != None:
        nome = RTX3000(tipo,name)
        return nome
    else:
        Name = RTX3000(name,atribute)
        if Name == None:
            Name = RTX2000(name,atribute)
        return Name
def GTX1660(name,atribute):
    nome = None
    if re.search(pattern="1660",string=name) != None:
        if re.search(pattern="Super",string=name) != None:
            nome = "GTX 1660S"
        elif re.search(pattern="TI",string=name) != None:
            nome = "GTX 1660 Ti"
        elif re.search(pattern="Super",string=atribute) != None:
            nome = "GTX 1660S"
        elif re.search(pattern="TI",string=atribute) != None:
            nome = "GTX 1660 Ti"
        else:
            nome = "GTX 1660"
    return nome
def GTX1080(name,atribute):
    nome = None
    if re.search(pattern="1080",string=name) != None:
        if re.search(pattern="TI",string=name) != None:
            nome = "GTX 1080 Ti"
        elif re.search(pattern="TI",string=atribute) != None:
            nome = "GTX 1080 Ti"
        else:
            nome = "GTX 1080"
    return nome
def getModelGTX(tipo,name,atribute):
    Name = None
    if re.search(pattern="166",string=tipo) != None:
        nome = GTX1660(tipo,name)
        return nome
    elif re.search(pattern="10",string=tipo) != None:
        nome = GTX1080(tipo,name)
        return nome
    else:
        Name = GTX1660(name,atribute)
        if Name == None:
            Name = GTX1080(name,atribute)
        return Name

def RX6000(name,atribute):
    nome = None
    if re.search(pattern="6700",string=name) != None:
        if re.search(pattern="XT",string=name) != None:
            nome = "6700 XT"
        elif re.search(pattern="XT",string=atribute) != None:
            nome = "6700 XT"
        else:
            nome = "6700"
    elif re.search(pattern="6800",string=name) != None:
        if re.search(pattern="XT",string=name) != None:
            nome = "6800 XT"
        elif re.search(pattern="XT",string=atribute) != None:
            nome = "6800 XT"
        else:
            nome = "6800"
    return nome
def RX5(name,atribute):
    nome = None
    if re.search(pattern="5700",string=name) != None:
        if re.search(pattern="XT",string=name) != None:
            nome = "5700 XT"
        elif re.search(pattern="XT",string=atribute) != None:
            nome = "5700 XT"
        else:
            nome = "5700"
    elif re.search(pattern="5600",string=name) != None:
        if re.search(pattern="XT",string=name) != None:
            nome = "5600 XT"
        elif re.search(pattern="XT",string=atribute) != None:
            nome = "5600 XT"
        else:
            nome = "5600"
    elif re.search(pattern="580",string=name) != None:
        nome = "580"
    elif re.search(pattern="570",string=name) != None:
        nome = "570"
    return nome
    
def getModelRX(tipo,name,atribute):
    Name = None
    if re.search(pattern="6",string=tipo) != None:
        nome = RX6000(tipo,name)
        return nome
    elif re.search(pattern="5",string=tipo) != None:
        nome = RX5(tipo,name)
        return nome
    else:
        Name = RX6000(name,atribute)
        if Name == None:
            Name = RX5(name,atribute)
        return Name



def cleanName(tipo,name,atribute):
    tipo = tipo.upper()
    name = name.upper()
    atribute = atribute.upper()
    certo = False
    if re.search(pattern="RTX",string=tipo) != None:
        certo = True
        nome = getModelRTX(tipo,name,atribute)
    elif re.search(pattern="GTX",string=tipo):
        certo = True
        nome = getModelGTX(tipo,name,atribute)
    elif re.search(pattern="RX",string=tipo):
        certo = True
        nome = getModelRX(tipo,name,atribute)
    elif re.search(pattern="Vega64",string=tipo) != None:
        certo = True
        nome = "Vega64"
    elif re.search(pattern="Vega56",string=tipo) != None:
        certo = True
        nome = "Vega56"
    elif re.search(pattern="VII",string=tipo) != None:
        certo = True
        nome = "VII"
    if certo == True:
        return nome
    else:
        return None 
def cleanMemory(memory,value):
    memory = memory.upper()
    if re.search(pattern="GB",string=memory) != None:
        z = 0
        primeiro = True
        while (z < len(memory) - 1) and primeiro == True :
            if memory[z] == "G" and memory[z+1] == "B":
                primeiro = False
                try:
                    memoria = int(memory[z-2])*10 + int(memory[z-1])
                    return memoria
                except:
                    memoria = int(memory[z-1])
                    return memoria
            z = z + 1
        try:
            value = int(value[0])*10 + int(value[1])
            return value
        except:
            value = int(value[0])
            return value
    
    else:
        return None
def cleanPrice(preco_text,pontuacao):
    array = []
    for x in range(len(preco_text)):
        array.append(preco_text[x])
    if check_array(array,"R") == True:
        array.remove("R")
    if check_array(array,"$") == True:
        array.remove("$")
    if pontuacao == ",":
        if check_array(array,".") == True:
                array.remove(".")
    else:
        if check_array(array,",") == True:
            array.remove(",")
    for x in range(len(array)):
        if array[x] == pontuacao:
            posicao = x
    if len(array) > posicao + 3:
        for x in range(posicao + 3,len(array)):
            array.pop(x)   
    for x in range(len(array)):
        if x != posicao:    
            array[x] = float(array[x])
    value = number_array_to_value(array,posicao)
    return value