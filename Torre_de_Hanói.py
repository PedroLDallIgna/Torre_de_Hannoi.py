##Torre de Hanói
##Instituto Federal Catarinense - Campus Concórdia
##Trabalho da disciplina de Fundamentos de Lógica e Algoritmos - Professor Hewerton Enes de Oliveira
##Micael Sabadin Presotto - 2019328089; Pedro Lucas Dall' Igna - 2019310119.

import sys

jogadas = 0
h1 = []
h2 = []
h3 = []
hasteInicial = []
micaeportugalindos = True

def verificacao(dQual, pQual, jogadas):
    if len(dQual) == 0:
        print("MOVIMENTO INVÁLIDO")
        jogadas = jogadas
    elif len(dQual) != 0:
        if len(pQual) == 0:
            pQual.append(dQual[-1])
            del(dQual[-1])
            jogadas = jogadas + 1
            print("Ja foram %s jogada(s)" % jogadas)
        elif len(pQual) != 0:
            if pQual[-1] < dQual[-1]:
                print("MOVIMENTO INVÁLIDO!")
            else:
                pQual.append(dQual[-1])
                del(dQual[-1])
                jogadas = jogadas + 1
                print("Ja foram %s jogada(s)" % jogadas)
        
def ganhador():
    global micaeportugalindos, h1, h2, h3, nPecas, jogadas, hasteInicial
    if h3 == hasteInicial:
        print('Parabéns você ganhou')
        micaeportugalindos = input("Desejas jogar novamente? (Y/N): ").upper()
        if micaeportugalindos == 'Y':
            h1 = []
            h2 = []
            h3 = []
            hasteInicial = []
            jogadas = 0
            nPecas = int(input("Número de peças: "))
            print('Seu número mínimo de jogadas é',2**nPecas-1)
            for i in range(nPecas, 0, -1):
                h1.append(i)
                hasteInicial.append(i)
        
            print()
            print("Haste 1:", h1)
            print("Haste 2:", h2)
            print("Haste 3:", h3)
            print()
            micaeportugalindos = True
        elif micaeportugalindos == 'N':
            print('Obrigado por jogar!!!')
            micaeportugalindos = False
            sys.exit()
##        if jogadas < 2**nPecas-1:
##            print("Você não atingiu o número mínimo de jogadas! Você roubou,ladrao")
        
def torre(dQual, pQual, h1, h2, h3):
    verificacao(dQual, pQual, jogadas)
    print()
    print("Haste 1:", h1)
    print("Haste 2:", h2)
    print("Haste 3:", h3)
    print()
    ganhador()

while micaeportugalindos == True:
    nPecas = int(input("Número de peças: "))
    print('Seu número mínimo de jogadas é',2**nPecas-1)
    for i in range(nPecas, 0, -1):
        h1.append(i)
        hasteInicial.append(i)
        
    print()
    print("Haste 1:", h1)
    print("Haste 2:", h2)
    print("Haste 3:", h3)
    print()

    while h3 != range(nPecas, 0, -1):
        dQual = int(input("De qual haste você deseja mover: "))
        while dQual != 1 and dQual != 2 and dQual != 3:
            dQual = int(input("DADO INVÁLIDO! De qual haste você deseja mover: "))
        else:
            if dQual == 1:
                dQual = h1
            elif dQual == 2:
                dQual = h2
            elif dQual == 3:
                dQual = h3    
        pQual = int(input("Para qual haste você deseja mover: "))
        while pQual != 1 and pQual != 2 and pQual != 3:
            pQual = int(input("DADO INVÁLIDO! De qual haste você deseja mover: "))
        else:
            if pQual == 1:
                pQual = h1
            elif pQual == 2:
                pQual = h2
            elif pQual == 3:
                pQual = h3
        
        torre(dQual, pQual, h1, h2, h3)