"""
Exercício 1: Relatório de Margem de Lucro (Setor Financeiro):
Uma empresa de varejo precisa de um resumo rápido sobre a performance de um produto.
Dado o faturamento de R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa
que calcule o lucro e a margem de lucro (lucro dividido pelo faturamento).
Exiba uma mensagem formatada onde o lucro use o separador de milhar e duas casas decimais,
e a margem seja exibida como uma porcentagem inteira.
"""

fat_total = 45000
custo = 23500

lucro = fat_total - custo
margem_lucro = lucro / fat_total
porcentagem = margem_lucro * 100

print(f'O lucro obtido para este produto foi de R$ {lucro:,.2f} e a margem de lucro foi de {porcentagem:.0f}%,'
      .replace(',', 'X').replace('.', ',').replace('X', '.'))