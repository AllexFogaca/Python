"""
Exercicio - Trocar variaveis

"""

# Trocando variaveis em python

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

# Criaremos uma variavel temporaria

temp = x
x = y
y = temp

print(f"o valor de x depois da troca: {x}")
print(f"o valor de y depois da troca: {y}")
