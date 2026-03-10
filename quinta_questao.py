import os

os.system('cls')

(' Solicitando dados -')
Operacao = input('Digite uma operacao (+,-,*,/)')

A = float(input('Digite o primeiro número'))
B = float(input('Digite o segundo número'))

if operacao == '+':
    resultado = A + B
elif subtracao== '-':
    resultado =  A - B
elif multiplicacao == ' * ':
    resultado = A * B
elif  divisao == '/':
    resultado = A / B
else:
    print ('Operação inválida')
    resultado:None
if resultado is not None:
    print('Resultado:', resultado)
