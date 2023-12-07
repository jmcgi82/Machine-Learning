import sys
sys.path.append("..")

from model.load_data import loader
from model.liquor_class import liquor
from model.bar_chart import barchart
from model.scatter_plot import scatterplot
from model.ols import ols
from View.gui import gui

from PyQt5.QtWidgets import *
from PyQt5 import QtGui



######################################################
#   Load data from persistence
######################################################

#load all data from database
loader = loader()
result = loader.load()
types = set()

liquors = list()
#convert the raw load data into a usable liquor object
#populate a list of all available types
for r in result:
    liquors.append(liquor(r[0], r[1], r[2], r[3], r[4]))
    types.add(r[2])

######################################################
#   Bar chart creation
######################################################

x_axis = list()
y_axis = list()

#for each type of liquor, loop through all liquors
for t in types:
    count = 0.0
    summation = 0.0
    for r in liquors:
        #if the types match, add one to count and one to summation
        if t == r.getType():
            count += 1
            summation += r.getPricePerOunce()
    #once all liquors have been checked, add the current type to the x axis list
    x_axis.append(t)
    #calculate the mean for this liquor
    mean = round(summation/count, 2)
    
    #add the mean to the y axis list
    y_axis.append(mean)

#generate bar graph using bargraph class
barchart = barchart(x_axis, y_axis)
barchart.show()

######################################################
#   Scatter Plot Creation
######################################################

x_axis = list()
y_axis = list()

#for each liquor, add its' alcohol content to list x and its price per ounce to list y
for l in liquors:
    if l.getAlcoholContent() < 60:
        x_axis.append(l.getAlcoholContent())
    if l.getPricePerOunce() < 25:
        y_axis.append(l.getPricePerOunce())

#Account for extra incomplete data
x_axis.pop()
x_axis.pop()

#Generate scatter plot using scatterplot class
scatterplot = scatterplot(x_axis, y_axis)
scatterplot.show()


######################################################
#   Ordinary Least Squares Creation
######################################################

x_axis = list()
y_axis = list()
min_x = 100
max_x = 0.0

#for each liquor, add its' alcohol content to list x and its price per ounce to list y
#To accout for the ols line, also keep track of min and max x values
for l in liquors:
    if l.getAlcoholContent() < 60:
        x_axis.append(l.getAlcoholContent())
        if l.getAlcoholContent() < min_x:
            min_x = l.getAlcoholContent()
        if l.getAlcoholContent() > max_x:
            max_x = l.getAlcoholContent()
    if l.getPricePerOunce() < 25:
        y_axis.append(l.getPricePerOunce())

#Account for extra incomplete data
x_axis.pop()
x_axis.pop()

#create the new ols object
ols = ols(x_axis, y_axis, min_x, max_x)



#show the ols graph
ols.show()

######################################################
#   GUI
######################################################
app = QApplication([])

size = app.desktop().availableGeometry()
app.setWindowIcon(QtGui.QIcon('../icon.png'))
app.setApplicationName("Liquor Management System")

gui = gui(size, ols)
gui.setupGUI()
gui.show(app)





