import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import math


# function name: least_sq
# inputs: file_name- name of the csv file
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
# LITERALLY return m, b (both rounded 4 decimal places)
# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
    n, x_sum, y_sum, x_square, xy = 0, 0, 0, 0, 0
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for row in scanner:
                x, y, n = float(row[0]), float(row[1]), n + 1
                x_sum, y_sum, x_square, xy = x_sum + x, y_sum + \
                    y, x_square + math.pow(x, 2), xy+x*y
    slope = (n * xy - x_sum * y_sum) / (n * x_square - math.pow(x_sum, 2))
    y_inter = (y_sum - slope * x_sum) / n
    return round(slope, 4), round(y_inter, 4)


# function name: mat_least_sq
# inputs: file_name- name of the csv file
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
    # LITERALLY return m, b (both rounded 4 decimal places)
    # YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
    x_vector, y_vector, n = [], [], 0
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for row in scanner:
                n += 1
                x_vector.append(float(row[0]))
                y_vector.append(float(row[1]))
    x_mat = np.column_stack((x_vector, np.ones(n)))
    m_b_mat = np.matmul(np.linalg.inv(
        np.matmul(x_mat.T, x_mat)), np.matmul(x_mat.T, y_vector))
    return round(m_b_mat[0], 4), round(m_b_mat[1], 4)
    pass

# function name: predict
# inputs: file_name- name of the csv file
    # x- input value that you will interpolate or extrapolate using mat_least_sq
# output: the predicted value based on the linear regression equation found using mat_least_sq
    # The output should be rounded to 4 decimal places
# assumptions: The csv file will always have headers in the order of: x, y


def predict(file_name, x):
    m, b = mat_least_sq(file_name)
    return round(x * m + b, 4)


# function name: plot_reg
# inputs: file_name- name of the csv file
    # using_matrix: True if you are plotting the linear equation from mat_least_sq
    #                 False if you are plotting the linear equation from least_sq
# output: nothing is returned
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
    # your graph should have the following: labeled x and y axes, title, legend
    # if using_matrix is False (using least_sq), use X's and red in your graph
    # if using_matrix is True (using mat_least_sq), you can use any color except for the default blue and red
    # you can use any marker except for the default dot and X
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
    x_points, y_points = [], []
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for row in scanner:
                x_points.append(float(row[0]))
                y_points.append(float(row[1]))
    _color = 'purple' if using_matrix is True else 'red'
    _marker = '+' if using_matrix is True else 'x'
    _title = 'Using Matrix Least Sqaures' if using_matrix is True else 'Using Algebra Least Squares'
    x = np.linspace(sorted(x_points)[0], sorted(x_points, reverse=True)[0])
    m, b = mat_least_sq(
        file_name) if using_matrix is True else least_sq(file_name)
    plt.plot(x, m*x+b, '-', label=f'y={m}x+{b}', color=_color)
    plt.scatter(x_points, y_points, color=_color,
                label='data points', marker=_marker)
    plt.title(_title)
    plt.xlabel('x', color='black')
    plt.ylabel('y', color='black')
    plt.legend(loc='upper left')
    plt.show()
    return


######## TEST CASES ########
# this test case is the same as the one in
# csv_file = "data2.csv"
#
# m1, b1 = least_sq(csv_file)
# print("Slope using algebraic least squares:", m1)
# print("y-intercept using algebraic least squares:", b1)
# print()
#
# m2, b2 = mat_least_sq(csv_file)
# print("Slope using linear algebra least squares:", m2)
# print("y-intercept using linear algebra least squares:", b2)
# print()
#
# y1 = predict(csv_file, 100)  # extrapolation
# print("Extrapolation:", y1)
# y2 = predict(csv_file, 38)  # interpolation
# print("Interpolation:", y2)
#
# plot_reg(csv_file, False)
#
# plot_reg(csv_file, True)
