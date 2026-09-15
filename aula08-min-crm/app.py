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
    print(controller.read_leads())
    # desafio: formatar como tabela

def main():
    while True:
        print("\nMini CRM de Leads")
        print("\n[1] Adicionar lead")
        print("\n[2] Listar lead")
        print("\n[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar lead")
        elif opt == "0":
            print("Até mais...")
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
