from matematica import *
from colorama import init, Fore
import os 


init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == "nt" else 'clear')

def menu():
    print(f"{Fore.BLUE}Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    print("0 - Sair")

def obter_numeros():
    a = input("Digite o primeiro número: ")
    while not a.isdigit():
         print(f"{a} não é um número, tente novamente!")
         a = input("Digite o primeiro número: ")
    a = float(a)

    b = input("Digite o segundo número: ")
    while not b.isdigit():
        print(f"{b} não é um número, tente novamente!")
        b = input("Digite o segundo número: ")

    b = float(b)
    return a, b

def destacarTexto(texto):
    print (f"{Fore.YELLOW}####################")
    print (f"{Fore.YELLOW}  {texto}   ")
    print (f"{Fore.YELLOW}####################")

def pausar():
    input("Pressione qualquer tecla para continuar...")

while True:
    menu()
    escolha = input(f"{Fore.BLUE}Digite o número da operação desejada: {Fore.RESET}")
    if escolha == '0':
        print("Encerrando o sistema!")
        break
    if escolha in ('1','2','3','4', '5'):
        num1, num2 =  obter_numeros()
        if escolha == '1':
            resultado = soma(num1, num2)
        elif escolha == '2':
            resultado = subtracao(num1, num2)
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
        elif escolha == '4':
            resultado = divisao(num1, num2)
        elif escolha    == '5':
            resultado = exponenciacao(num1, num2) 
        
        destacarTexto(resultado)
        pausar()
        limpar_tela()

    else:
        destacarTexto("Opção inválida! Tente novamente...")
