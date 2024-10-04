my_dict={'Cocaine':[10000, 150000], 'Weed':1200, 'Lirica':300}
print(my_dict)
my_dict['Cocaine']=12500
print(my_dict['Cocaine'],['Girl'])
del my_dict['Lirica']
print(my_dict)
my_dict.update({'TT':15000, 'Human':45000})
print(my_dict)
print(my_dict.get('TT'))
print(my_dict.get('Mef'))
print(my_dict.get('Mef', 'не найдено'))
print(my_dict)
a=my_dict.pop('TT')
print(my_dict)
print(a)
list_=[1,2,3,4]
list_.pop(0)
print(list_)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


set_={1,2,3,2,1,4,5,6,5,4,5,2}
print(set_)
set_={1,2,3,2,1,4,5,6,5,4,5,2, True, 'string',(1,2,3)}
print(set_)
list_=[1,1,1,1,2,4,2,2]
print(list_)
list_=set(list_)
#print(list_.discard(1))
print(list_.remove(1))
print(list_)
print(list_.add(5))
print(list_)



my_dict={'Cocaine':[10000, 150000], 'Weed':1200, 'Lirica':300}
print(my_dict)
my_dict['Cocaine']=12500
print(my_dict['Cocaine'],['Girl'])
del my_dict['Lirica']
print(my_dict)
my_dict.update({'TT':15000, 'Human':45000})
print(my_dict)
a=my_dict.pop('TT')
print(a)
print(my_dict)

my_set={1,True,'String',7,7,1,True,True,'String'}
print(my_set)
my_set.add(9)
my_set.add(8)
print(my_set)
my_set.remove(1)
print(my_set)