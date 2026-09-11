"""
Exercício 2: Controle de Estoque de E-commerce (Logística): 
Um e-commerce começou o dia com 250 unidades de um smartphone no estoque.
Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor.
Atualize a variável de estoque e exiba o saldo final.
"""

unidadestotais = 250
numvendas = 78
novasuni = 100

print(f'Estoque total no momento: {(unidadestotais - numvendas) + novasuni}')