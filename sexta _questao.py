import os

os.system('cls')
# Leitura das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Exibição da média
print("Média:", media)

# Verificação da situação do aluno
if media >= 6.0:
    print("Parabéns! Você está aprovado.")
elif media >= 4.0:
    print("Você está em recuperação.")
else:
    print("Você está reprovado.")