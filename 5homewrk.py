immutable_var=(1, 2, 3, 'kukushka')
print(immutable_var)

#immutable_var=(1, 2, 3, 'kukushka')
#immutable_var[0]=2
#print(immutable_var)

immutable_var=([1, 2, 3], 'kukushka')
print(immutable_var)
immutable_var[0][0]=4
print(immutable_var)

mutable_list=[1,2,3,'kukushka']
print(mutable_list)
mutable_list[1]='z'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
#mutable_list.extend('string')
#print(mutable_list)
mutable_list.extend(['string', 2, 3])
print(mutable_list)
