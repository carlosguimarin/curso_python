# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'João da Silva'  # str
soma_dois_mais_dois = 2 + 2  # int
print(nome_completo, soma_dois_mais_dois) # João da Silva 4

int_um = int('1')  # int
float_um = float('1')  # float
print(int('1'), type(int('1')))  # 1 - int
print(float('1'), type(float('1')))  # 1.0 - float
print(int_um, type(int_um))  # 1 - int
print(float_um, type(float_um))  # 1.0 - float

nome = 'João da Silva'  # str
idade = 30  # int
maior_de_idade = idade >= 18  # bool
print('Nome:', nome)  # Nome: João da Silva
print('Idade:', idade)  # Idade: 30
print('É maior de idade?', maior_de_idade)  # É maior de idade? True