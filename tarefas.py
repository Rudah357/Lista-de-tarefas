
import os, time

lista_tarefas = []

def back():
    back = input("0 --> Back\n")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar_tarefa():

    tarefas = input("Adicione uma tarefa na lista:\n")

    tarefa_dict = {"nome": tarefas, "concluida": False}

    lista_tarefas.append(tarefa_dict)

def listar_tarefas():

    if not lista_tarefas: 

        print("A lista de tarefas está vazia.")

    else:

        for id, tarefa in enumerate(lista_tarefas, start=1):

            conclusao = False
            falso_ou_true = "🟢" if conclusao else "🔴"

            print(f"# ID: {id} | Tarefa: {tarefa} | Concluída: {falso_ou_true} |")

def concluir_tarefa():

    entrada = input("Digite o ID ou o Nome da tarefa para concluir: ")
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

