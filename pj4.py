#pj4

from pj_euler import mathStuff
print('hi')
for num in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        if mathStuff.is_palindrome(num*num2):
            print(num*num2)
            exit()
