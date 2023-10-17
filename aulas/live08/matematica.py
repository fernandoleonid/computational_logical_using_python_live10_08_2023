def soma(n1, n2):
    r = n1  + n2
    return f"{n1} + {n2} = {r}"

def subtracao(n1, n2):
    r = n1 - n2
    return f"{n1} - {n2} = {r}"

def multiplicacao(n1, n2):
    r = n1 * n2
    return f"{n1} * {n2} = {r}"

def divisao(n1, n2):
    if n2 == 0:
        return "Não existe divisão por zero"
    r = n1 / n2
    return f"{n1} / {n2} = {r}"

def exponenciacao(n1, n2):
    r = n1 ** n2
    return f"{n1} ** {n2} = {r}"