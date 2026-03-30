escolha_usuario = 1
# 0 => sair do programa
# 1 => entrar no programa
# >>>> erro!

match escolha_usuario:
    case 0:
        print("SAIR DO PROGRAMA")
    case 1:
        print("ENTRAR NO PROGRAMA")
    case _:
        print("ERRO")
