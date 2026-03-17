"""
Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
Exemplo: nota a * 4 e nota b * 6.
"""

notaA = int(input("Digite a nota A: "))
notaB = int(input("Digite a nota B: "))

pesoA = notaA * 0.4
pesoB = notaB * 0.6

media = (pesoA + pesoB) / 2

print(f"A média é de {media}")
