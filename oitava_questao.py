import os

os.system('cls')
#ENTRADA DE COR

cor = input('Digite a cor do CD:').lowe()

#Verificaçao de preços 
if cor == 'verde':
    preco = 10.00
elif cor == 'azul':
    preco = 20.00
elif cor == 'amarelo':
    preco = 30.00
elif cor == 'vermelho':
    preco = 40.00
else:
    preco =  None
#Saída 
if preco is not None:
    print(f'O preço do CD é: R$ {preco:2f}')
else:
    print('Cor inválida')