import random
Tabuleiro =[[" "," "," "],
            [" "," "," "],
            [" "," "," "]];

def reinicializar_tabuleiro():
    global Tabuleiro
    Tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

def verificaVitoria():
    pontoJogadorX = 1;
    pontoJogadorO = 0;
    nenhumPonto = -1;

    if Tabuleiro [0][0] == "X" and Tabuleiro [0][1] =="X" and Tabuleiro [0][2] == "X":
        print("Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [0][0] == "O" and Tabuleiro [0][1] =="O" and Tabuleiro [0][2] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [1][0] == "X" and Tabuleiro [1][1] =="X" and Tabuleiro [1][2] == "X":
        print(" Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [1][0] == "O" and Tabuleiro [1][1] =="O" and Tabuleiro [1][2] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [2][0] == "X" and Tabuleiro [2][1] =="X" and Tabuleiro [2][2] == "X":
        print(" Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [2][0] == "O" and Tabuleiro [2][1] =="O" and Tabuleiro [2][2] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [0][0] == "X" and Tabuleiro [1][0] =="X" and Tabuleiro [2][0] == "X":
        print(" Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [0][0] == "O" and Tabuleiro [1][0] =="O" and Tabuleiro [2][0] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [0][1] == "X" and Tabuleiro [1][1] =="X" and Tabuleiro [2][1] == "X":
        print(" Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [0][1] == "O" and Tabuleiro [1][1] =="O" and Tabuleiro [2][1] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [0][2] == "X" and Tabuleiro [1][2] =="X" and Tabuleiro [2][2] == "X":
        print("Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [0][2] == "O" and Tabuleiro [1][2] =="O" and Tabuleiro [2][2] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [0][0] == "X" and Tabuleiro [1][1] =="X" and Tabuleiro [2][2] == "X":
        print("Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro[0][0] == "O" and Tabuleiro [1][1] =="O" and Tabuleiro [2][2] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;

    elif Tabuleiro [0][2] == "X" and Tabuleiro [1][1] =="X" and Tabuleiro [2][0] == "X":
        print("Ponto para o jogador X")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorX;

    elif Tabuleiro [0][2] == "O" and Tabuleiro [1][1] =="O" and Tabuleiro [2][0] == "O":
        print("Ponto para o jogador O")
        imprimirTabuleiro()
        reinicializar_tabuleiro()
        return pontoJogadorO;
    else:
        return nenhumPonto;

def imprimirTabuleiro():

    print ("     C0  C1  C2 ")
    
    print("L0:   " + Tabuleiro [0][0] + " | " + Tabuleiro [0][1] + " | " + Tabuleiro [0][2])

    print ("   ---------------")

    print("L1:   " + Tabuleiro [1][0] + " | " + Tabuleiro [1][1] + " | " + Tabuleiro [1][2])

    print ("   ---------------")

    print("L2:   " + Tabuleiro [2][0] + " | " + Tabuleiro [2][1] + " | " + Tabuleiro [2][2])

    print ("   ---------------")

def lerCordenadaLinha():
    linha = int(input("digite a linha: "))
    return linha;

def lerCordenadaColuna():
    coluna = int(input("digite a coluna: "));
    return coluna;

def posicaoValida(linha,coluna):
    if linha < 0 or linha > 2:
        print("Digite um número válido de 0 a 2 para a linha.")
        return False
    elif coluna < 0 or coluna > 2:
        print("Digite um número válido de 0 a 2 para a coluna.")
        return False
    elif Tabuleiro[linha][coluna] != " ":
        print("Posição já preenchida. Escolha outra.")
        return False
    else:
        return True

def jogar(linha,coluna,tipoJogada):
    if tipoJogada == 0:
        Tabuleiro[linha][coluna] = "O"
    if tipoJogada == 1:
        Tabuleiro[linha][coluna] = lerJogada()
    if tipoJogada == 2:
        Tabuleiro[linha][coluna] = "X"

   
def jogadaUsuario(linha,coluna):
    validacao = posicaoValida(linha,coluna);
    while(validacao == False):
       linha= lerCordenadaLinha();
       coluna = lerCordenadaColuna()
       validacao = posicaoValida(linha,coluna);
    jogar(linha,coluna,1)

def jogadaUsuarioIA(linha,coluna):
    validacao = posicaoValida(linha,coluna);
    while(validacao == False):
       linha= lerCordenadaLinha();
       coluna = lerCordenadaColuna()
       validacao = posicaoValida(linha,coluna);
    jogar(linha,coluna,2)


def lerJogada():
    while True:
        jogada = input("Digite 'X' ou 'O': ").upper()
        if jogada == 'X' or jogada == 'O':
            return jogada
        else:
            print("Digite apenas 'X' ou 'O'")

def imprimirPontuacao(x,o):
    print (f"Pontuação X: {x}")
    print (f"Pontuação O: {o}")

def modoJogador():
    pontoJogadorX = 0
    pontoJogadorO = 0
    while pontoJogadorX < 3 and pontoJogadorO < 3:
        jogadas = 0
        while jogadas < 10:
            jogadas += 1
            imprimirPontuacao(pontoJogadorX,pontoJogadorO)
            verificador = verificaVitoria()
            if verificador == -1:
                imprimirTabuleiro()
                jogadaUsuario(lerCordenadaLinha(),lerCordenadaColuna())
            if verificador == 1:
                pontoJogadorX += 1
                jogadas = 0
                break
            elif verificador == 0:
                pontoJogadorO += 1
                jogadas = 0
                break
            if jogadas == 10:
                print("Xii... Deu velha")
                break
        if pontoJogadorX == 3:
            print("Vitoria Jogador X")
        elif pontoJogadorO == 3:
            print("Vitoria jogador O")
    print("Fim da partida")

def modo1vsIa():
    print("Você será o jogador X")
    pontoUsuario = 0
    pontoIa = 0
    while pontoUsuario < 3 and pontoIa < 3:
        jogadas = 0
        while jogadas <= 7:

            imprimirPontuacao(pontoUsuario, pontoIa)
            imprimirTabuleiro()
            jogadas += 1
            print(jogadas)
            jogadaUsuarioIA(lerCordenadaLinha(), lerCordenadaColuna())
            verificador = verificaVitoria()
            if jogadas == 5 and verificador == -1:
                print("Xiiiii , deu velha")
                reinicializar_tabuleiro()
                break
            if verificador == 1:
                pontoUsuario += 1
                jogadas = 0
                break
            elif verificador == 0:
                pontoIa += 1
                jogadas = 0
                break
            if verificador == -1:  # Verifica se o jogo continua
                jogadaIa(lerCordenadaLinhaIa(), lerCordenadaColunaIa())
                verificador = verificaVitoria()  # Verifica novamente após a jogada da IA
                if verificador == 1:
                    pontoUsuario += 1
                    jogadas = 0
                    break
                elif verificador == 0:
                    pontoIa += 1
                    jogadas = 0
                    break
    if pontoIa == 3:
        print("Fim !!!! Vitória para Ia")
    else:
        print("Fim!!! Você venceu , Parabéns")
            
def lerCordenadaLinhaIa():
    linha = random.randint(0, 2)
    return linha

def lerCordenadaColunaIa():
    coluna = random.randint(0, 2)
    return coluna

def jogadaIa(linha,coluna):
    validacao = posicaoValida(linha,coluna);
    while(validacao == False):
       linha= lerCordenadaLinhaIa();
       coluna = lerCordenadaColunaIa()
       validacao = posicaoValida(linha,coluna);
    jogar(linha,coluna,0)

def menu():
    print(
        """
        ----------------------
        Escolha o modo de jogo:
        1 - Modo 1v1 
        2- Modo 1vIA
        -----------------------
        """    
    )
    escolha = int(input("Digite a sua opção: "))
    if escolha == 1:
        modoJogador();
    elif escolha == 2: 
        modo1vsIa()
    else:
        print("Escolha uma das opções validas")
        menu()

menu()