# == 1 ==

# class Sensor:
#     def __init__(self, codigo):
#         self.codigo = codigo
#         self.ativo = True
    
#     def desligar(self):
#         self.ativo = False

# s1 = Sensor("S1")
# s2 = Sensor("S2")

# sensores = [s1, s2]
# sensores[0].desligar()


# print(sensores)
# print()
# print(s1, s2)

# == 2 ==

# class Disciplina:
#     def __init__(self, nome, professor):
#         self.nome = nome
#         self.professor = professor


# class Aluno:
#     def __init__(self, nome):
#         self.nome = nome
#         self.disciplinas = []
#         self.notas = {}

#     def adicionar_nota(self, disciplina, nota):
#         if disciplina not in self.disciplinas:
#             self.disciplinas.append(disciplina)

#         if disciplina.nome not in self.notas:
#             self.notas[disciplina.nome] = []

#         self.notas[disciplina.nome].append(nota)


# a = Aluno("João")
# d1 = Disciplina("Python", "Prof. Ana")
# d2 = Disciplina("Python", "Prof. Carlos")

# a.adicionar_nota(d1, 8)
# a.adicionar_nota(d2, 6)
# a.adicionar_nota(d1, 10)

# print(len(a.disciplinas), len(a.notas), a.notas["Python"])


# == 3 ==
# geracao = [
#     [3, 5, 0, 4],
#     [0, 0, 0, 6],
#     [7, 1, 0, 0]
# ]

# resultado = []

# for i in range(len(geracao)):
#     zeros = 0
#     for j in range(len(geracao[i])):
#         if geracao[i][j] == 0:
#             zeros += 1
#             if zeros >= 2:
#                 resultado.append(i)
#                 break
#         else:
#             zeros = 0

# print(resultado)


# == 4 ==
# from pathlib import Path
# import json

# PROXIMO = {
#     "novo": "contato",
#     "contato": "proposta",
#     "proposta": "ganho",
#     "ganho": "ganho"
# }


# class CRM:
#     def __init__(self, arquivo):
#         self.arquivo = Path(arquivo)
#         self.leads = self.carregar()

#     def carregar(self):
#         if not self.arquivo.exists():
#             return []
#         try:
#             return json.loads(self.arquivo.read_text(encoding="utf-8"))
#         except json.JSONDecodeError:
#             return []

#     def salvar(self):
#         texto = json.dumps(self.leads, ensure_ascii=False, indent=2)
#         self.arquivo.write_text(texto, encoding="utf-8")

#     def avancar_stage(self, email):
#         # for lead in self.leads:
#         #     if lead["email"].lower() == email.lower():
#         #         lead["stage"] = PROXIMO[lead["stage"]]
#         #         self.salvar()
#         #         return lead["stage"]
        
#         # for lead in self.leads:
#         #     if lead["email"].lower() == email.lower():
#         #         lead["stage"] = PROXIMO[lead["stage"]]
#         #         self.salvar()
#         #         return lead["stage"]
#         # else:

#         # leads = self.carregar()
#         # for lead in self.leads:
#         #     if lead["email"].lower() == email.lower():
#         #         lead["stage"] = PROXIMO[lead["stage"]]
#         #         self.salvar()
#         #         return lead["stage"]

#         # for lead in self.leads:
#         #     if lead["email"].lower() == email.lower():
#         #         lead["stage"] = PROXIMO[lead["stage"]]
#         #         return lead["stage"]
#         return None


# crm = CRM("leads_4.json")
# print(crm.avancar_stage("BRUNO@goodwe.com"))

# # simulando o programa sendo fechado e aberto novamente
# crm_reaberto = CRM("leads.json")
# print(crm_reaberto.leads[1]["stage"])


# == 5 ==
# class Inversor:
#     def __init__(self, modelo, potencia):
#         self.modelo = modelo
#         self.potencia = potencia
#         self.leituras = []

#     def registrar(self, valor):
#         self.leituras.append(valor)
#         return len(self.leituras)
    
# inv1 = Inversor("GW5000", 5000)
# inv2 = inv1
# inv3 = Inversor("GW5000", 5000)

# inv2.registrar(1200)
# inv1.registrar(800)
# total = inv3.registrar(300)

# print(len(inv1.leituras), len(inv3.leituras), total)



# == 6 ==
# class Medidor:
#     def __init__(self, local):
#         self.local = local
#         historico = []

#     def registrar(self, kwh):
#         if kwh < 0:
#             print("Leitura inválida")
#         else:
#             self.historico.append(kwh)

# m = Medidor("Bloco A")
# m.registrar(120)
# print(m.historico)



# == 7 ==
# import json
# import csv
# from pathlib import Path

# texto = """[
#     {"name": "Ana", "email": "ana@fiap.com.br", "stage": "novo"},
#     {"name": "Bruno", "email": "bruno@goodwe.com", "stage": "contato"},
#     {"name": "Ana Paula", "email": "ANA@fiap.com.br", "stage": "ganho"},
#     {"name": "Carla", "email": "carla@fiap.com.br", "stage": "proposta"}
# ]"""

# leads = json.loads(texto)

# unicos = {}
# for lead in leads:
#     chave = lead["email"].lower()
#     unicos[chave] = lead

# with open("export.csv", "w", newline="", encoding="utf-8") as f:
#     w = csv.DictWriter(f, fieldnames=["name", "stage"])
#     w.writeheader()
#     for lead in unicos.values():
#         w.writerow({"name": lead["name"], "stage": lead["stage"]})

# linhas = Path("export.csv").read_text(encoding="utf-8").splitlines()
# print(len(linhas), linhas[1])


# == 8 ==
# class Turma:
#     def __init__(self, codigo):
#         self.codigo = codigo
#         self.alunos = []  # lista de tuplas (rm, nome)
#         self.notas = []   # matriz: uma linha de checkpoints por aluno

#     def matricular(self, rm, nome, cps):
#         self.alunos.append((rm, nome))
#         self.notas.append(cps)

#     def media(self, i):
#         menor = self.notas[i][0]
#         for nota in self.notas[i]:
#             if nota < menor:
#                 menor = nota
#         return (sum(self.notas[i]) - menor) / (len(self.notas[i]) - 1)

#     def situacao(self):
#         resumo = {"APROVADO": [], "EXAME": [], "REPROVADO": []}

#         for i in range(len(self.alunos)):
#             m = self.media(i)

#             if m >= 6:
#                 chave = "APROVADO"
#             elif m >= 4:
#                 chave = "EXAME"
#             else:
#                 chave = "REPROVADO"

#             resumo[chave].append(self.alunos[i][1])

#         return resumo


# t = Turma("1CCPK")
# cps_caio = [2, 6, 2]

# t.matricular(101, "Ana", [5, 8, 9])
# t.matricular(102, "Bia", [3, 4, 5])
# t.matricular(103, "Caio", cps_caio)
# t.matricular(104, "Duda", [10, 1, 2])

# cps_caio[0] = 7

# r = t.situacao()
# print(r["APROVADO"], len(r["EXAME"]), r["REPROVADO"])
