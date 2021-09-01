notas = []
num_notas = int(input("Quantas notas você quer tirar a média: "))
for i in range(num_notas):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    
media = sum(notas) / num_notas
print("A média é: %.1f" %media)
