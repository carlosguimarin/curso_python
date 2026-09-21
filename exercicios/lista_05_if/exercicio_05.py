"""
Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience):
Crie um sistema que ajude a filtrar para qual departamento uma reclamação deve ir.
O usuário deve digitar o assunto do e-mail.

Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado para o Financeiro".
Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a Logística".
Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral".
Dica: Use o operador in para verificar se a palavra está dentro do texto.
"""

financeiro = ['pagamento','boleto']
logistica = ['entrega','atraso']

reclamacao = input('Digite aqui sua reclamação: ')
reclamacao_padrao = reclamacao.lower()

if any(palavra in reclamacao_padrao for palavra in financeiro):
    print(f'Encaminhado para o Financeiro')
elif any(palavra in reclamacao_padrao for palavra in logistica):
    print(f'Encaminhado para a Logística')
else:
    print(f'Encaminhado para o Suporte Geral')