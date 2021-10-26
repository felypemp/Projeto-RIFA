import random

def mostrarCartela():
    for linha in range(0,4): 
        for coluna in range (0,5):
            print(f'[{cartela[linha][coluna]:^4}]', end='')
    print()
print('-=' *15)
print()

cont = 0
print('-=' *15)

###### Cria uma matriz 4 x 5 (4 linhas e 5 colunas) ######## 
cartela = [ list(range(1,6)),
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20]
           ]
###### Cria uma lista com 20 elementos ######
listaNome = ['A','B','C','D','E','F','G','H','I','J','L','K','M','N','O','P','R','S','T','U']

###### Exibe a matriz no terminal######
mostrarCartela()

###### repete o codigo e incrementa o contador se a condição for verdadeira ######
while (cont != 20):
    print('Verifique a disponibilidade do número na cartela acima!')
    nome = input("Informe o nome do assinante: ")
    numEscolhido = int(input("Insira qual número deseja assinar: "))

    ###### Verifica se o numero escolhido esta entre 1 e 20 ######
    ###### Percorre a matriz e substitui o numero selecionado por * ######
    if numEscolhido >0 and numEscolhido <21:
        for linha in range(0,4):
            for coluna in range (0,5):
                if cartela[linha][coluna] == numEscolhido:
                    cartela[linha][coluna] = '*'


        print('-=' *15)            
        for linha in range(0,4):
            for coluna in range (0,5):
                 print(f'[{cartela[linha][coluna]:^4}]', end='')
            print()
        print('-=' *15)
        print()
        cont +=1
        ###### Adicina o nome na lista referente a posição escolhida ######
        listaNome[numEscolhido-1] = nome
 
    else:
        ### Exibe erro na tela caso o número escolhido não esteja entre 1 e 20 ###
        print()
        print('ERRO: Insira um número entre 1 e 20')
        print('PRESSIONE ENTER PARA CONTINUAR')
        input()

print('CARTELA COMPLETA. PRESSIONE ENTER PARA SORTEAR O NÚMERO!')
input()

###### Gera um número aleatório entre 1 e 20 e exibe-o na tela ######
num = random.randrange(1,20)
print(f'O número sorteado é: {num}')

###### Exibe o nome da lisa refente ao numero sorteado ######
print(f'Parabéns {listaNome[num-1]}!!!! ')

input()
