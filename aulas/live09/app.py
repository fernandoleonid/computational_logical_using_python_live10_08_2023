from manipulador_arquivos import *
import os
from colorama import init, Fore

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input ('Digite ENTER para continuar...')

def exibir_menu():
    print (f'{Fore.BLUE}#### MENU ####')
    print ('1 - Adicionar tarefa')
    print ('2 - Ler tarefas')
    print ('0 - Sair')
    print (f'{Fore.BLUE}##############')
    
def selecionar_menu(opcao):
    if opcao == '1':
        tarefa = input('Digite a tarefa: ')
        escrever_arquivo('controle_tarefas.txt', tarefa)
    elif opcao == '2':
        tarefas = ler_arquivo('controle_tarefas.txt')
        print (tarefas)
        pausar()
    elif opcao == '0':
        print (f'{Fore.RED}Saindo do sistema...')
        exit(0)
    else:
        print (f'{Fore.RED}Opção inválida. Tente novamente...')
        pausar()
    

def executar_sistema():
    limpar_tela()
    exibir_menu()
    opcao = input('Escolha uma opção: ')
    selecionar_menu(opcao)
    executar_sistema()

executar_sistema()

#Aguardando duvidas!!!