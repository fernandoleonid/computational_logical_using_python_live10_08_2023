def menu():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    print("0 - Sair")

def obter_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

def soma(n1, n2):
    r = n1  + n2
    return f"{n1} + {n2} = {r}"

def subtracao(n1, n2):
    r = n1 - n2
    return f"{n1} - {n2} = {r}"

def multiplicacao(n1, n2):
    r = n1 * n2
    return f"{n1} * {n2} = {r}"
def divisao(n1, n2):
    if n2 == 0:
        return "Não existe divisão por zero"
    r = n1 / n2
    return f"{n1} / {n2} = {r}"

def exponenciacao(n1, n2):
    r = n1 ** n2
    return f"{n1} ** {n2} = {r}"

def destacarTexto(texto):
    print ("####################")
    print (f"  {texto}   ")
    print ("####################")

while True:
    menu()
    escolha = input("Digite o número da operação desejada: ")
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

    else:
        destacarTexto("Opção inválida! Tente novamente...")
