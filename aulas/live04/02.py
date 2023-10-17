# Crie uma lista chamada nomes com 
# três nomes de pessoas. 
# Adicione mais três nomes a essa
# lista e, em seguida, substitua o 
# segundo nome pelo seu próprio nome. 
# Imprima os resultados.

nomes = ['Ana','Carlos', 'Hugo']
print (f"Chamada Original: {nomes}")

nomes.append('Gabriela')
nomes.append('Marta')
nomes.append('Suzane')
print (f"Chamda mais 3: {nomes}")

nomes[1] = 'Fernando'
print (f"Chamda substituida: {nomes}")
