a = 'AAAAA'
b = 'BBBBB'
c = 1.1

string = 'a={} b={} c={:.2f}'
format = string.format(a, b, c)

print(format)

string = 'a={name1} b={name2} c={name3:.2f}'
format = string.format(
    name1=a, name2=b, name3=c
)

print(format)