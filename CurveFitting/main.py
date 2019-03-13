'''
Project Name : Non-linear iteration algorithm for multiple unknown variables using BFGS and curve fitting
Package requirements : pandas, xlrd, scipy.optimize and numpy
Author : Nivedita Pagar
Created on : 03/03/2019
Please read the readme file associated with this code
'''

import pandas as pd
from scipy.optimize import fmin_bfgs
import numpy

# Assigning Variables to data set
excel_filename  = "Book1.xlsx"
excel_sheetname = "Sheet1"
xi_columnname   = "Real (xi)"
yi_columnname   = "Abs (yi)" # Absolute value considered for easy calculations, otherwise the curve is inverted


# Class Data including any and all required methods for solving the algorithm
class Data:
    def __init__(self, filename, sheet):
        print("Initializing excel file")
        self.excel_data = pd.ExcelFile(filename).parse(sheet)

        self.xi_array = self.excel_data[xi_columnname]    # get xi column from excel sheet
        self.yi_array = self.excel_data[yi_columnname]    # get yi column from excel sheet

        self.x0 = self.xi_array.sum() / len(self.xi_array)  # calculate initial value of x0
        self.y0 = self.yi_array.sum() / len(self.yi_array)  # calculate initial value of y0
        self.r0 = ( self.xi_array.max() - self.xi_array.min() ) / 2 # calculate initial value of r0

    '''
    The method solve takes in no parameters and contains the main algorithm code to solve the non-linear equation'''
    def solve(self):
        initial_guess = numpy.array([self.x0, self.y0, self.r0])  # initial values of x0, y0 and r0
        self.result = fmin_bfgs(myfunc, initial_guess, args=(self.xi_array, self.yi_array) )

        # Splitting the result to obtain the three unknowns separately
        self.new_x0 = self.result[0]
        self.new_y0 = self.result[1]
        self.new_r0 = self.result[2]
        print("\nResult: \n x0: {} \n y0: {} \n r0: {} ".format(self.result[0], self.result[1], self.result[2]))

        # Calculating Cole parameters R0 and Rinf using distance formula
        x1_x2 = (self.new_r0**2 - self.new_y0**2)**(float(1)/2)
        self.R0 = x1_x2 + self.new_x0
        self.Rinf = self.new_x0 - x1_x2

        print("R0 : {} ".format(self.R0))
        print("Rinf: {} ".format(self.Rinf))

def myfunc(guess, x_array, y_array):
    x0, y0, r0 = guess
    total = 0 # The sum of x_array to be used further for calculating mean
    for i in range(len(x_array)):
        total += ((((x_array[i]-x0)**2 + (y_array[i]-y0)**2)**(float(1)/2)) - r0)**2
    return total


myData = Data(excel_filename, excel_sheetname)
myData.solve()
