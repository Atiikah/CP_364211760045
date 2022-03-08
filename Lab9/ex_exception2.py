# Input Exceptoin

# try:
#     num = int(input('Enter an integer.'))
#     print(f'The number that you entered is: {num}')
# except Exception as e:
#     print(e)

num = input('Enter an integer.') # string
if not type(num) is int: # num is not integer
    raise Exception('Only integer are allowed')

try:
    #something_went_wrong() # an error
    pass
except TypeError as e:
    print(e.args)

print(f'The number that you entered is: {num}')