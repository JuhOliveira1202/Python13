#Exercício 16:
#Faça um programa que recebe a idade de 15 pessoas e que
#no final mostre a distribuição conforme a sua faixa etária
# 1º até 15 anos;
# 2º de 16 a 30 anos;
# 3º de 31 a 45 anos;
# 4º de 46 a 60 anos;
# 5º acima de 61 anos;


contador15=0
contador30=0
contador45=0
contador60=0
contador61=0

for contador in range(0,15,+1):
    idade=int (input("introduza a idade"))
    while idade<0:
        idade=int(input("introduza a idade"))

    if idade>=0 and idade<=15:
        contador15+=1

    elif idade<=30:
        contador30+=1

    elif idade<=45:
        contador45+=1

    elif idade<=60:
        contador60+=1

    else:
        contador61 +=1

print(" Até 15 anos - ", contador15, "\n De 16 a 30 anos - ", contador30, "\n De 31 a 45 anos - ", contador45, "\n De 46 a 60 anos - ", contador60, "\n Acima de 61 anos - ", contador61) 


