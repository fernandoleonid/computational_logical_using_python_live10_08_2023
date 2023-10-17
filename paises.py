import requests

def consultar_info_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"
    
    response = requests.get(url)
    if response.status_code == 200:
        dados_pais = response.json()
        return dados_pais[0]
    else:
        return {"erro": "País não encontrado"}
    


pais = input('Digite um nome de Pais: ')
informacoes_pais = consultar_info_pais(pais)

if 'erro' in informacoes_pais:
    print(informacoes_pais['erro'])
else:
    print("Nome do País:", informacoes_pais['name']['common'])
    print(f'Capital: {informacoes_pais["capital"][0]}' )
    print("Bandeira:", informacoes_pais['flags']['png'])
    print("População:", informacoes_pais['population'])
    print("Moeda:", informacoes_pais['currencies']['BRL']['name'])
    print("Idioma:", informacoes_pais['languages']['por'])
