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