import math

raio = float(input("Escreva o valor do Raio: "))
calculo = (4/3)*math.pi*(raio**3)
volume_da_esfera=print("O volume é:",calculo)


massa=int(input("Digite seu peso: "))
agua = massa*0.03
print("Você deve ingerir:",agua,"litros de agua")


x1 = int(input("Digite o x do ponto P: "))
y1 = int(input("Digite o y do ponto P: "))
x2 = int(input("Digite o x do ponto Q: "))
y2 = int(input("Digite o y do ponto Q: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"A distância entre dois pontos P e Q é: {distancia}")


numero = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
if numero > numero2:
    print(f"{numero} é maior que {numero2}")
elif numero < numero2:
    print(f"{numero2} é maior que {numero}")
else:
    print("Os números são iguais")


altura = float(input("Digite sua altura: "))

peso_h = (72.7 * altura) - 58
peso_m = (62.1 * altura) - 44.7

sexo = input("Digite seu sexo (h para homem, m para mulher): ").strip().lower()

if sexo == "h":
    print(f"Seu peso ideal é: {peso_h:.2f} kg")
elif sexo == "m":
    print(f"Seu peso ideal é: {peso_m:.2f} kg")

