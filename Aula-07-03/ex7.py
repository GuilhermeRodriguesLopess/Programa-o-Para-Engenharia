print("--------Livraria--------")
quantidade= int(input("Digite a quantidade de cópias: "))
pergunta=input("É livraria?: ")
if pergunta == "sim":
    livro=24.95*(100-35)/100*quantidade+3+0.75*(quantidade-1)
else:
    livro=24.95*quantidade+3+0.75*(quantidade-1)
print(f"Valor dos livros:{livro:.2f}")