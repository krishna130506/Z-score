import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
populationMean = statistics.mean(data)
Populationstdev = statistics.stdev(data)
print("The Population Mean is {}".format(populationMean))
print("The Population standard deviation is {}".format(Populationstdev))


def random_set_of_mean(counter):
        dataset = []
        for i in range(0,counter):
                random_index = random.randint(0,len(data))
                value = data[random_index]
                dataset.append(value)
        mean = statistics.mean(dataset)
        stdev = statistics.stdev(dataset)
        return(mean)



def show_fig(mean_list):
        df = mean_list
        mean1 = statistics.mean(mean_list)
        stdev1 = statistics.stdev(mean_list)
        print("mean of sampling distribution ", mean1)
        newInt = []
        for i in range(1):
                newInt.append(random.choice(data))
        newMean = statistics.mean(newInt)
        first_stdev_start, first_stdev_end = mean1-stdev1,mean1+stdev1
        second_stdev_start, second_stdev_end = mean1-(2*stdev1),mean1+(2*stdev1)
        third_stdev_start, third_stdev_end = mean1-(3*stdev1),mean1+(3*stdev1)
        print("std1", first_stdev_start,first_stdev_end)
        print("std2", second_stdev_start,second_stdev_end)
        print("std3", third_stdev_start,third_stdev_end)
        fig = ff.create_distplot([df],["reading_time"],show_hist=False)
        fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.9],mode = "lines",name = "Mean"))
        fig.add_trace(go.Scatter(x = [newMean,newMean],y = [0,0.9],mode = "lines",name = "New Mean"))
        fig.add_trace(go.Scatter(x = [first_stdev_start,first_stdev_start],y = [0,0.9],mode = "lines",name = "1 start"))
        fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end],y = [0,0.9],mode = "lines",name = "1 start"))
        fig.add_trace(go.Scatter(x = [second_stdev_start,second_stdev_start],y = [0,0.9],mode = "lines",name = "2 start"))
        fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end],y = [0,0.9],mode = "lines",name = "2 end"))
        fig.add_trace(go.Scatter(x = [third_stdev_start,third_stdev_start],y = [0,0.9],mode = "lines",name = "3 start"))
        fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end],y = [0,0.9],mode = "lines",name = "3 end"))
        fig.show()
        z_score = (newMean-mean1)/stdev1
        print("the z_score is-",z_score)

def setup():
        mean_list = []
        for i in range(0,100):
                set_of_mean = random_set_of_mean(30)
                mean_list.append(set_of_mean)
        show_fig(mean_list)
        
setup()

newInt = []
for i in range(1):
        newInt.append(random.choice(data))
newMean = statistics.mean(newInt)
