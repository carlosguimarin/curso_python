primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor digitado que é igual a ({primeiro_valor}) é maior que o segundo que é igual a ({segundo_valor}).')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor digitado que é igual a ({segundo_valor}) é maior que o primeiro que é igual a ({primeiro_valor}).')
else:
    print('Os dois valores são iguais.')