def int_to_roman(input):

    #if type(input) != type(1):
    #    raise TypeError, "expected integer, got %s" % type(input)
    #if not 0 < input < 4000:
    #    raise ValueError, "Argument must be between 1 and 3999"   
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL', 'X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(input / ints[i])
        result += nums[i] * count
        input -= ints[i] * count
    return result

print(int_to_roman(19))
