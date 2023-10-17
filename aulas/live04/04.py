# Crie uma lista de números inteiros. 
# Em seguida, crie uma nova lista chamada dobro 
# que contenha o dobro de cada número da lista original.
# Crie uma lista chamada quadrado
# Crie uma lista com os números pares
# Crie uma lista com os números pares

numeros = [2, 4, 7, 90, 3, 56, 13, 12]

limite = len(numeros)
dobro = []
quadrado = []
pares = []
impares = []
desconto = []

for contador in range(0, limite):
    dobro.append(numeros[contador] * 2)
    quadrado.append(numeros[contador] ** 2)
    if numeros[contador] % 2 == 0:
        pares.append(numeros[contador])
    else:
        impares.append(numeros[contador])
    
    valoresDesconto = numeros[contador]  * 0.98
    desconto.append(f"{valoresDesconto:.2f}")

print(f"Números: {numeros}")
print(f"Dobro: {dobro}")
print(f"Quadrados: {quadrado}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Desconto: {desconto}")