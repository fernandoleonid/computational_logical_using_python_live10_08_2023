# 9. Leia o valor correspondente ao salário mensal 
# (variável SALARIO_MENSAL) de um trabalhador e 
# também o valor do percentual de reajuste 
# (variável PERCENTUAL_REAJUSTE) 
# a ser atribuído. Apresente o valor do novo 
# salário (variável NOVO_SALARIO).

salario_mensal = float(input("Digite o valor do salário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

novo_salario = salario_mensal + (salario_mensal * percentual_reajuste / 100)

print (f"Novo salário: {novo_salario:.2f}")