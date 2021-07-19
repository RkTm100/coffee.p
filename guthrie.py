import csv 

import numpy as nm

def getDataSource(data_path):
    coffee_cups=[]
    sleep_hours=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_cups.append(float(row["Coffee in ml"]))
            sleep_hours.append(float(row["sleep in hours"]))
    
    return{"x": coffee_cups,"y":sleep_hours }

def findCorrelation(dataSource):
    correlation=nm.corrcoef(dataSource["x"],dataSource["y"])
    print("correlationship between coffee cups and sleep hours: \n ", correlation[0,1])

def setUp():
    data_path="./coffee.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    
setUp()


