"""
Name: Kenry Yu
"""


class Vector:

    # input: l - a list
    # Example: Vector([1, 2, 3, 4]) will make a vector <1, 2, 3, 4>
    def __init__(self, l):
        # ALREADY DONE FOR YOU! DO NOT TOUCH
        self.v = l
        self.size = len(l)

    # get's the ith element of the vector
    def get_ith_element(self, i):
        return self.v[i]

    # Part0
    # vector addition (ALREADY IMPLEMENTED)
    # inputs: self, other
    # output: if addition is possible, return the sum
    #           if addition is not possible, return None
    def __add__(self, other):
        if self.size != other.size:
            return None
        sum = []
        for i in range(self.size):
            sum.append(self.get_ith_element(i) + other.get_ith_element(i))
        return Vector(sum)

    # Part1
    # TODO: implement vector subtraction
    # inputs: self, other
    # output: if subtraction is possible, return the differences
    #           if subtraction is not possible, return None
    def __sub__(self, other):
        if self.size != other.size:
            return None
        sum = []
        for i in range(self.size):
            sum.append(self.get_ith_element(i) - other.get_ith_element(i))
        return Vector(sum)

    # Part2
    # TODO: implement dot product
    # inputs: self, other
    # output: if dot product is possible, return the dot product
    #           if dot product is not possible, return None

    def __mul__(self, other):
        if self.size != other.size:
            return None
        sum = 0
        for i in range(self.size):
            sum += self.get_ith_element(i) * other.get_ith_element(i)
        return sum

    # DO NOT TOUCH! For debugging purposes

    def __str__(self):
        return str(self.v)


"""**********************************************************************"""
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
"""**********************************************************************"""


# def checker(expected, actual):
#     if type(expected) == type(actual):
#         if str(expected) == str(actual):
#             print("CORRECT!")
#         else:
#             print("expected " + str(expected) + ", but got " + str(actual))
#     else:
#         print("Data type issue!")


"""**********************************************************************"""

# vec1 = Vector([53, -95, 13, -22, 78])
# vec2 = Vector([-61, 72, 95, 13, 15, 69, -47, 36, 73])
# vec3 = Vector([-30, -46, 24, 40, -25, -96, 23, -33, -8])
#
# test1 = vec2 - vec3
# expected1 = Vector([-31, 118, 71, -27, 40, 165, -70, 69, 81])
# checker(expected1, test1)
#
# test2 = vec1 - vec2
# expected2 = None
# checker(expected2, test2)
#
# test3 = vec2 * vec3
# expected3 = -8534
# checker(expected3, test3)
#
# test4 = vec1 * vec3
# expected4 = None
# checker(expected4, test4)
