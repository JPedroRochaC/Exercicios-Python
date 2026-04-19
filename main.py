serieA = ['Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense']
serieB = ['Ceará', 'Sport', 'Fortaleza', 'Vila Nova', 'Novorizontino']
jogadores = []
posicoes = []

def escolher_time(lista):
    print('Times disponíveis:')
    for i, time in enumerate(lista):
        print(f'  {i} - {time}')
    escolha = int(input('Digite o número do time: '))
    if 0 <= escolha < len(lista):
        return lista[escolha]
    else:
        print('Número inválido!')
        return None

print('===PEDROFOOT===')
nome = input('Olá, treinador! Qual seu nome?\n==> ')
anos = int(input('Quantos anos de experiência você tem?\n==> '))

if anos > 4:
    serie = int(input('Você pode comandar times da SÉRIE A e B, qual você escolhe?\n1. SÉRIE A\n2. SÉRIE B\n==> '))
    if serie == 1:
        time_escolhido = escolher_time(serieA)
    elif serie == 2:
        time_escolhido = escolher_time(serieB)
    else:
        print('Escolha inválida!')
        time_escolhido = None
else:
    print('Você só pode comandar times da SÉRIE B')
    time_escolhido = escolher_time(serieB)

if time_escolhido:
    print(f'\nVocê escolheu o {time_escolhido}!')
    print(f'\nAGORA VAMOS MONTAR O ELENCO, {nome}!')

    adicionar = 'S'
    while adicionar == 'S':
        jogadores.append(input('Adicione um jogador ao seu time: '))
        posicoes.append(input('Qual a posição dele? '))
        adicionar = input('Deseja adicionar outro jogador? (S/N)\n==> ').upper()

    print(f'\n{nome}, seu elenco no {time_escolhido}:')
    for jogador_nome, posicao in zip(jogadores, posicoes):
        print(f'  - {jogador_nome} ({posicao})')