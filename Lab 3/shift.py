# function name: shift_cipher_encode
# inputs: string - string to encode (str)
# n - amount to shift by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
#  Should be able to accommodate upper and lower case letters
#  0 < n < 26
# restrictions:  DO NOT USE A DICTIONARY OR LIST TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):
    # out A string to store encoded letters
    # c   Character of string
    # i   Encoded ASCII number
    out = ""
    for c in string:
        i = 65 if c.isupper() else 97 if c.islower() else None
        out += chr((ord(c) - i + n) % 26 + i) if c.isalpha() else c
    return out


# function name: shift_cipher_decode
# inputs: string - string to decode (str)
    # n - amount to shift by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
    #  Should be able to accommodate upper and lower case letters
    #  0 < n < 26
# restrictions:  DO NOT USE A DICTIONARY OR LIST TO ENCODE YOUR LETTERS
def shift_cipher_decode(string, n):
    # out A string to store decoded letters
    # c   Character of string
    # i   Decoded ASCII number
    out = ""
    for c in string:
        i = 65 if c.isupper() else 97 if c.islower() else None
        out += chr((ord(c) - i - n) % 26 + i) if c.isalpha() else c
    return out


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
def check(expected, yours):
    if type(expected) != type(yours):
        print("INCONSISTENT DATA TYPES! EXPECTED",
              type(expected), "BUT GOT", type(yours))
    elif expected != yours:
        print("INCORRECT! EXPECTED \'" + expected
              + "\' BUT GOT \'" + yours + "\'")
    else:
        print("CORRECT")


# check("Wmfauw ak yjwsl! :)", shift_cipher_encode("Eunice is great! :)", 18))
# check("Qobkbny sc qbokd dyy!!!", shift_cipher_encode(
#     "Gerardo is great too!!!", 10))
# check("Gjwsfwit nx fqxt lwjfy! :I", shift_cipher_encode(
#     "Bernardo is also great! :D", 5))
# check("WYWM229 cm nby vymn wfumm un WMOFV", shift_cipher_encode(
#     "CECS229 is the best class at CSULB", 20))
#
# check("This is the lab.", shift_cipher_decode("Qefp fp qeb ixy.", 23))
# check("ThErE r m@ny m0rE Labs 2 come!",
#       shift_cipher_decode("KyViV i d@ep d0iV Crsj 2 tfdv!", 17))
# check("s0 B prepared!", shift_cipher_decode("y0 H vxkvgxkj!", 6))
# check("pineapples", shift_cipher_decode("buzqmbbxqe", 12))
