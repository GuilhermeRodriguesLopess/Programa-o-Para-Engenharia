nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3)/3
if media >= 6:
    print("O aluno ",nome," esta aprovado, com a média: ",media)
else:
    print("O aluno ",nome," esta reprovado, com a média: ",media)
    
