print(f"{'Fahrenheit':>10} | {'Celsius':>8}")
print("-" * 30)

for f in range(45, 81):
    c = 5 * (f - 32) / 9
    print(f"{f:10.1f} °F | {c:8.3f} °C")



inicio = int(input("Digite o valor inicial em °F: "))
fim = int(input("Digite o valor final em °F: "))

print(f"\n{'Fahrenheit':>10} | {'Celsius':>8}")
print("-" * 30)

if inicio <= fim:
    for f in range(inicio, fim + 1):
        c = 5 * (f - 32) / 9
        print(f"{f:10.1f} °F | {c:8.3f} °C")
else:
    for f in range(inicio, fim - 1, -1):
        c = 5 * (f - 32) / 9
        print(f"{f:10.1f} °F | {c:8.3f} °C")




soma = 0
for i in range(1, 501):
    soma += i
print("A soma dos números de 1 a 500 é:", soma)




soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print("A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é:", soma)





for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")




numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{i} x {numero} = {i * numero}")

