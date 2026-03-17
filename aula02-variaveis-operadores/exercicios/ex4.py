"""
Você comprou 3 livros por R$ 25 cada e 2 canetas por R$ 5 cada. Calcule o total gasto.
"""

livros = int(input("Digite a quantidade de livros que comprou: "))
preco_livro = float(input("Digite o preço do livro: "))
canetas = int("Digite a quantidade de canetar que comprou: ")
preco_caneta = float(input("Digite o preço da caneta: "))

total_livro = livros * preco_livro
total_caneta = canetas * preco_caneta
total = total_livro + total_caneta

print(f"Total gasto nos livros: {total_livro}")
print(f"Total gasto nas canetas {total_caneta}")
print(f"Total gasto nos dois {total}")
