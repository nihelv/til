# e=input()
e='This:-(is str:-(:-(ange te:-)xt.'

a=e.count(':-)')
b=e.count(':-(')

if a == b == 0:
    print('none')
elif a < b:
    print('sad')
elif a == b:
    print('unsure')
else:
    print('happy')