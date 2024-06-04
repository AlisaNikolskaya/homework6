#Работа со словарями
my_dict = {'Natalia': 1999, 'Alex': 1985, 'Petr': 1971}
print(my_dict)
print('Existing value:', my_dict.get('Alex'))
print('Not existing value:', my_dict.get('Vitaly'))
my_dict.update({'Tatiana': 1969, 'Avdotia': 2010})
a = my_dict.pop('Natalia')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

#Работа с множествами:
my_set_ = {5, 5, 5, 1, 1, 2, 'one', (1, 2, 3)}
print('Set:', my_set_)
my_set_.add(3)
my_set_.add(4)
my_set_.discard('one')
print('Modified set:', my_set_)
