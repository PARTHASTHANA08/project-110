import csv 
import random 
import statistics 
import pandas as pd 
import plotly.graph_objects as go
import plotly.figure_factory as ff 
from pandas.core.indexes.base import maybe_extract_name

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
def random_mean(counter):
    dataSet = []
    for i in range (0,counter):
         randomIndex = random.randint(0,len(data) - 1)
         value = data[randomIndex]
         dataSet.append(value)
    mean = statistics.mean(dataSet)     
    return(mean)
def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["claps"])
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,15],mode = "lines" , name = "Mean"))
    fig.show()     
def setup():
    meanList = []
    for i in range(0,2000):
        means = random_mean(200)
        meanList.append(means)
    showFig(meanList)
    mean = statistics.mean(meanList)
    print("Mean of the sampling distribution", mean)

setup() 
