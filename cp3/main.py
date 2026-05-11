temp = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

room = 0
maior = 0
for i in temp:
    soma = 0
    cont = 0
    for j in i:
        if j >= 33:
            cont += 1
        soma += j
    room += 1
    media = soma / len(temp)

    if cont > maior:
        maior = cont
        maior_room = room

    print(
        f"""Sala {room} \nMédia: {media} \nRegistros críticos: {cont}\n"""
    )

print(f"Sala com maior risco: Sala {maior}")