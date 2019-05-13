from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)
dado3 = randint(1, 6)
dado4 = randint(1, 6)

jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

print("Jogador 1")
print("Primeiro dado:", dado1)
print("Segundo dado:", dado2)
print("\tTotal:", jogador1)

print("\nJogador 2")
print("Primeiro dado:", dado3)
print("Segundo dado:", dado4)
print("\tTotal:", jogador2)

