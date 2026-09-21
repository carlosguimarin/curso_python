"""
Exercício 4: Análise de Metas Combinadas (Setor Comercial):
Uma empresa paga bônus se a meta individual do vendedor e a meta da loja forem batidas.

1. Peça as vendas do vendedor e a meta individual dele.

2. Peça as vendas totais da loja e a meta da loja.

3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre as vendas do vendedor.

4. Caso contrário, o bônus é zero. Exiba a mensagem: “Seu bônus este mês é de: R$[valor]”.
"""

meta_vendedor = input('Digite sua meta: ')
vendas = input ('Digite quanto você vendeu esse mês: ')

meta_loja = input('Digite a meta da loja: ')
fat_loja = input('Digite quanto a loja vendeu esse mês: ')

meta_vendedor_limpo = float(meta_vendedor.replace('R$' ,'').replace(',' ,'.'))
vendas_limpo = float(vendas.replace('R$' ,'').replace(',' ,'.'))

meta_loja_limpo = float(meta_loja.replace('R$' ,'').replace(',' ,'.'))
fat_loja_limpo = float(fat_loja.replace('R$' ,'').replace(',' ,'.'))

if vendas_limpo >= meta_vendedor_limpo and fat_loja_limpo >= meta_loja_limpo:
    print(f'Seu bônus esse mês é de: R$ {vendas_limpo * 0.2:,.2f}'
          .replace(',' ,'X').replace('.' ,',').replace('X' , '.'))
else:
    print('Esse mês as metas não foram cumpridas.')