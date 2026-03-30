idade = 70

if idade > 0:
    if idade < 16:
        print("Não pode votar")
    elif idade < 18 or idade >= 70:
        print("O voto é opcional")
    elif idade < 70:
        print("Voto é obrigatório")
