"""
▪ Crie um programa que receba o valor do produto e valor pago.
▪ Calcule o troco a ser pago.
▪ O valor do troco deve ser exibido no terminal.
"""

valor_produto = float(input("Digite o valor do produto: "))
valor_pago = float(input("Digite o valo pago: "))

troco = valor_pago - valor_produto

print(f"O troco é de R${troco}")
