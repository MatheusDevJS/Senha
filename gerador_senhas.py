import random

print('Seja Bem-vindo ao Gerador de Senhas')

carcter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY!@#$%¨&*().;?/[]0123456789'

            #Quantas senhas queremos criar
number = input('Quantidade de senhas a serem geradas: ')
number = int(number)

            #Comprimento da senha
lenght = input('Comprimento da senha: ')
lenght = int(lenght)

print('\nSua senha é: ')

for pwd in range(number):
    passoword = ''
    for c in range(lenght):
        passoword += random.choice(carcter)

    print(passoword)