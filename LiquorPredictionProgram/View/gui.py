import sys

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from model.bar_chart import barchart

class gui(QDialog):
    def __init__(self, size, ols, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #initialize window size as size
        self.size = size
        self.ols = ols

        #create widget and set properties
        self.gui = QWidget()
        self.gui.setMinimumWidth(size.width())
        
        #create scroll window to prevent collapsing of items
        self.window = QScrollArea()
        self.window.setAlignment(Qt.AlignCenter)

        #create sliders and set properties
        self.alcoholSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.alcoholLabel = QLabel('Alcohol Percentage: 50%\n', self)

        self.priceSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.priceLabel = QLabel('Target Sales Growth Percentage: 175%\n\n', self)
        
        #create prediction labels
        self.predictPriceLabel = QLabel('Predicted Price per Shot: $NA, at NA% Alcohol Percentage!')
        self.predictAlcoholLabel = QLabel('Recommended Price per Shot: $NA, at NA% Alcohol Percentage to achieve NA% Sales Growth Percentage!')
        

    #setup all GUI elements
    def setupGUI(self):
        #Setup Gui
        self.gui.setWindowTitle("Capstone")

        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        
        #Styles
        with open('../gui.css',"r") as style:
            self.gui.setStyleSheet(style.read())
        

        # self.gui.setGeometry(100, 100, 280, 80)
        #create labels and text for gui
        barchartHeader = QLabel('<h1>Barchart</h1>')
        barchartinfo = QLabel('<p>This barchart displays the mean price per ounce for each liquor. This barchart can be used to determine general pricing for each liquor.</p>')
        scatterHeader = QLabel('<h1><br /><br />Scatter Plot</h1>')
        scatterinfo = QLabel('<p>This scatter plot show the relationship between alcohol conecntration per volume and price per ounce of liquor. This scatter plot can be used to determine which alcohol concentration has which price.')
        scatterNote = QLabel('<p><i>**Notice high concentrations of data at 5%, 12.5%, AND 40%. These are the most common alcoholic percentages.</i></p>')
        olsHeader = QLabel('<h1><br /><br />Ordinary Least Squares Plot</h2>')
        olsinfo = QLabel('<p>This plots a regression line that can be used for prediction. This plot can be used to predict what any alcohol content will cost per ounce.</p>')


        #load barchart
        label = QLabel()
        barchart = QPixmap("../figures/barchart.png")
        label.setPixmap(barchart)
        label.setMask(barchart.mask())
        

        #load scatter plot
        label2 = QLabel()
        scatter = QPixmap("../figures/scatter.png")
        label2.setPixmap(scatter)
        label2.setMask(scatter.mask())
       

        #load ols
        label3 = QLabel()
        ols = QPixmap("../figures/ols.png")
        label3.setPixmap(ols)
        label3.setMask(ols.mask())


        #sliders
        self.alcoholSlider.setRange(0, 100)
        self.alcoholSlider.setValue(50)
        self.alcoholSlider.setSingleStep(5)
        self.alcoholSlider.setPageStep(10)
        self.alcoholSlider.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.alcoholSlider.valueChanged.connect(self.updateAlcohol)
    
        self.priceSlider.setRange(50, 300)
        self.priceSlider.setValue(175)
        self.priceSlider.setSingleStep(5)
        self.priceSlider.setPageStep(10)
        self.priceSlider.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.priceSlider.valueChanged.connect(self.updatePrice)

        #buttons
        alcoholButton = QPushButton()
        alcoholButton.setText("Get price based on alcohol content")
        alcoholButton.clicked.connect(self.predictAlcohol)
        priceButton = QPushButton()
        priceButton.clicked.connect(self.predictPrice)
        priceButton.setText("Get price per shot based on alcohol content and target sales growth")

        #descriptive labels
        sliderHeader = QLabel('<h1>Predict Pricing</h1>')
        sliderHeader.setAlignment(QtCore.Qt.AlignCenter)
        sliderDesc = QLabel('<p>Feel free to scroll below, you can use just the alcohol slider to predict what a alcohol of that percentage might be price. <br /> You can also use the combined alcohol and percentage sliders to get a recommendation for a shot price based on the alcohol content and your requested profit margins.')
        sliderDesc.setAlignment(QtCore.Qt.AlignCenter)
        
        #Add everything to the gui
        layout.addRow(barchartHeader)
        layout.addRow(barchartinfo)
        layout.addRow(label)
        layout.addRow(scatterHeader)
        layout.addRow(scatterinfo)
        layout.addRow(label2)
        layout.addRow(scatterNote)
        layout.addRow(olsHeader)
        layout.addRow(olsinfo)
        layout.addRow(label3)

        layout.addRow(sliderHeader)
        layout.addRow(sliderDesc)
        layout.addRow(self.alcoholSlider)
        layout.addRow(self.alcoholLabel)
        layout.addRow(self.priceSlider)
        layout.addRow(self.priceLabel)

        layout.addRow(self.predictPriceLabel)
        layout.addRow(self.predictAlcoholLabel)

        layout.addWidget(alcoholButton)
        layout.addWidget(priceButton)

        #add gui to scrollable window
        self.gui.setLayout(layout)
        
        self.window.setWidget(self.gui)
    
    def updateAlcohol(self, value):
        self.alcoholLabel.setText(f'Alcohol Percentage: {value}%\n')

    def updatePrice(self, value):
        self.priceLabel.setText(f'Target Sales Growth Percentage: {value}%\n\n')
   
    def predictAlcohol(self):
        #call method defined in ols module
        value = self.alcoholSlider.value()
        prediction = self.ols.predictPricePerOunce(value)
        self.predictPriceLabel.setText(f'Predicted Price per Shot: ${prediction}, at {float(value)}% Alcohol Percentage!')

    def predictPrice(self, value):
        prediction = self.ols.predictSalePrice(self.alcoholSlider.value(), self.priceSlider.value()/100)
        self.predictAlcoholLabel.setText(f'Recommended Price per Shot: ${prediction}, at {float(self.alcoholSlider.value())}% Alcohol Percentage to achieve {self.priceSlider.value()}% Sales Growth Percentage!')


    #display GUI
    def show(self, app):
        #show gui
        self.window.showMaximized()

        #setup exit
        sys.exit(app.exec())