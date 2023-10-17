import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return data
        else:
            return {'erro': 'CEP não encontrado'}
    else:
        return {'erro': 'Erro na solicitação!12'}
        
cep = input('Digite um cep para a pesquisa: ')
info = consultar_cep(cep)

if 'erro' in info:
    print (info['erro'])
else:
    print ('######################')
    print (f'CEP: {info["cep"]}')
    print (f'Logradouro: {info["logradouro"]}')
    print (f'Bairro: {info["bairro"]}')
    print (f'Cidade: {info["localidade"]}')
    print (f'Estado: {info["uf"]}')

    # Aguardando dúvidas!!!!