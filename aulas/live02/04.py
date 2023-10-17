#11. Calcule e apresente o valor de uma prestação
# em atraso, utilizando a fórmula 
# PRESTACAO = VALOR + (VALOR * TAXA/100) * TEMPO.

valor = float(input("Digite o valor: "))
taxa = float(input("Digite a taxa: "))
tempo = float(input("Digite o tempo: "))

prestacao = valor + (valor * taxa/100) * tempo

print (f"O valor da prestação em atraso é: {prestacao:.2f}")