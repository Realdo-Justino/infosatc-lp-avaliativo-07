numero=float(input("Insira um número: "))

funcoes = [
    lambda x: x **2,
    lambda x: x **3,
]
for i in funcoes:
    print(i(numero))