"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, boo
"""

string = 'luiz otavio'
# string[3] = 'ABC' # TypeError: 'str' object does not support item assignment
# print(string[3])

outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.capitalize())
print(string.zfill(10))
