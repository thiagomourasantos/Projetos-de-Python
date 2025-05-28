def conta_numeros():
    numeros = []
    while True:
        n = int(input("'Digite um número ou aperte -1 para sair: "))
        if n == -1:
            break
        numeros.append(n)
    quantidade = len(numeros)
    print(f"Você digitou {quantidade} numeros.")
if  __name__ == "__main__":
    conta_numeros






def media_turma():
    notas = []
    while True:
        entrada = float(input("Digite a nota do aluno ou digite -1 para sair: "))
        if entrada == -1:
            break
        notas.append(entrada)

    quantidade_alunos = len(notas)
    if quantidade_alunos == 0:
        print("Nenhuma nota foi digitada.")
    else:
        soma_notas = sum(notas)
        media = soma_notas / quantidade_alunos
        print(f"quantidade de alunos: {quantidade_alunos}")
        print(f"Média da turma: {media:.2f}")
if __name__ == "__main__":
    media_turma()