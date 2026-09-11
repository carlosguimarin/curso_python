# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)  # 2 - int
print('1' + '1')  # 11 - str
print('a' + 'b')  # ab - str
print(int('1'), type(int('1')))  # 1 - int
print(float('1') + 1) # 2.0 - float
print(bool(''))  # False - bool
print(bool(' '))  # True - bool
print(str(11) + 'b')  # 11b - str
print(11 + 'b')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'