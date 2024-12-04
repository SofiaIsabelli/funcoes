#Crie uma função que calcule a equação do segundo grau.
print("--Exercicio 1---")
import math
def equacao(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return "Não há raízes reais" 
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    return raiz1, raiz2
resultado = equacao(1, -6, 8)
print(resultado)


#Escreva uma função chamada soma que recebe dois números como parâmetros e retorna a soma deles.
print("--Exercicio 2---")
def soma (x,y):
    x+y 
    return x+y
result = soma(10,10)
print(result)

#Escreva uma função chamada pares que recebe um número como parâmetro e retorna True se o número for par e False se ímpar.
print("--Exercicio 3---")
def pares(x):
    if (x %2==0):
        return True
    else:
        return False
valor = pares(5)
print(valor)

#Escreva uma função chamada fatorial que recebe um número inteiro não negativo como parâmetro e retorna o fatorial desse número. O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n.
print("--Exercicio 4---")
def fatorial(x):
    if (x==0 or x==1):
        return 1
    else:
        return x*fatorial(x-1)
print(fatorial(5))

#Escreva a função chamada primo que recebe um número inteiro como parâmetro e retorna True se o número for primo e Flase caso contrário.
print("--Exercicio 5---")
def primo(number):
    if number < 2:
        return False
    for i in range (2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        else:
            return True
resultado = primo (19)
print(resultado)