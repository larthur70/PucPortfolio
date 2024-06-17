import random

def jogo(jogada1,jogada2):
    pontuacaoJ1 = 0
    pontuacaoJ2 = 0

    pontuacao = [[0,-1,1],[1,0,-1],[-1,1,0]]

    codigos = {
        '1': 0,
        '2': 1,
        '3': 2 
    }

    ponto = pontuacao[codigos[jogada1]][codigos[jogada2]]
    if ponto == 0:
        return 'Empate',pontuacaoJ1,pontuacaoJ2
    elif ponto == 1:
        pontuacaoJ1 = 1
        return 'Jogador 1 venceu',pontuacaoJ1,pontuacaoJ2
    else:
        pontuacaoJ2 = 1
        return 'jogador 2 venceu',pontuacaoJ1,pontuacaoJ2
        
opcoesValidas = ['1','2','3'] 
opcoesEscritas = ['Pedra','Papel','Tesoura']      

while True:
    pontuacao1 = 0
    pontuacao2 = 0
    modalidade = input("[1]humano x humano [2]humano x computador [3]computador x computador: ")

    if modalidade not in opcoesValidas:
        print("Digte uma opção válida")
        continue

    while True:

        if modalidade == '1':
            jogador1 = input("Jogador 1: [1]Pedra [2]Papel [3]Tesoura: ")
            jogador2 = input("Jogador 2: [1]Pedra [2]Papel [3]Tesoura: ")
        elif modalidade == '2':
            jogador1 = input("Jogador 1: [1]Pedra [2]Papel [3]Tesoura: ")
            jogador2 = str(random.randrange(1,4))
        elif modalidade == '3':
            jogador1 = str(random.randrange(1,4))
            jogador2 = str(random.randrange(1,4))

        if jogador1 not in opcoesValidas or jogador2 not in opcoesValidas:
                print("Digite uma jogada válida")
                print("Tente de novo")
                continue

        resultado = jogo(jogador1,jogador2)

        pontuacao1 += resultado[1]
        pontuacao2 += resultado[2]

        indiceEscrito1 = int(jogador1) - 1
        indiceEscrito2 = int(jogador2) - 1
        print(f'{opcoesEscritas[indiceEscrito1]} X {opcoesEscritas[indiceEscrito2]}')
        print(f'{resultado[0]} Pontuação J1:{pontuacao1} J2:{pontuacao2}')
            
        escolha = input("[S]air ou [C]ontinuar: ")

        if pontuacao1 > pontuacao2:
            vencedor = 'Jogador1'
        elif pontuacao1 == pontuacao2:
            vencedor = 'Empate'
        else:
            vencedor = 'Jogador2'

        if escolha.lower() == 'c':
            continue
        elif escolha.lower() == 's':
            print(f"O vencedor é o {vencedor}")
            print(f'Placar geral: Jogador 1: {pontuacao1} Jogador 2: {pontuacao2}\
                  Obrigado pro jogar, de Luiz Arthur Lima')
            break
        else:
            print("Você não digitou sair, então irei continuar")
    break   