# list comprehension

fruit = ['apple ', 'banana','cherry','pineapple','orange']

# without comprehension
newlist = []
for x in fruit:
    if 'a' in x:
        newlist.append(x)

print('Data in newlist: \n',newlist)

# using comprehension
newlist = [x for x in fruit if 'a' in x]
print('Data in newlist(comprehension):\n',newlist)

num = [23,54,67,34,89,90,11]
# คัดกรองข้อมูลใน num โดยเลือกเฉพาะข้อมูลที่มีค่าน้อยกว่า 50
newlist = [x for x in num if  x <50]
print (newlist)
newlist = [x for x in num if x>30 and x<90]
print (newlist)

# sort data in list
# sort()
# low to high
num.sort()
print(num)
# high to low
num.sort(reverse=True)
print(num)

mylist = ['apple','cherry','banana','Mango']
mylist.sort()
print(mylist)
mylist.sort(key = str.lower)
print(mylist)
