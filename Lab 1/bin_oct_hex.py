# function name: to_decimal
# input: num (a non-negative non-decimal int as string)- ex: 11101, 7712, ABC
# base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: decimal representation of num AS INTEGER
# restrictions: you are NOT allowed to use the Python int function
# that will convert it to decimal for you. You should use
# implement the algorithm discussed in class
# assumptions: num will always be non-negative
#  num will always be a valid number ex: 31112 (base2) won't be an input
# . if num has letters, they will always be capitalized
#  base will be 2, 8, or 16
def to_decimal(num: str, base: int) -> int:
    output = 0
    for i in range(len(num)):
        temp = ord(num[i].upper()) - \
                   55 if base == 16 and ord(
                       num[i].upper()) >= 65 else int(num[i])
        output += temp * pow(base, len(num) - 1 - i)
    return output


# funtion name: to_base
# input: dec_num (a positive decimal integer)- ex: 1, 6, 10, 68, 102...
# base (the number system you're converting to as an int)- ex: 2, 8, 16
# output: non-base-10 representation of dec_num AS STR
# restrictions: you are NOT allowed to use the Python int function
# that will convert it for you. You should use
# implement the algorithm discussed in class
# assumptions: dec_num will always be non-negative
#  base will be 2, 8, or 16
def to_base(dec_num: int, base: int) -> str:
    temp, output = dec_num, ''
    while temp != 0:
        output = chr(temp % base + 55) + \
            output if base == 16 and temp % base > 9 else str(
                temp % base) + output
        temp = temp // base
    return output


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
def check(expected, yours):
    if type(expected) != type(yours):
        print("your data type is", type(yours),
              "but should be", type(expected))
        return
    if expected == yours:
        print("CORRECT")
    else:
        print("INCORRECT: expected", expected, "but got", yours)


check(5, to_decimal('101', 2))
check(14, to_decimal('1110', 2))
check(418, to_decimal('642', 8))
check(738, to_decimal('1342', 8))
check(101, to_decimal('65', 16))
check(1402, to_decimal('57A', 16))

check('1111011', to_base(123, 2))
check('110010000', to_base(400, 2))
check('6540', to_base(3424, 8))
check('12134', to_base(5212, 8))
check('4027', to_base(16423, 16))
check('3E5F', to_base(15967, 16))
check('0', to_base(0, 2))
check('0', to_base(0, 8))
check('0', to_base(0, 16))
