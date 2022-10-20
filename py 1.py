print("\n ■■■ TORRE DE HANÓI ■■■\n")

torre = [[], [], []]

discos = int(input("\nQuantidade de discos (3 - 8): "))
for i in range(0, discos):
    torre[0].append(discos - i)

def mostrarTorres():
    print("\n Torre 1: ", torre[0], '\n', "Torre 2: ", torre[1],'\n', "Torre 3: ", torre[2])

def movimento():
    origem = int(input("\nTorre de origem: ")) - 1
    destino = int(input("\nTorre de destino: ")) - 1
    if origem >= 0 and origem <= 2 and destino >= 0 and destino <=2:
        if len(torre[origem]) != 0:
            if len(torre[destino]) == 0 or torre[origem][-1] <torre[destino][-1]:
                torre[destino].append(torre[origem][-1])
                torre[origem].remove(torre[origem][-1])
                mostrarTorres()

            else:  ("\n*** Movimento Inválido ***")
        else: print("\n*** Torre de Origem Vazia ***")
    else: print("\n*** Torre Inválida ***")

if discos > 2 and discos < 9:
    mostrarTorres()
    while len(torre[2]) != discos:
        movimento()
        print("\nSucesso!")
    else: print("*** Escolha entre 3 e 8 discos ***")