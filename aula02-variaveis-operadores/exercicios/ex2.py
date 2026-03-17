"""
Converta uma temperatura de Fahrenheit para Celsius. A fórmula de conversão é: Celsius = (Fahrenheit
- 32) * 5/9.
"""

fahrenheit = float(input("Digite uma temperatura em Fahrenheit: "))
celsius = fahrenheit - 32 * 5 / 9

print(f"A temperatura em celsius é: {celsius}")
