"""
como descobrir se é um numero impar ou par

"""

print(60 * "-")
numero = int(input("Insira um numero para saber se e impar ou par: "))
if (numero % 2) == 0:  # se o resto da divisão for 0 é par
    print(f"{numero} e um numero par")
else:
    print(f"{numero} e um numero impar")
print(60 * "-")
