#pj17
ones = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tenties = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
ten_to_str = {3:'thousand', 6:'million', 9:'billion'}

def int_to_str(num):
    """takes num e.g. 123 and outputs 'one hundred and twenty three'"""

    b = strip(num)
    
    c = []
    length = len(b)
    count = length-1
    temp = 0
    while count >= 0:
        if temp == 3:
            temp = 0
        if temp == 0:
            c.append([])
        c[-1].append(b[count])
        temp += 1
        count -= 1
    c.reverse()
    for thing in c:
        thing.reverse()


    numString = ''
    for thing in c:
        power = thing[-1][-1]
        num = int(''.join([str(pair[0]) for pair in thing]))
        powerString = ' ' + ten_to_str[power] + ' ' if power != 0 else ''
        if power == 0 and num < 100 and num != 0:
            numString += 'and '
        numString += int_to_num_below_100(num) +  powerString

    return(numString)

def strip(num):
    """ takes num e.g. 456 and outputs [[4, 2], [5, 1], [6, 0]]"""
    a = str(num)
    b = []
    length = len(a)-1
    for char in a:
        b.append([int(char), length])
        length -= 1
    return(b)

def int_to_num_below_100(num):
    b = strip(num)
    comp = ''
    count = 0
    length = len(b)
    #True if there was stuff before - then next thing will add ' '
    stuffLatch = False
    #True if there is hundreds to deal with - then if stuff in tens or ones will add 'and'
    andLatch = False
    #True if there is teens to deal with - then ones ignored
    teenLatch = False
    #True if no hundreds or tens - then zero can be put in
    zeroLatch = False
    twoLatch = False

    if length == 3:
        #If the hundred's isn't 0, so it is actually a number ish.
        if b[count][0] != 0:
            #some number of hundreds
            comp += ones[b[count][0]-1] + ' ' + 'hundred'
            #There will need to be an and
            stuffLatch = True
            andLatch = True
        count += 1
        stuffLatch = True

    if length >= 2:
        temp = len(comp)

        #If there's stuff in 2, and stuff in 3, add ' and'
        if b[count][0] != 0:
            twoLatch = True
            if andLatch:
                comp += ' and '
                andLatch = False
            else:
                #So that step 3 (1) knows that stuff's happened
                stuffLatch = True

        if b[count][0] == 1:
            #So that step 3 (1) knows not to do anything
            teenLatch = True
            comp += teens[b[count+1][0]]
        elif b[count][0] != 0:
            #If not teen and not 0, add on twenty/thirty/...
            comp += tenties[b[count][0]-2]

        count += 1

    if length >= 1:
        if b[count][0] != 0:
            #If and needs to be said, say ' and'
            if andLatch:
                comp += ' and '

        if zeroLatch:
            #aka if the one digit is zero and there's been nothing before, add zero
            comp += 'zero'

        if not teenLatch and b[count][0] != 0:
            if twoLatch:
                comp += '-'
            #if wasn't a teen and stuff
            comp += ones[b[count][0]-1]

    return(comp)

def letter_length(end, start=1):
    """calculates number of letters from start to end inclusive"""
    comp = 0
    for num in range(start, end+1):
        temp = int_to_str(num)
        for char in temp:
            if char != ' ' and char != '-':
                comp += 1
    return(comp)
                          
            
    
                
