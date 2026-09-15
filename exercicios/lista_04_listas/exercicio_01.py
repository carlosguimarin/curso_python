"""
Exercício 1: Dashboard de Vendas (Análise de Dados):
Você recebeu uma lista com as vendas diárias de uma equipe:

vendas = [1500, 2000, 800, 3500, 1200].

Crie um programa que exiba um pequeno relatório contendo:

1. O total de vendas na semana.

2. A média de vendas diária.

3. O valor da melhor venda e da pior venda do período.
"""

vendas_seg = float(input('Digite o faturamento de segunda-feira: '))
vendas_ter = float(input('Digite o faturamento de terça-feira: '))
vendas_qua = float(input('Digite o faturamento de quarta-feira: '))
vendas_qui = float(input('Digite o faturamento de quinta-feira: '))
vendas_sex = float(input('Digite o faturamento de sexta-feira: '))

vendas = [vendas_seg, vendas_ter, vendas_qua, vendas_qui, vendas_sex]

total_semana = vendas_seg + vendas_ter + vendas_qua + vendas_qui + vendas_sex
media_semana = total_semana / 5

print(f'Total de vendas semanal: R$ {total_semana:,.2f}'
      .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))

print(f'Média semanal: R$ {media_semana:,.2f}'
      .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))

print(f'Melhor dia da semana: R$ {max(vendas):,.2f}'
      .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))
print(f'Pior dia da semana: R$ {min(vendas):,.2f}'
      .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))