
nota1 = float(input("qual sua primeira nota? "))
nota2 = float(input("qual sua segunda nota? "))
nota3 = float(input("qual sua terceira nota? "))
media = (nota1+nota2+nota3)/3
if media >= 6:
    print("você está aprovado", ", sua média foi", media)
else:
    print("você está em recuperação", ", sua média foi", media)
