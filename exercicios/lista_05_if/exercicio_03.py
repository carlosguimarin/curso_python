"""
Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas):
Um e-commerce aplica descontos automáticos no carrinho.
Crie um programa que receba o valor total da compra e aplique a seguinte lógica:

Compras a partir de R$ 500,00: 15% de desconto.
Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
Compras abaixo de R$ 200,00: Sem desconto.
O programa deve exibir o valor do desconto e o valor final a pagar, formatados em R$.
"""

valor_compra = input('Digite o valor total da compra: ')

valor_limpo = float(valor_compra.replace('R$' ,'').replace('.', '').replace(',', '.'))

if valor_limpo > 500:
    print(f'O desconto ficou de R$ {(valor_limpo * 0.15):,.2f} e o total ficou R$ {(valor_limpo * 0.85):,.2f}'
          .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))
elif 200 <= valor_limpo <= 500:
    print(f'O desconto ficou de R$ {(valor_limpo * 0.10):,.2f} e o total ficou R$ {(valor_limpo * 0.90):,.2f}'
          .replace(',' ,'X').replace('.' ,',').replace('X' ,'.'))
else:
    print(f'Compra sem desconto!')