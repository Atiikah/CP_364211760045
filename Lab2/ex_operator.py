# Operators

# Assign operators
x = 100
print(x)
x += 100
print(x)
x -= 50
print(x)
x **= 2
print(x, type(x))

# matimatic operators
x, y = 100 ,200
print('x is',x,'\ny is ', y)
print('sum of x and y is ', x+y)
print('sum of x and y is ', x-y)
z = x-y
print(z, type(z))
print('multiply of x and y is ', x*y)
print('divide of x and y is ', x/y)
print('modulus of x and y is ', x%y)
print('floor division of x and y is ', x//y)
z = x//y
print(z, type(z))

# comparaion operators
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

# logical operators --> and,or,not
x,y =10,20
print(x > 5 and y > 5)
print(x > 5 and y > 5)
z = True
print(z)
print(not z)

# bitwise operators
x = 10
y = 5
print(x & y)
print(x  | y)
print(x ^ y)
print(~x)
print(x << 3)
print(x >> 3)

#identity operators --> is,is,not
x = [1,2,3,4,5]
y = [1,2,3,4,5]
print(x is y)
print(x is not y)
z = x
print(z is x)
print(x[0])
print(z[0])
z[0] = 100
print(x[0])
print(z[0])

a = 10
b = 10
print(a is b)
print(a is not b)


