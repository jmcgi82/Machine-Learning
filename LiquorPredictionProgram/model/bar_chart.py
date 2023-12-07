import matplotlib.pyplot as plt

class barchart:
    
    def __init__(self, x_axis, y_axis) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis

    def show(self):
        plt.bar(self.x_axis, self.y_axis)
        plt.title('Liquor Bar Chart')
        plt.xlabel('Category')
        plt.ylabel('Mean price per ounce')
        plt.tight_layout()
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=.5)
        plt.savefig('../figures/barchart.png')
        plt.close()