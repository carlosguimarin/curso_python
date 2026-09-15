"""
Exercício 3: Análise de Metas de Vendas (Setor Comercial):
Um gerente quer comparar o desempenho de duas filiais.

O programa deve:
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar números decimais).

2. Calcular o faturamento total das duas lojas.

3. Calcular a média de faturamento entre elas.

4. Exibir uma única mensagem formatada informando o total e a média,
utilizando o separador de milhar e duas casas decimais.
"""

fat_loja_a = float(input('Digite o faturamento da Loja A: ').replace(',', '.'))
fat_loja_b = float(input('Digite o faturamento da Loja B: ').replace(',', '.'))

fat_total = fat_loja_a + fat_loja_b
fat_médio = fat_total / 2

print(f'O faturamento total das duas lojas é de R$ {fat_total:,.2f}'
      f' e a média de faturamento é igual a R$ {fat_médio:,.2f}'.replace(',', 'X').replace('X', '.'))