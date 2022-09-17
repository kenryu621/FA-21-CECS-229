"""
Name: Kenry Yu
"""


class Matrix:

    # input: mat (a 2d list)
    # Example: Matrix([[1, 2, 3], [2, 4, 6]]) makes a matrix like...
    # [1 2 3 ]
    # [2 3 6 ]
    def __init__(self, mat):
        # ALREADY DONE FOR YOU! DO NOT TOUCH
        self.m = mat                 # the matrix
        self.rows = len(mat)        # number of rows
        self.cols = len(mat[0])        # number of columns

    # get's the element of the matrix in row i, column j
    def get_element(self, i, j):
        # ALREADY DONE FOR YOU! DO NOT TOUCH
        return self.m[i][j]

    # Part3
    # TODO: implement matrix addition
    # inputs: self, other
    # output: if matrix addition is possible, return the sum Matrix
    #          DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
    #           if matrix addition is not possible, return None
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        sum = Matrix([[self.get_element(r, c) + other.get_element(r, c)
                     for c in range(self.cols)] for r in range(self.rows)])
        return sum

    # Part4
    # TODO: implement matrix subtraction
    # inputs: self, other
    # output: if matrix subtraction is possible, return the difference Matrix
    #          DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
    #           if matrix subtraction is not possible, return None
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        sum = Matrix([[self.get_element(r, c) - other.get_element(r, c)
                     for c in range(self.cols)] for r in range(self.rows)])
        return sum

    # Part5
    # TODO: implement dot product
    # inputs: self, other
    # output: if matrix multiplication is possible, return the product Matrix
    #          DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
    #           if matrix multiplication is not possible, return None

    def __mul__(self, other):
        if self.cols != other.rows:
            return None
        sum = Matrix([[0 for i in range(other.cols)]
                     for j in range(self.rows)])
        for i in range(sum.rows):
            for j in range(sum.cols):
                for t in range(self.cols):
                    sum.m[i][j] += self.get_element(i, t) * \
                                                    other.get_element(t, j)
        return sum

    # DO NOT TOUCH! For debugging purposes

    def __str__(self):
        string = ""
        for r in self.m:
            string += "["
            for c in r:
                string += str(c) + " "
            string += "]\n"
        return string


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
#             print("expected:\n" + str(expected) + ", but got:\n" + str(actual))
#     else:
#         print("Data type issue!")


"""**********************************************************************"""

# mat1 = Matrix([[1, 2, 3],
#               [4, 6, 8]])
#
# mat2 = Matrix([[-10, 9, 4],
#               [-19, 4, 2],
#               [7, -3, 2]])
#
# mat3 = Matrix([[1, 6],
#               [-10, 7]])
#
# mat4 = Matrix([[9, -4, 3],
#               [10, -2, 1]])
#
# test1 = mat4 + mat1
# expected1 = Matrix([[10, -2, 6], [14, 4, 9]])
# checker(expected1, test1)
#
# test2 = mat1 + mat2
# expected2 = None
# checker(expected2, test2)
#
# test3 = mat4 - mat1
# expected3 = Matrix([[8, -6, 0], [6, -8, -7]])
# checker(expected3, test3)
#
# test4 = mat1 - mat2
# expected4 = None
# checker(expected4, test4)
#
# test5 = mat3 * mat1
# expected5 = Matrix([[25, 38, 51], [18, 22, 26]])
# checker(expected5, test5)
#
# test6 = mat1 * mat3
# expected6 = None
# checker(expected6, test6)
