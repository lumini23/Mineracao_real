import att_planilha
import criar_planilha

end = False
while end == False:
    resposta = int(input("\n 1: Criar planilha \n 2: Atualizar tudo \n 3: Atualizar um aspecto \n 0: Sair \n Digite aqui: "))
    if resposta == 1:
        #criar planilha
        None
    elif resposta == 2:
        print("\n Digite o local do arquivo que deseja atualizar")
        print(" Exemplo: /Users/daniel/Computacao/Python_excel_1/env/project/Minerando_crypto.xlsx")
        local = str(input("\n Digite aqui: "))
        att = att_planilha.planilha(local)
        print("\n Atualizando Rentabilidade... ")
        att.atualizarRentabilidade(local)
        print("\n Atualizando Lucro... ")
        att.atualizarLucro(local)
        print("\n Atualizando Dolar... ")
        att.atualizarDolar(local)
    elif resposta == 3:
        final = False
        print(" Digite o local do arquivo que deseja atualizar")
        print(" Exemplo: /Users/daniel/Computacao/Python_excel_1/env/project/Minerando_crypto.xlsx")
        local = str(input("\n Digite aqui: "))
        att = att_planilha.planilha(local)
        while final == False:
            resposta = int(input("\n 1: atualizar rentabilidade \n 2: atualizar lucro \n 3: atualizar dolar \n 0: Voltar \n Digite aqui: "))
            if resposta == 1:
                print("\n Atualizando Rentabilidade... ")
                att.atualizarRentabilidade(local)
            elif resposta == 2:
                print("\n Atualizando Lucro... ")
                att.atualizarLucro(local)
            elif resposta == 3:
                print("\n Atualizando Dolar... ")
                att.atualizarDolar(local)
            elif resposta == 0:
                final = True
            else:
                print("\n Voce digitou errado por favor tente novamente")
    elif resposta == 0:
        end = True
    else:
        print("\n Voce digitou errado, tente novamente \n")
    
