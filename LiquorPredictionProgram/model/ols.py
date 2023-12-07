import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

class ols:
    def __init__(self, x_axis, y_axis, min_x, max_x) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.max_x = max_x
        self.min_x = min_x
        self.result = 0

    def show(self):
        #add constant term
        x_axis = sm.add_constant(self.x_axis)

        # performing the regression
        # and fitting the model
        self.result = sm.OLS(self.y_axis, self.x_axis).fit()
 
        # print the summary table
        # print(self.result.summary())

        plt.scatter(self.x_axis, self.y_axis)
        plt.title('Ordinary Least Squares Plot')
        plt.xlabel('Alcohol Content')
        plt.ylabel('Price Per 25 ounces')
        plt.tight_layout()
 
        # range of values for plotting
        # the regression line
        x_axis = np.arange(self.min_x, self.max_x, 1)
 
        # the substituted equation
        y_axis = .0011 * x_axis + 2.9547
 
        # plotting the regression line
        plt.plot(y_axis, 'r')
        plt.savefig('../figures/ols.png')
        plt.close()

    def predictPricePerOunce(self, x_value):
        return round(float(self.result.predict(x_value)),2)
        
    def predictSalePrice(self, x_value, profitDecimal):
        return round(profitDecimal * float(self.result.predict(x_value)),2)