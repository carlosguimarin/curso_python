"""
Exercício 3: Divisão de Cargas (Logística/Transporte):
Uma transportadora precisa levar 1.250 caixas em caminhões pequenos.
Cada caminhão suporta exatamente 12 caixas.
Quantos caminhões sairão totalmente cheios?
(Use //) e quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %).
"""
totalcaixas = 1250
cadacaminhao = 12

print(f'O número de caminhões necessário para transporte será de {totalcaixas // 12}.')
print(f'E sobraram {totalcaixas % 12} caixas para enviar nas próximas viagens.')