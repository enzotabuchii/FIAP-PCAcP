"""
Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro
levou para percorrer essa distância?
"""

km = float(input("Digite quanto que o carro percorreu (em km): "))
vel = int(input("Digite a velocidade média do carro: "))
hora = km / vel

print(f"O carro percorreu {km} em {hora}h")
