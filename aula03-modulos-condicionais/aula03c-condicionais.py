# --------------------------------------------------
# ESTRUTURA CONDICIONAL SIMPLES
# --------------------------------------------------

# nota_final = 8.0
#
# if nota_final < 6:
#     print("REPROVADO")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL COMPOSTA
# --------------------------------------------------

# nota_final = 8.0
#
# if nota_final < 6:
#     print("REPROVADO")
# else:
#     print("APROVADO")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL ENCADEADA
# --------------------------------------------------

# nota_final = 7.0
#
# if nota_final < 4:
#     print("REPROVADO")
# else:
#     if nota_final < 6:
#         print("RECUPERAÇÃO")
#     else:
#         print("APROVADO")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL ENCADEADA (elif)
# --------------------------------------------------

nota_final = 7.0

if nota_final < 4:
    print("REPROVADO")
elif nota_final < 6:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

print("FIM")
