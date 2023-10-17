# Crie uma função que de as boas vindas
# a um usuário que digitou seu nome

nome_digitado = input("Digite seu nome: ")

def cumprimentar (nome):
    return f"Olá, {nome}!"

mensagem = cumprimentar(nome_digitado)

print (mensagem)