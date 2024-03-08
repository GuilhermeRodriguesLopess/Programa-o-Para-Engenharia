nome=input("Digite seu nome: ")
cidade=input("Digite sua cidade: ")
estado=input("Digite seu estado: ")
datanasc=input("Digite sua data de nascimento: ")
#"F" para chamar a biblioteca F strings 2
print(f"Meu nome é {nome} nasci na cidade {cidade}, {estado}, eu nasci: {datanasc}")
#ou
print("Meu nome é %s nasci na cidade %s, %s, eu nasci: %s"% (nome,cidade,estado,datanasc))