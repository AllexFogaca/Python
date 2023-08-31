"""
Metodo de substituição

Security = chave
5ecur1ty = senha

hex

1 = 1
2 = 2
9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
"""
chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "@"
    elif letra in "Bb":
        senha = senha + "8"
    elif letra in "Ee":
        senha = senha + "&"
    elif letra in "Ff":
        senha = senha + "7"
    elif letra in "Gg":
        senha = senha + "6"
    elif letra in "Ii":
        senha = senha + "1"
    elif letra in "Oo":
        senha = senha + "0"
    elif letra in "Xx":
        senha = senha + "*"
    else:
        senha = senha + letra
print(senha)
