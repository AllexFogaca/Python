"""

Descobrir se o numero eh primo

"""

print(30 * "-")

numero = int(input("Insira um numero: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Este nao eh um numero primo")
            break
    else:
        print("Este numero é primo")
else:
    print("Este numero não é primo")

print(30 * "-")
