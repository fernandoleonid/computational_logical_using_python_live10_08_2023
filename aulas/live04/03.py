# Crie uma lista chamada notas com 5 notas. 
# Calcule a média das notas e imprima o 
# resultado.

notas = []
for contador in range(1,6):
    notaDigitada = int(input(f"Digite a nota {contador}: "))
    notas.append(notaDigitada)

media = sum(notas) / len(notas)

print (f"Sua média é: {media}")