# Esse script calcula a porcentagem de um dado número real.

numero = float(input("Digite o número: "))
porcentagem = float(input("Digite a porcentagem: "))
p = (numero / 100) * porcentagem
print(f"{porcentagem:.2f}% de {numero:.2f} = {p:.2f}")
