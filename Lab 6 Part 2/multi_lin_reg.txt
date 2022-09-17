import numpy as np
import pandas as pd
import csv

# function name: multivar_linreg
# inputs: file_name- name of the train csv file
# output: 1xn numpy array [m1, m2, m3, ..., b] (row vector not column vector)
# return a numpy array! NOT a list
# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# Round each value to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
# Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)


def multivar_linreg(file_name):
    xVectors, yVectors = [], []
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for r in scanner:
                xVectors.append([])
                for c in range(len(r)):
                    if c + 1 == len(r):
                        yVectors.append(float(r[c]))
                    else:
                        xVectors[len(xVectors) - 1].append(float(r[c]))
    xVectors = np.column_stack((xVectors, np.ones(np.shape(xVectors)[0])))
    mbMat = np.matmul(np.linalg.inv(
        np.matmul(xVectors.T, xVectors)), np.matmul(xVectors.T, yVectors))
    return np.round(mbMat, 4)


# function name: predict
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
    # file_name- name of test csv file
# output: 1xm numpy array [y1, y2, y3 ...] (row vector not column vector)
    # return a numpy array! NOT a list
    # the order of the list corresponds to the order of the rows of data from top to bottom
    # Round each value to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
    # Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
def predict(inputs, file_name):
    predict = []
    with open(file_name) as file:
        scanner = csv.reader(file)
        header = next(scanner)
        if header is not None:
            for r in scanner:
                currRow = []
                for c in range(len(r)):
                    if c + 1 is len(r):
                        currRow.append(1)
                    else:
                        currRow.append(float(r[c]))
                predict.append(np.matmul(currRow, inputs))
    return np.round(predict, 4)


# function name: MAE
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
    # file_name- name of test csv file
# output: the mean absolute error of the predictions formed from inputs
    # round mae to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
    # Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
    # you may use any of the previous functions
def MAE(inputs, file_name):
    prediction, diff, num = predict(inputs, file_name), [], 0
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for r in scanner:
                diff.append(abs(prediction[num] - float(r[len(r) - 1])))
                num += 1
    return round(sum(diff) / len(diff), 4)


# function name: MRE
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
    # file_name- name of test csv file
# output: the mean relative error of the predictions formed from inputs
    # round mre to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
    # Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
    # you may use any of the previous functions
def MRE(inputs, file_name):
    prediction, diff, num = predict(inputs, file_name), [], 0
    with open(file_name) as file:
        scanner = csv.reader(file, delimiter=',')
        header = next(scanner)
        if header is not None:
            for r in scanner:
                diff.append(
                    abs(prediction[num] - float(r[len(r) - 1]))/float(r[len(r)-1]))
                num += 1
    return round(sum(diff) / len(diff), 4)


######## TEST CASES ########
# this test case is the same as the one in
# train_csv = "Real estate train.csv"
# test_csv = "Real estate test.csv"
#
# weights = multivar_linreg(train_csv)
# # weights = multivar_linreg(test_csv)
# expected_weights = np.array(
#     [4.9535, -0.2696, -0.0045, 1.1148, 230.7976, -13.5932, -14039.6784])
# print("expected weights:", expected_weights)
# print("your answer:", weights)
# print("CORRECT\n" if np.allclose(weights, expected_weights) else "INCORRECT\n")
#
# # NOTE: using expected_weights instead of weights for testing purposes
# # you should replace this with predicted to check if your model works
# predicted = predict(expected_weights, test_csv)
# expected_predictions = np.array([41.0483, 33.3038, 39.6696, 45.0673, 46.8449,
#                                 37.8108, 49.7323, 26.6559, 32.0756, 14.4788, 50.0397, 46.9619, 44.7727, 53.9234])
# print("expected predictions:", expected_predictions)
# print("your answer:", predicted)
# print("CORRECT\n" if np.array_equal(
#     predicted, expected_predictions) else "INCORRECT\n")
#
# # NOTE: using expected_weights instead of weights for testing purposes
# # you should replace this with predicted to check if your model works
# mae = MAE(expected_weights, test_csv)
# expected_mae = 5.4668
# print("expected MAE:", expected_mae)
# print("your answer:", mae)
# print("CORRECT\n" if mae == expected_mae else "INCORRECT\n")
#
# # NOTE: using expected_weights instead of weights for testing purposes
# # you should replace this with predicted to check if your model works
# mre = MRE(expected_weights, test_csv)
# expected_mre = 0.1518
# print("expected MRE:", expected_mre)
# print("your answer:", mre)
# print("CORRECT" if mre == expected_mre else "INCORRECT")
