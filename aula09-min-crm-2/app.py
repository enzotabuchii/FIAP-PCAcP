from model import model_lead
import controller

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa no funil: ")

    # valida os dados aqui!!!
    # depois de valida, é necessário modelar o lead como um dict
    # usamos o model

    print(model_lead(name, email, stage))

    # agora com o lead modeloado como um dict
    # precisamos enviar esse lead para os leads.json
    # para isso, vamos usaro o controller

    controller.create_lead(model_lead(name, email, stage))

def list_leads():
    leads = controller.read_leads()

    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    # validar query

    search_results = controller.read_leads_search(query)
    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def export_leads():
    path_csv = controller.export_csv()
    if path_csv is None:
        print("Não foi possível exportar para csv")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
