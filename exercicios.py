import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# x = int(input("valor 1:"))
# y = int(input("valor 2:"))
# z = x + y

# print(z)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# x = int(input("valor 1:"))

# z = x % 5

# print(z)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# x = int(input("valor 1:"))
# y = int(input("valor 2:"))
# z = x * y

# print(z)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# x = int(input("valor 1:"))
# y = int(input("valor 2:"))
# z = x / y

# print(int(z))

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# x = float(input("valor 1:"))
# y = float(input("valor 2:"))
# z = x + y
# print(z)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# x = float(input("valor 1:"))
# y = float(input("valor 2:"))
# z = (x + y)/2
# print(z)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# x = float(input("valor 1:"))
# y = float(input("valor 2:"))
# z = x ** 2
# print(z)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# x = float(input("valor 1:"))

# z = x * (9/5) + 32
# print(z)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# x = float(input("valor 1:"))

# z = math.pi * (x**2)
# print(z)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# x = str(input("valor 1:"))

# print(x.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# x = str(input("nome completo: "))

# print(x.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# x = str(input("nome completo: "))

# print(x.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# x = str(input("igitar uma data no formato 'dd/mm/aaaa' "))

# y = x.split("/")
# print(y)
# print(y[0])
# print(y[1])
# print(y[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# x = str(input("nome : "))
# y = str(input("sobrenome : "))

# print(x + y)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# x = bool(input("valor 1:"))
# y = bool(input("valor 2:"))
# z = x and y
# print(z)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# x = bool(input("valor 1:"))
# y = bool(input("valor 2:"))
# z = x or y
# print(z)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# x = bool(input("valor 1:"))

# z = not x
# print(z)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# x = int(input("valor 1:"))
# y = int(input("valor 2:"))

# if x == y:
#     print("são iguais")
# else:
#     print("nao sao iguais")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# x = int(input("valor 1:"))
# y = int(input("valor 2:"))

# if x != y:
#     print("nao sao iguais")
# else:
#     print("sao iguais")

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     numero = int(input("valor 1:"))

#     z = numero * (9/5) + 32
#     print(z)
# except:
#     print("voce nao digitou um numero")

# 22: Verificador de Palíndromo
# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples

# try:

#     num_1 = int(input("Insira o primeiro numero: "))
#     num_2 = int(input("Insira o segundo numero: "))
    
#     operacao = input("Insira a operação desejada: ")

#     if operacao == "+":
#         resultado = num_1 + num_2
#     elif operacao == "-":
#         resultado = num_1 - num_2
#     elif operacao == "/":
#         resultado = num_1 / num_2
#     elif operacao == "*":
#         resultado = num_1 * num_2

#     print(resultado)
# except:
#     print("Voce digitou um valor não aceito")

# 24: Classificador de Números

# try:

#     num_1 = int(input("Insira o primeiro numero: "))    

#     if num_1 < 0:
#         print("O numero inserido é negativo")
#     elif num_1 > 0:
#         print("O numero inserido é positivo")
#     elif num_1 == 0:
#         print("O numero inserido é zero")

# except:
#     print("Voce digitou um valor não aceito")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except:
    print("Insira um valor inteiro")