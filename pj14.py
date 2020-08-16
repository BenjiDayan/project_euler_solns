#pj14
import mathStuff

biggest_length = 1
biggest_num = 1
for num in range(1, 1000000):
    if num % 50000 == 0:
        print(num, end=', ')
    length = len(mathStuff.collatz_sequence(num))
    if length > biggest_length:
        biggest_length = length
        biggest_num = num
print('')
print("biggest length: " + str(biggest_length))
print("biggest num: " + str(biggest_num))
