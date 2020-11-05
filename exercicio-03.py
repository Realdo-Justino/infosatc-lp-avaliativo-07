listaNumeros=[]


comparacao=filter(lambda x: 10 < x, listaNumeros)

for i in range(10):
    numero=float(input("Insira um numero: "))
    listaNumeros.append(numero)
print("Os numeros maiores que 10 são: ",list(comparacao))

