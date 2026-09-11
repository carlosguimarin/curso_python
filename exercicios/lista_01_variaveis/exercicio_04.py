"""
Exercício 4: Análise de Margem de Lucro (Financeiro):
Uma consultoria faturou R$ 15.000,00 em um projeto.
Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%.
Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento).
No final, crie uma variável booleana chamada meta_atingida que verifica
se a margem de lucro é superior a 0.30 (30%).
"""
fat_total = 15000
custos = 5000
imposto = 0.15

lucro = (fat_total - custos) - fat_total * imposto

print(f'Total em impostos: R$ {fat_total * imposto}')
print(f'Lucro líquido: R$ {lucro}')
print(f'Margem de lucro: {(lucro / fat_total):.2f}%')

meta_atingida = lucro / fat_total

if meta_atingida >= 0.30:
    print('Margem de lucro atingida')
else:
    print('A margem de lucro não foi atingida')