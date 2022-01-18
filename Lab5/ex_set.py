# set

myset = {'apple','banana','cherry'}
print(myset)
print(type(myset))
print(len(myset))
print(f'Lenght of myset is {len(myset)}')

# access data in set
# for
for x in myset:
    print(x)
# keyword in --> True, False
print('apple' in myset)
print('Apple' in myset)

myset2 = {10,'1',20,True,100,'abc'}
print(myset2)

# add data to set
# add()
myset.add('mango')
print(myset)

# updata()
myset3 = {'orange','grap'}
myset.update(myset3)
print(myset)

myset.add('mango')
print(myset)

mylist = ['pineapple','apple']
myset.update(mylist)
print(myset)

# delete data in set
# remove ()
myset.remove('apple')
print(myset)
myset.remove('pineapple')
print(myset)
#discad()
myset.add('mango')
print(myset)

if 'apple'in myset:
    myset.discad('apple')
else:
    print('Set have no data apple')
print(myset)


#pop ()
d = myset.pop()
print(d)
print(myset)
d = myset.pop()
print(d)
print(myset)


#keyword del
del myset3
#print(myset3)