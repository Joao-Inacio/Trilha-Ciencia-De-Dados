import random
from collections import Counter


def zeroR_classificador(rotulos):
    contagem = Counter(rotulos)
    mais_comum = contagem.most_common(1)[0][0]
    return mais_comum

rotulos = ["pedra", "papel", "tesoura"]
predicao = zeroR_classificador(rotulos)
print(f"Classe prevista pelo ZeroR: {predicao}")

# while True:
#     print("Escolha uma opção (1, 2, 3 ou 4): \n1-Pedra \n2-Papel \n3-Tesoura \n4-Sair ")
#     jogador = str(input())
#     pc = random.randint(1, 4)
#     if jogador == "1" and pc == "3":
#         print("Jogador ganho")
#     elif jogador == "2" and pc == "1":
#         print("Jogador ganho")
#     elif jogador == "3" and pc == "2":
#         print("Jogador ganho")
#     elif pc == "1" and jogador == "3":
#         print("pc ganho")
#     elif pc == "2" and jogador == "1":
#         print("pc ganho")
#     elif pc == 3 and jogador == "2":
#         print("pc ganho")
#     elif jogador == "4":
#         print(pc)
#         break
