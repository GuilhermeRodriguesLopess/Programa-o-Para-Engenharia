pv = float(input ("Digite o valor do investimento: "))
n = float(input ("Digite o numero de meses do investimento: "))
i = float(input ("Digite o a porcentagem da rentabilidade: "))/100
valor =  pv*(1+i)**n
#somente dois numeros após a virgula
print (f"Valor do investimento:{valor:.2f}")
