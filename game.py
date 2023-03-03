import random

def jogo():
    opcoes = ["pedra", "papel", "tesoura"]

    pj = 0
    pc = 0

    while True:
        jogador = input('Escolha pedra, papel ou tesoura (ou sair para encerrar o jogo): ').lower()

        if jogador == "sair":
            print('Fim do jogo!')
            print(f" Pontuação final:\n Jogador: {pj} x {pc} Computador")
            break

        if jogador not in opcoes:
            print('Opção invalida. tente novamente.')
            continue

        computador = random.choice(opcoes)
        print(f"O computador escolheu {computador}")

        if jogador == computador:
            print("Empate!")
        elif jogador == "pedra" and computador == "tesoura":
            print("Jogador venceu!")
            pj += 1
        elif jogador == "papel" and computador == "pedra":
            print("Jogador venceu!")
            pj += 1
        elif jogador == "tesoura" and computador == "papel":
            print("Jogador venceu!")
            pj += 1
        else:
            print("Computador venceu!")
            pc += 1

            print(f"Pontuação: Jogador {pj} x {pc} Computador")

jogo()