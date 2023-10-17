# 2. Crie um programa que solicite ao usuário o 
# início, o fim e o número para a tabuada. 
# Em seguida, exiba a tabuada desse número no 
# intervalo determinado. 

print (" -- TABUADA --")

numero =  int(input("Digite um número para a tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

for contador in range(inicio, fim+1):
    produto = numero * contador
    print (f"{numero} X {contador} = {produto}")
