import matplotlib.pyplot as plt

class scatterplot:
    def __init__(self, x_axis, y_axis) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis

    def show(self):
        plt.scatter(self.x_axis, self.y_axis)
        plt.title('Liquor Scatter Plot')
        plt.xlabel('Alcohol Content')
        plt.ylabel('Price Per 25 ounces')
        plt.tight_layout()
        plt.savefig('../figures/scatter.png')
        plt.close()