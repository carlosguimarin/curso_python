"""
Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos):
Um contrato de manutenção de software tem a duração de 40 meses.
O cliente quer ver esse tempo no formato: “X anos e Y meses”.
Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.
"""

manutencao = 40

ano = 40 // 12
mes = 40 % 12


print(f'O contrato de duração terá {ano} anos e {mes} meses.')