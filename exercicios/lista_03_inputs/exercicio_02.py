"""
Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH):
Ao cadastrar um novo funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o e-mail.

Crie um programa que:
1. Peça o nome completo do colaborador.

2. Peça o e-mail pessoal do colaborador.

3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).

4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).

5. Exiba a mensagem: “Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]”.
"""

nome = input('Digite seu nome completo: ')
email_pessoal = input('Digite seu email pessoal: ')

primeiro_espaco = nome.find(' ')
primeiro_nome = nome[:primeiro_espaco].title()
email_pessoal = email_pessoal.strip().lower()

print(f'Cadastro concluído: {primeiro_nome}. E-mail de acesso: {email_pessoal}')