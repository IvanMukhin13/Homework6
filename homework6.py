my_dict = {'Ivan': 1990,
           'Anna': 1969,
           'Tamara': 1948}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Pedro'))
my_dict.update({'Valery': 1939,
                "Alexandr" : 2020})
print(my_dict['Tamara'])
del my_dict['Tamara']
print(my_dict)


my_set ={1,1,1,2,2,3.2,3.2,'Ivan','Ivan'}
print(my_set)
my_set.update({44,55})
my_set.discard(2)
print(my_set)

