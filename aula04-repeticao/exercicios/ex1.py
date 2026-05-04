while True:
    print("Olá, Mundo!")
    deseja_continuar = input("Desejas continuar? ").strip().lower()

    if deseja_continuar not in ["sim", "s", "yes", "y"]:
        break
