import numpy as np

# function name: per_to_dec
# inputs: mat - n x n numpy array with percentages
# output: n x n numpy array where percentages are converted to decimal numbers
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
#  more or less rows/columns (always square matrix though)


def per_to_dec(mat):
    return mat.astype(float) / 100


# function name: sig_change
# inputs: oldmat - n x n numpy array (decimal form)
    # newmat - n x n numpy array (decimal form)
# output: True if there is at least one element in newmat that is at least 0.0001 away
    # from its respective counterpart in oldmat
    # False otherwise
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
    #  more or less rows/columns (always square matrix though)
def sig_change(oldmat, newmat):
    for row in range(len(oldmat)):
        for col in range(len(oldmat[row])):
            if abs(oldmat[row][col] - newmat[row][col]) >= 0.0001:
                return True
    return False


# function name: prob_x
# inputs: mat - n x n numpy array with PERCENTAGES
    # x - number of iterations
# output: n x n numpy array that represents the probability matrix after x stages
    # Use per_to_dec here
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
    #  more or less rows/columns (always square matrix though)
    #  x will always be >= 1
def prob_x(mat, x):
    temp = per_to_dec(mat)
    for i in range(x - 1):
        temp = np.matmul(temp, per_to_dec(mat))
    return temp


# function name: long_run_dist
# inputs: mat - n x n numpy array with PERCENTAGES
# output: n x n numpy array where percentages are converted to decimals
    # USE sig_change and per_to_dec
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
    #  more or less rows/columns (always square matrix though)
def long_run_dist(probs):
    i = 1
    while sig_change(prob_x(probs, i), prob_x(probs, i + 1)):
        i += 1
    return prob_x(probs, i + 1)


"""**********************************************************************"""
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
"""**********************************************************************"""


def checker(expected, actual):
    if type(expected) == type(actual):
        if type(expected) == bool:
            if expected == actual:
                print("CORRECT!")
            else:
                print("expected " + str(expected) + ", but got " + str(actual))
        else:
            if np.all(np.isclose(expected, actual)):
                print("CORRECT!")
            else:
                print("expected " + str(expected) + ", but got " + str(actual))
    else:
        print("Data type issue!")


"""**********************************************************************"""

# prob = np.array([[80, 18, 2],
#                  [40, 50, 10],
#                  [20, 60, 20]])
#
#
# print("test 0: per_to_dec")
# test0 = per_to_dec(prob)
# expected0 = np.array([[0.8, 0.18, 0.02],
#                       [0.4, 0.5, 0.1],
#                       [0.2, 0.6, 0.2]])
# checker(expected0, test0)
#
#
# print("\ntest 1: sig_change")
# compare1 = np.array([[0.716, 0.2461, 0.038],
#                      [0.54, 0.382, 0.078],
#                      [0.44, 0.456, 0.004]])
# test1 = sig_change(compare1, expected0.dot(expected0))
# expected1 = True
# checker(expected1, test1)
#
#
# print("\ntest 2: sig_change")
# compare2 = np.array([[0.71601, 0.24601, 0.03801],
#                      [0.54, 0.382, 0.07801],
#                      [0.44, 0.45603, 0.104]])
# test2 = sig_change(compare2, expected0.dot(expected0))
# expected2 = False
# checker(expected2, test2)
#
#
# print("\ntest 3: prob_x")
# test3 = prob_x(prob, 3)
# expected3 = expected0.dot(expected0).dot(expected0)
# checker(expected3, test3)
#
#
# print("\ntest 4: long_run_dist")
# test4 = long_run_dist(prob)
# expected4 = np.array([[0.64887596, 0.29769378, 0.05343026],
#                       [0.64882099, 0.29773604, 0.05344296],
#                       [0.64878924, 0.29776046, 0.0534504]])
# checker(expected4, test4)
# checker(expected4, test4)
