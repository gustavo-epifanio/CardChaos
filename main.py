element1 = 'Ice'
element2 = 'Fire'
value1 = 7
value2 = 8
if element1 == 'Fire' and element2 == 'Ice':
    print('First Player Win!')
elif element1 == 'Fire' and element2 == 'Water':
    print('Second Player Win!')
elif element1 == 'Ice' and element2 == 'Water':
    print('First Player Win!')
elif element1 == 'Ice' and element2 == 'Fire':
    print('Second Player Win!')
elif element1 == 'Water' and element2 == 'Fire':
    print('First Player Win!')
elif element1 == 'Water' and element2 == 'Ice':
    print('Second Player Win!')
elif element1 == element2:
    if value1 > value2:
        print('Fist Player Win!')
    elif value1 < value2:
        print('Second Player Win!')
