import os

os.system('cls')


nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))


total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05


total_pagar = total - desconto

print("\nProduto:", nome)
print("Total da compra: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_pagar)