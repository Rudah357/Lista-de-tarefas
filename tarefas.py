
import os, time, json

lista_tarefas = []

def back():
    back = input("0 --> Back\n")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar_tarefa():

    tarefas = input("Adicione uma tarefa na lista:\n")

    tarefa_dict = {"nome": tarefas.strip().capitalize(), "concluida": False}

    lista_tarefas.append(tarefa_dict)

def listar_tarefas():

    if not lista_tarefas: 

        print("A lista de tarefas está vazia.")

    else:

        for id, tarefa in enumerate(lista_tarefas, start=1):

            status = "🟢" if tarefa["concluida"] else "🔴"

            print(f"# ID: {id} | Tarefa: {tarefa['nome']} | Concluída: {status} |")

def concluir_tarefa():


    entrada = input("Digite o ID ou o Nome da tarefa para concluir (ou 0 para sair): \n")

    if entrada == "0":
        return
    
    achou = False

    if entrada.isdigit():
        indice = int(entrada) - 1
        if 0 <= indice < len(lista_tarefas):
            lista_tarefas[indice]["concluida"] = True
            achou = True

    if not achou:
        for tarefa in lista_tarefas:
            if tarefa["nome"].lower() == entrada.lower():
                tarefa["concluida"] = True
                achou = True
                break

    if achou:
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")

def remover_tarefa():

    entrada = input("Digite o ID ou o Nome da tarefa para removê-la da lista (ou 0 para sair): \n")

    if entrada == "0":
        return

    removido = False

    if entrada.isdigit():
        indice = int(entrada) - 1
        if 0 <= indice < len(lista_tarefas):
            tarefa_removida = lista_tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['nome']}' removida!")
            removido = True

    if not removido:
        for tarefa in lista_tarefas:
            if tarefa["nome"].lower() == entrada.lower():
                lista_tarefas.remove(tarefa)
                print(f"Tarefa '{tarefa['nome']}' removida!")
                removido = True
                break

    if not removido:
        print("Tarefa não encontrada.")

def salvar_dados():

    with open("Lista-de-tarefas.json", "w") as arquivo:

        json.dump(lista_tarefas, arquivo, indent=4)

def carregar_dados():

    global lista_tarefas
    if os.path.exists("Lista-de-tarefas.json"):

        try:

            with open("Lista-de-tarefas.json", "r") as arquivo:
                lista_tarefas = json.load(arquivo)

        except FileNotFoundError:

            print("Arquivo não encontrado!")

    else:

        lista_tarefas = []
