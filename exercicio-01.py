a=""
b=0
nome=str(input("Insira seu nome: "))
idade=int(input("Insira sua idade: "))

frase= lambda nome, idade: print(nome, "possui",idade,"anos.")

print(frase(nome,idade))