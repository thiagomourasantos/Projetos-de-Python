contador = 0
soma = 0
maiores_20 = 0
print("Digite valores ou Digite 'sair' para terminar")
while True:
    valor = input("Digite um valor: ")
    if valor == "sair":
        break
    try:
        numero = float(valor)
        contador += 1
        soma += numero
        if numero > 20:
            maiores_20 +=1
    except:
     print("Valor invalido")
media = soma / contador if contador > 0 else 0
print(f"Você digitou {contador} valores com a soma de {soma}, com a média de {media:.2f}, com {maiores_20} valores maiores que 20")



aprovados = 0
reprovados = 0
print("Digite as notas dos alunos (0 a 10) ou escreva 'sair' para terminar")
while True:
    entrada = input("Nota: ")
    if entrada == "sair":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            if nota >= 5:
                aprovados += 1
            else:
                reprovados += 1
        else:
            print("nota invalida digite um numero entre 0 e 10")
    except:print("entrada invalida")
total_alunos = aprovados + reprovados
print(f"RESULTADOS: Alunos que fizeram a prova = {total_alunos} , Aprovaods = {aprovados} , Reprovados =  {reprovados}")



soma_pares = 0
cont_pares = 0
soma_impares = 0
cont_impares = 0

print("Digite os números ou '0' para finalizar:")
while True:
    entrada = input("Número: ")

    if entrada == "0":
        break

    try:
        numero = int(entrada)
        if numero == 0:
            continue

        if numero % 2 == 0:
            soma_pares += numero
            cont_pares += 1
        else:
            soma_impares += numero
            cont_impares += 1
    except ValueError:
        print("Erro: Digite apenas números inteiros ou 0 para sair!")
media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
media_impares = soma_impares / cont_impares if cont_impares > 0 else 0
print("Resultados:")
print(f"Média dos pares: {media_pares:.2f}" if cont_pares > 0 else "Nenhum número par foi digitado")
print(f"Média dos ímpares: {media_impares:.2f}" if cont_impares > 0 else "Nenhum número ímpar foi digitado")