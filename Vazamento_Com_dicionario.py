vazamento = {"BOBESPONJA":["SpongeBob@gmail.com","Garry@123"], "PATRICK":["PatrickStar@gmail.com", "AquiÉoPatrick"], "LULA MOLUSCO":["LulaMolusco@gmail.com", "EuSouUmPolvo"], "sandy":["Sandy@gmail.com", "AdoroNozes"], "PLANKTON":["Plankton@gmail.com", "KarenS2"], "CIRIGUEIJO":["SrCirigueijo@gmail.com", "$dinheiro$"], "CATDOG":["CatDog@gmail.com", "CatCat"],"MABEL":["MabelPynes@gmail.com", "familhaemoletons"], "DIPPER":["DipperPynes@gmail.com", "segredosdegravityfalls"], "BILLS":["BillCypher@gmail.com", "oPortãoEntreOsMundosEstaAberto"], "TIMMY":["Timmy@gmail.com", "CosmoWandaePoff"], "COSMO":["Cosmo@gmail.com", "LapisVerde"], "WANDA":["Wanda@gmail.com", "@poff123"], "BYLLI":["Bylli@gmail.com", "oAmorMudaAsPessoas"], "MANDY":["Mandy@gmail.com", "OdeioOBilly"], "PUROOSSO":["PuroOsso@gmail.com", "MorteaTodos"], "FLAPJACK":["FlapJack@gmail.com", "aventuras123"], "BOLHA":["bolha@gmail.com", "@familia123"], "CAPITAO":["Capitão@gmail.com", "BalasDoces"], "JOJO":["JonathanJoestar@gmail.com", "ErinaLOVE"], "DIO":["Dio@gmail.com", "aMascaraeMinha"], "FLORZINHA":["Florzinha@gmail.com", "desculpa"], "LINDINHA":["Lindinha@gmail.com", "mas"], "DOCINHO":["Docinho@gmail.com", "esta"], "RIGBY":["Rigby@gmail.com", "acabando"], "MORDECAI":["Mordecai@gmail.com", "minha"], "BENSON":["Benson@gmail.com", "criatividade"], "SALTITAO":["Saltitao@gmail.com", "sao"], "MUSCULOSO":["Musculoso@gmail.com", "muitas"], "FANTASMAO":["FantasMao@gmail.com", "senhas"]}
resp = "S"

while resp == "S":
    print("o que você pretende fazer? \n")
    print("1 - checar a lista de vazamento ")
    print("2 - buscar por um e-mail vazado ")
    print("3 - adicionar um novo vazamento ")
    print("4 - cancelar/sair")
    acao = int(input("escolha uma ação "))
    if acao == 1:
        for e in vazamento:
            print(e)
    elif acao == 2:
        busca = input("qual a tag? ").upper()
        lista = vazamento.get(busca)
        if lista != None:
            print("email.....", lista[0])
            print("senha.....", lista[1])
        else:
            print("tag não encontrada")
    elif acao == 3:
        tag = input("escreva a tag: ").upper()
        vazamento[tag] = [input("digite o e-mail: "), input("digite a senha: ")]
    elif acao == 4:
        print("Tchau")
        break 
    else:
        print("isso não é uma opção")
    resp = input("\nmais alguma coisa? S/N ").upper()
print("\nTchau\n")













