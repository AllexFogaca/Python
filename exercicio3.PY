"""
Escreva um programa que leia 5 valores e encontre o maior e o
menor deles. Mostre o resultado.

"""

n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
n3 = int(input("Digite um numero:"))
n4 = int(input("Digite um numero:"))
n5 = int(input("Digite um numero:"))

if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            if n1 > n5:
                print("O MAIOR NUMERO É O:", n1)
if n2 > n1:
    if n2 > n3:
        if n2 > n4:
            if n2 > n5:
                print("O maior numero é o:", n2)
if n3 > n1:
    if n3 > n2:
        if n3 > n4:
            if n3 > n5:
                print("O maior numero é o:", n3)
if n4 > n1:
    if n4 > n2:
        if n4 > n3:
            if n4 > n5:
                print("O maior numero é o:", n4)
if n5 > n1:
    if n5 > n2:
        if n5 > n3:
            if n5 > n4:
                print("O maior numero é o:", n5)

if n1 < n2:
    if n1 < n3:
        if n1 < n4:
            if n1 < n5:
                print("O menor numero é o:", n1)
if n2 < n1:
    if n2 < n3:
        if n2 < n4:
            if n2 < n5:
                print("O menor numero é o:", n2)
if n3 < n1:
    if n3 < n2:
        if n3 < n4:
            if n3 < n5:
                print("O menor numero é o:", n3)
if n4 < n1:
    if n4 < n2:
        if n4 < n3:
            if n4 < n5:
                print("O menor numero é o:", n4)
if n5 < n1:
    if n5 < n2:
        if n5 < n3:
            if n5 < n4:
                print("O menor numero é o:", n5)
