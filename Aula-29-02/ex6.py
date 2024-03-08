vf = float(input ("Digite o valor final que deseja com seus investimentos: "))
n = float(input ("Digite o numero de meses que deseja deixar: "))
i = float(input ("Digite o a porcentagem da rentabilidade: "))/ 100 
vi =  vf/(1+i)**n
print ("Valor do investimento inicial: ",vi)
