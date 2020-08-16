print('hi')

def list2str(nums):
    return(''.join([chr(x).lower() for x in nums]))
    
def is_english(text):
    letters = {}
    for char in text:
        try:
            letters[char] += 1
        except KeyError:
            letters[char] = 1
    
    
    listver = [[key, letters[key]] for key in letters]
    listver.sort(key=lambda x: x[1])
    return(listver[-1])
    

for num1 in range(256):
    