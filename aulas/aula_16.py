# if / elif / else

# Quero que as sugestões sejam em inglês, pois o código quero treinar já digitando tudo em inglês.

entry = input('Do you want to enter or exit the system? ')

if entry == 'enter' or entry == 'Enter':
    print('You have entered the system')
elif entry == 'exit' or entry == 'Exit':
    print('You have left the system')
else:
    print('Invalid option')