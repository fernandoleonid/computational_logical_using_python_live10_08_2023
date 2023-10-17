# Listas        -> [ ]
# Dicionários   -> { }

# Fico no Aguardo de dúvidas

produtos = [
    {
        'nome': 'mouse',
        'qtd': 200,
        'preco': 50.00
    }, 
    {
        'nome': 'teclado',
        'qtd': 120,
        'preco': 150.00
    }, 
    {
        'nome': 'monitor',
        'qtd': 50,
        'preco': 1500.99
    }
]

novoProduto = {
    'nome': 'Impressora',
    'qtd': 123,
    'preco': 677.00,
    'tipo': 'colorida'
}
produtos.append(novoProduto)

print ('#### Todos os Elementos ####')
for produto in produtos:
    print (produto)


del produtos[2]

print ('#### Deletando o 3º item####')
for produto in produtos:
    print (produto)

produtos[0]['preco'] = '34.99'

print ('#### Modificando o preço do primeiro produto ####')

for produto in produtos:
    print (produto)

print ('#### Mostrando somente o produto que tiver tipo ####')

for produto in produtos:
    if 'tipo' in produto:
        print (produto)