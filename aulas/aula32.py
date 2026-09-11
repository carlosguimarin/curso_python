"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    if int(numero) % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
else:
    print('Não é um número inteiro.')

# numero = input('Digite um número inteiro: ')

# if int(numero) % 2 == 0:
#     print('O número é par.')
# elif int(numero) % 2 != 0:
#     print('O número é ímpar.')
# else:
#     print('Não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora atual (0-23): ')

if int(hora) >= 0 and int(hora) <= 11:
    print('Bom dia!')
elif int(hora) <= 12 and int(hora) >= 17:
    print('Boa tarde!')
elif int(hora) >= 18 and int(hora) <= 23:
    print('Boa noite!')
else:
    print('Não conheço essa hora!')


"""
Faca um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')

if 1 >= len(nome) <= 4:
    print('Seu nome é curto.')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal.')
elif len(nome) > 6:
    print('Seu nome é muito grande.')
else:
    print('Você não digitou seu nome.')