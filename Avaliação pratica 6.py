def mostrar_mensagem(mensagem , numero):
    print(mensagem, numero)
def main():
    msg = input("Digite uma mensagem: ")
    num = float(input("Digite um numero: "))
    mostrar_mensagem(msg , num)
if __name__ == "__main__":
    main()



def motra_idade(idade):
    print(f"Você tem {idade} anos")
def main():
    nascimento = int(input("Digite seu ano de nascimento: "))
    calculo = 2025 - nascimento
    motra_idade(calculo)
if __name__ == "__main__":
    main()



def mostra_resultado(resultado):
    print(f"a soma dos valores é {resultado}")
def main():
    valor = int(input("Difite um valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))
    calculo_de_valores = valor + valor2 + valor3
    mostra_resultado(calculo_de_valores)
if __name__ == "__main__":
    main()



def e_par(numero):
    return numero % 2 == 0
def main():
    num = int(input("Digite um número: "))
    if e_par(num):
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é impar")
if __name__ == "__main__":
    main()
