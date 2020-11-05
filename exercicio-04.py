listaNumeros=[]


comparacaoPar=filter(lambda x: x%2==0, listaNumeros)
comparacaoInpar=filter(lambda x: x%2!=0, listaNumeros)

for i in range(10):
    numero=float(input("Insira um numero: "))
    listaNumeros.append(numero)

print("Os numeros pares são ",list(comparacaoPar))
print("Os numeros inpares são ",list(comparacaoInpar))
