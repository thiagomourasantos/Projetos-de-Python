def positivo_nulo_negativo(x):
    if x > 0:
        print("Valor Positivo")
    elif x == 0:
        print("Valor Nulo")
    else:
        print("Valor Negativo")
if __name__ == "__main__":
    n = float(input("Digite um número qualquer:"))
    positivo_nulo_negativo(n)





def valor_absoluto(x):
    if x < 0:
        return -x
    else:
        return x
if __name__ == "__main__":
    n = float(input("Digite um numero qualquer:"))
    mod = valor_absoluto(n)
    print(f"o valor absoluto de {n} é {mod}")





def soma(a,b):
    print(f"{a} + {b} = {a + b}")
def subitracao(a,b):
    print(f"{a} - {b} = {a - b}")
def multiplicao(a,b):
    print(f"{a} * {b} = {a * b}")
def divisao(a,b):
    print(f"{a} / {b} = {a / b}")
if __name__ == "__main__":
    op = input("Escolha a opereção (+,-,*,/):")
    x = float(input("Digite o primeiro valor:"))
    y = float(input("Digite o segundo valor:"))
    if op == "+":
        soma(x,y)
    elif op == "-":
        subitracao(x,y)
    elif op == "*":
        multiplicao(x,y)
    elif op == "/":
        divisao(x,y)




def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *=i
    return  resultado
if __name__ == "__main__":
    n = int(input("Digite um número inteiro não negativo:"))
    if n < 0:
        print("Erro")
    else:
        print(f"O fatorial de {n} é {fatorial(n)}")