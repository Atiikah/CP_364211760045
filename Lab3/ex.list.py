# List

# List vs variable
x = 100
print(x)
x = 200
print(x)

mylist = []
print(mylist)
print(type(mylist))

mylist = ['apple ', 'banana','cherry']
print(mylist)

# accessing list data
print(mylist[0])
print(mylist[1])
print(mylist[2])

# accessing list data - negative index
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])

# accessing list data - range index
mylist = ['apple ', 'banana','cherry','pineapple','orange']
print(len(mylist))

print(mylist[2:4])
print(mylist[2:5])
# พิมพ์ข้อมูลตำแหน่ง 1-3 ใน mylist
print(mylist[1:4])
# พิมพ์ข้อมูลตำแหน่ง 1 ถึงตำแหน่งสุดท้าย
print(mylist[1:])
# พิมพ์ข้อมูลตำแหน่ง 3 ถึงตำแหน่งแรก
print(mylist[:4])

# accessing list data - loop
# for
print('Display with for loop:')
for x in mylist :
    print(x, type(x))
# while
i = 0
while i < len(mylist):
    print(mylist[i],type(mylist[i]))
    i+= 1

# changing data in list
mynum = [10,20,30,100,200,300]
print(mynum)
mynum[0] = 1000
print(mynum)
mynum[-1] = 3000
print(mynum)

# add data into list
mynum.append(4000)
print(mynum)

#insert data to list
#แทรกข้อมูล 500 ที่ตำแหน่งที่1 ของ mynum
mynum.insert(1,500)
print(mynum)

mynum[1:3] =[600,700]
print(mynum)

mynum[1:2] = [5,6]
print(mynum)

mynum[:5] = [10]
print(mynum)

# delate data in list
# remove()
mynum.remove(4000)
print(mynum)
# pop()
mynum.pop(0)
print(mynum)
mynum.pop()
print(mynum)
# key del
del mynum[1]
print(mynum)
del mynum
# print(mynum)

mynum = [1,2,3,4,5]
print(mynum)
mynum.clear()
print(mynum)

