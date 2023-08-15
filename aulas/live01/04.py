# Leia dois valores (inteiros, reais ou caracteres) 
# para as variáveis A e B, e efetue a troca dos valores 
# de forma que a variável A passe a possuir o valor da 
# variável B e a variável B passe a possuir o valor da 
# variável A. Apresente os valores trocados.

a = input ("Digite um valor para A: ") 
b = input ("Digite um valor para B: ") 

auxiliar = a
a = b
b = auxiliar

print ("Valor trocados:")
print (f"A = {a}")
print (f"B = {b}")