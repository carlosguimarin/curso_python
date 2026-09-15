"""

Exercício 5: Atualização de Preços Interativa (Input + Lista):
Você tem uma lista de preços de produtos:

precos = [100.0, 250.0, 500.0]

Além disso, temos uma lista com os nomes:

vinhos = [“Branco”, “Tinto”, “Champagne”]. Crie um programa interativo que:

1. Peça para o usuário digitar qual o nome do produto.

2. Peça para o usuário digitar o novo preço.

3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços.
"""

precos = [100.0, 250.0, 500.0]
vinhos = ['Branco', 'Tinto', 'Champagne']

nome = input('Digite o nome do produto: ')
novo_preco = float(input('Digite o novo preço: '))

posicao = vinhos.index(nome)
precos[posicao] = novo_preco

print(vinhos)
print(precos)