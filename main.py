
from tarefas import limpar, lista_tarefas, adicionar_tarefa, listar_tarefas, back, concluir_tarefa

while True:

    print("----- Menu de tarefas -----\n")
    print("1- Adicionar")
    print("2- Listar")
    print("3- Concluir")
    print("4- Sair\n")
    print("----------------------------")

    try:

        opcao = int(input("Escolha uma opção: "))

    except ValueError:

        print("ERRO: Escolha inválida. Tente novamente...")
        back()
        limpar()
        continue

    match opcao:

        case 1:
            limpar()
            print("----- Adicinar tarefa -----\n")
            adicionar_tarefa()
            print("")
            limpar()
            print("----- Adicinar tarefa -----\n")
            print("Tarefa adicionado na lista!\n")
            print("----------------------------")
            back()
            limpar()

        case 2:
            limpar()
            print("----- Lista de tarefas -----\n")
            listar_tarefas()
            print("")
            print("----------------------------")
            back()
            limpar()

        case 3:
            limpar()
            print("----- Concluir tarefa -----")



        case 4:
            limpar()
            print("Encerrando programa...")
            break

        case _:
            print("ERRO: Escolha inválida. Tente novamente...")
            back()
            limpar()
            continue
