calculo=lambda x,y: (x+y)/2
funcoes = [
    lambda x: x<5,
    lambda x: x<7,
]

def comparacao(nota):
    if(nota<5):
        return "D"
    elif(nota<7):
        return "C"
    elif(nota<9):
        return "B"
    else:
        return "A"

nota1=float(input("Insira a sua primeira nota: "))
nota2=float(input("Insira a sua segunda nota: "))
media=calculo(nota1,nota2)
conceito=comparacao(media)

print("\n A media é ",media," e o conceito é ",conceito)
