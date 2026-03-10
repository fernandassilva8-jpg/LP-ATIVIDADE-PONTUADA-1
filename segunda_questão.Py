import os

os.system('cls')

( 'Solicitando dados -')

nome = input('Digite seu nome?')

sexo = input('Qual seu sexo?')

estado_civil = input('Digite seu estado civil?')

tempo_casada = nome

if sexo == 'feminino' and estado_civil == "CASADA":
    tempo_casada = int(input('Quanto tempo de casamento?'))
    print(f'\n --- Dados do úsuario')
    print(f'Nome', {nome})
    print (f'sexo', {sexo})
    print(f'estado_civil', {estado_civil})
