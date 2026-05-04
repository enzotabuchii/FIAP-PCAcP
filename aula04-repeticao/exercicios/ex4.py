soma = 0

for i in range(5):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    soma += valor

print(f"A soma de todos os valores digitados é: {soma}")