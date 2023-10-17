# 1. Crie um programa que solicite a média 
# e a frequência de um aluno, e determine 
# sua situação. Se a média for maior ou 
# igual a 5 e a frequência for maior ou 
# igual a 75%, o aluno está aprovado. 
# Se a média for menor que 5 e a frequência 
# for menor que 75%, o aluno está reprovado. 
# Em qualquer outro caso, o aluno está de 
# recuperação.

media = float(input("Digite a média do aluno: "))
frequecia = float(input("Digite a frequêcia do aluno: "))

if media >= 5 and frequecia >= 75:
    print ("Aluno aprovado")
elif media < 5 and frequecia < 75:
    print ("Aluno reprovado")
else:
    print ("Aluno em recuperação")