#pj17v2
import math

powers_of_thousand = {0:'', 1:'thousand', 2:'million', 3:'billion', \
                      4:'quadrillion', 5:'quintillion', 6:'sextillion'}


digits = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', \
          7:'seven', 8:'eight', 9:'nine'}

teens = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', \
         16: 'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

tens = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', \
        7:'seventy', 8:'eighty', 9:'ninety'}

hundred = 'hundred'

def int_to_words(num):
    """
    takes num e.g. 1234 and outputs
    "one thousand two hundred and thirty-four"
    """

    # num = 1234007, a will subsequently contain
    # [['1', 2], ['234', 1], ['007', 0]
    a = divide_up(num)
    length_a = len(a)
    for num in range(length_a):
        a[num] = [a[num], length_a-1-num]


    
    comp = [less_than_thousand_to_words(x[0]) + ' ' + powers_of_thousand[x[1]] \
            for x in a]

    # the statement above adds an unwantd ' ' at the end of the last thing in comp
    comp[-1] = comp[-1][:-1]


    # removes stuff in comp if they are zero
    num = 0
    while(True):
        if num == len(comp):
            break
        if comp[num] == 'zero':
            del(comp[num])
            num -= 1
        num += 1
    if comp == []:
        comp.append('zero')
        

    # if there needs to be an extra 'and' added to the beginning of the last
    # element of comp
    if  0 < int(a[-1][0]) <= 99 and length_a >= 2:
        comp[-1] = 'and ' + comp[-1]
    return(' '.join(comp))
        
    
    
def less_than_thousand_to_words(num):
    """
    takes in num (a str) between 0 and 999 inclusive e.g. 545 and outputs
    "five hundred and forty-five"
    """

    #This little chunk strips leading zeroes off of num
    temp = ''
    triggered = False
    for char in num:
        if not char == '0':
            triggered = True
        if triggered:
            temp += char
    num = temp
   
    if len(num) == 1:
        return(digits[int(num)])

    if num == '':
        return('zero')
    
    else:
        # if num is two or three characters long, take the last two characters
        # corresponding to 10-99 and deal with them separately
        last_two = num[-2:]
        # two_out is the output for last_two
        two_out = ''
        three_out = ''
        comp = ''

        # if last_two is of form 0x
        if last_two[0] == '0':
            if last_two[1] == '0':
                pass
            else:
                two_out = digits[int(last_two[1])]
            

        
        # if last_two is 10-19
        elif last_two[0] == '1':
            if last_two[1] == '0':
                two_out = tens[1]
            else:
                two_out = teens[int(last_two)]

        # if last_two is 20-99
        else:
            # add the tens value to two_out
            two_out += tens[int(last_two[0])]

            if last_two[1] != '0':
                two_out += '-' + digits[int(last_two[1])]

        # if there is a hundred digit as well:
        if len(num) == 3:
            three_out = digits[int(num[0])] + ' hundred'

        comp += three_out
        if (not three_out == '') and not two_out == '':
            comp += ' and '
        comp += two_out
        return(comp)
        
                

    
    
    

def divide_up(num):
    """
    takes num (int) e.g. 1234567 and outputs [1, 234, 567]
    """
    num_str = '{:,d}'.format(num)
    return(num_str.split(','))    
