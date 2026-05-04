maior = 0
for i in range(5):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    if maior is None or valor > maior:
        maior = valor
print(f"O maior valor é: {maior}")