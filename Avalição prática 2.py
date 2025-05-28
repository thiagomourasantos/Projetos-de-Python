valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor2 > valor1:
    print(f"{valor2} é maior que {valor1}")
else:
    print("valores iguais")




num = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num > num2:
    if num > num3:
        maior = num
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3

print(f"O maior valor é:{maior}")



num = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num >= num2 and num >= num3:
    maior = num
elif num2 >= num and num2 >= num3:
    maior = num2
else:
    maior = num3

print(f"O maior valor é:{maior}")



print("Calculadora Básica (+ , - , * , /)")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2


print(f"Resultado: {resultado}")




lado1 = float(input("Digite o primeiro valor: "))
lado2 = float(input("Digite o segundo valor: "))
lado3 = float(input("Digite o terceiro valor: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")



