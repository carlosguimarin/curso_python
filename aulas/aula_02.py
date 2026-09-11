print(12, 34)
print(56, 78)
print(12, 34, sep="-")
print(56, 78 , sep='-')
# \r\n -> CRLF que aparece no Windows, canto inferior direito do VSCode, no canto inferior esquerdo aparece o tipo de quebra de linha que está sendo usada no arquivo.
# \n -> LF que aparece no Linux e no Mac, canto inferior direito do VSCode, no canto inferior esquerdo aparece o tipo de quebra de linha que está sendo usada no arquivo.

print(12, 34, sep="-", end='#')
print(56, 78, sep="-", end='\n')
print(12, 34, sep="-", end='\n')

