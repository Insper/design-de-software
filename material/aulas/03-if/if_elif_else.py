numero = int(input('Digite um número: '))

if numero == 0:
    print('0 não é nem par, nem ímpar')
elif numero % 2 == 0:  # Resto da divisão de número por 2
    print('{0} é par'.format(numero))
else:
    print('{0} é ímpar'.format(numero))
