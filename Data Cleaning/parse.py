data_file = open('data.txt', 'r')

currLine = 1
while (currLine < 901):
    tempString = data_file.readline()
    entries = tempString.split(' ')


    #Assign each entry to a value
    #Remove extra standard deviation
    entries.pop()
    #Remove alchohol precentage and save it
    alchPercent = entries.pop()
    #Remove extra standard deviation
    entries.pop()
    #Remove price per ounce and save it
    pricePerOunce = entries.pop()
    #remove type
    entries.pop()
    #remove liquor type and save it
    type = entries.pop()

    #check if it is a specialty liquor and save name accordingly
    if type == 'Beverage' or type == 'Cream' or type == 'Drink':
        type = entries.pop() + " " + type
        type = entries.pop() + " " + type

    if type == 'Alcohol':
        type = entries.pop() + " " + type
    

    #save remaining fields as name
    name = entries.pop()
    while (len(entries) > 0):
        name =  entries.pop() + " " + name

    #create final string to be saved
    result = "(\'" + name + "\',\'" + type + "\'," + pricePerOunce + "," + alchPercent + "),\n"
    
    with open("updated.txt", "a") as write_file:
        write_file.write(result)
    currLine += 1

    
data_file.close()
print("Success!")
    