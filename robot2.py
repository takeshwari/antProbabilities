from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import sys



#draw the new graph
def demo(a):
    fig1 = plt.figure(1)
    plt.imshow(a, cmap='gray_r', interpolation='nearest')
    #plt.colorbar()
    plt.grid(True)


#add labels to graph
def annotateGraph(nestR, nestC, foodRow, foodCol):
    plt.scatter(nestR, nestC, marker='o', s=10, zorder=20)
    plt.annotate(
        "Ant's Home",
        xy=(nestR, nestC), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='pink', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    for x in range(len(foodRow)):
        plt.scatter(foodRow[x], foodCol[x], marker='o', s=10, zorder=20)
        plt.annotate(
            "FOOD!!!",
            xy=(foodRow[x], foodCol[x]), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='pink', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))



#Update Probability
def updateProb(time, intialProb, row, col, otherProb, nestR, nestC, foodProb):

    if(time ==0):
        for i in range(row):
            for x in range(col):
                if(foodProb[i][x]==0):
                    otherProb[i][x]=intialProb
        return


    for i in range(row):
        for x in range(col):
            counter=0
            if(i==0):
                if(x==0):
                    otherProb[i+1][x+1] = otherProb[i+1][x+1] + intialProb/3
                    otherProb[i][x+1]= otherProb[i][x+1] + intialProb/3
                    otherProb[i+1][x] = otherProb[i+1][x] +intialProb/3
                    counter= 1
                elif(x==(col-1)):
                    otherProb[i +1][x -1] = otherProb[i +1][x -1] +intialProb/3
                    otherProb[i+1][x ] = otherProb[i+1][x ] + intialProb/3
                    otherProb[i][x-1] = otherProb[i][x-1 ] + intialProb/3
                    counter = 1
                else:
                    otherProb[i + 1][x + 1] = otherProb[i + 1][x + 1] + intialProb / 5
                    otherProb[i +1][x - 1] = otherProb[i + 1][x - 1] + intialProb / 5
                    otherProb[i+1][x] =  otherProb[i+1][x] + intialProb / 5
                    otherProb[i][x-1] = otherProb[i][x-1] + intialProb / 5
                    otherProb[i][x+1] =  otherProb[i][x+1] + intialProb / 5
                    counter = 1
            if(i== (row-1)):
                if(x==(col-1)):
                    otherProb[i - 1][x - 1] = otherProb[i - 1][x - 1] + intialProb / 3
                    otherProb[i][x - 1] = otherProb[i][x - 1] + intialProb / 3
                    otherProb[i - 1][x] = otherProb[i - 1][x] + intialProb / 3
                    counter = 1
                elif(x==0):
                    otherProb[i][x + 1] = otherProb[i][x +1] + intialProb / 3
                    otherProb[i -1][x] = otherProb[i- 1][x] + intialProb / 3
                    otherProb[i-1][x +1] = otherProb[i -1][x+1] + intialProb / 3
                    counter = 1
                else:
                    otherProb[i - 1][x + 1] = otherProb[i -1][x + 1] + intialProb / 5
                    otherProb[i - 1][x - 1] = otherProb[i - 1][x - 1] + intialProb / 5
                    otherProb[i - 1][x] = otherProb[i - 1][x] + intialProb / 5
                    otherProb[i][x - 1] = otherProb[i][x - 1] + intialProb / 5
                    otherProb[i ][x + 1] = otherProb[i][x + 1] + intialProb / 5
                    counter = 1
            if(x==0):
                if(i != (row-1) ) and (i !=0):
                    otherProb[i-1 ][x + 1] = otherProb[i -1][x + 1] + intialProb / 5
                    otherProb[i+1][x+1] = otherProb[i+1][x+1] + intialProb / 5
                    otherProb[i -1][x] = otherProb[i - 1][x] + intialProb / 5
                    otherProb[i+1][x ] = otherProb[i+1][x] + intialProb / 5
                    otherProb[i][x + 1] = otherProb[i][x + 1] + intialProb / 5
                    counter = 1
            if(x==(col-1)):
                if( i != (row-1) ) and ( i != 0):
                    otherProb[i - 1][x -1] = otherProb[i - 1][x - 1] + intialProb / 5
                    otherProb[i + 1][x - 1] = otherProb[i + 1][x - 1] + intialProb / 5
                    otherProb[i - 1][x] = otherProb[i - 1][x] + intialProb / 5
                    otherProb[i + 1][x] = otherProb[i + 1][x] + intialProb / 5
                    otherProb[i][x -1] = otherProb[i][x - 1] + intialProb / 5
                    counter = 1
            if(counter==0):
                otherProb[i+1][x+1] =  otherProb[i+1][x+1] + intialProb / 8
                otherProb[i+1][x]= otherProb[i+1][x] + intialProb / 8
                otherProb[i+1][x-1]= otherProb[i+1][x-1] + intialProb / 8
                otherProb[i][x+1] =otherProb[i][x+1] + intialProb / 8
                otherProb[i][x-1] = otherProb[i][x-1] + intialProb / 8
                otherProb[i-1][x]= otherProb[i-1][x] + intialProb / 8
                otherProb[i - 1][x-1] = otherProb[i - 1][x-1] + intialProb / 8
                otherProb[i - 1][x + 1] = otherProb[i - 1][x +1] + intialProb / 8




#create array with paths from food to nest.
def foodProb1(intialProb, row, col, pathMatrix, nestR, nestC, foodRow, foodCol,time):
    if time == 0:
        pathMatrix[nestR][nestC]=intialProb
        return None;
    var= time;

    for a in range(len(foodRow)):
        if (foodRow[a] == nestR):
            if( foodCol[a]>nestC):
                for b in range(foodCol[a]-var, foodCol[a]):
                    if (b < row) and (b < col):
                        pathMatrix[b][foodRow[a]] = intialProb +  pathMatrix[b][foodRow[a]]
                      # pathMatrix[foodRow[a]][b] = intialProb + pathMatrix[foodRow[a]][b]
            else:
                for b in range(foodCol[a], foodCol[a]+var):
                    if (b < row) and (b < col):
                        pathMatrix[b][foodRow[a]] = intialProb + pathMatrix[b][foodRow[a]]
                       # pathMatrix[foodRow[a]][b] = intialProb + pathMatrix[foodRow[a]][b]
        elif (foodCol[a] == nestC):
            if (foodRow[a] > nestR):
                for b in range(foodRow[a]-var, foodRow[a]):
                    if(b<row) and (b<col):
                        pathMatrix[foodCol[a]][b] = intialProb +  pathMatrix[foodCol[a]][b]
                       # pathMatrix[b][foodCol[a]] = intialProb +  pathMatrix[b][foodCol[a]]
            else:
                for b in range(foodRow[a], foodRow[a]+var):
                    if (b < row) and (b < col):
                        pathMatrix[foodCol[a]][b] = intialProb +  pathMatrix[foodCol[a]][b]
                       # pathMatrix[b][foodCol[a]] = intialProb + pathMatrix[b][foodCol[a]]
        else:
            for b in range(nestR, nestR+var):
                if(b<col):
                    if(b<row):
                         pathMatrix[nestR + b][nestC + b] = intialProb +  pathMatrix[nestR + b][nestC + b]

#combine both probabilities together
def totalProb1(row, col, otherProb, foodProb, totalProb):
    for i in range(row):
        for x in range(col):
            totalProb[i][x] = otherProb[i][x] + foodProb[i][x]


if __name__ == '__main__':

#variables to be used
    foodRow = []
    foodCol = []

##get user input
    row = int(input('Enter number of row: '))
    col = int(input('Enter number of col: '))
    intialProb= 1/(row*col)

#get the matrixes ready
    totalProb = [[0 for x in range(col)] for y in range(row)]
    pathMatrix = [[0 for x in range(col)] for y in range(row)]
    foodProb = [[0 for x in range(col)] for y in range(row)]
    otherProb = [[0 for x in range(col)] for y in range(row)]

    iter = int(input('Enter number of iteration: '))
    nestR = int(input('Enter nest row: '))
    nestC = int(input('Enter nest col: '))

    num = int(input('Enter number of location: '))

    #while loop for food locations
    while num != 0:
        fR = int(input('Enter food row: '))
        foodRow.append(fR)
        fC = int(input('Enter food col: '))
        foodCol.append(fC)
        num = num- 1


#loop for iterations :)
    for time in range(iter):
        # function call to food prob1
        foodProb1(intialProb,row, col, foodProb, nestR, nestC, foodRow, foodCol, time)
        #function call to update prob1
        updateProb(time,intialProb, row, col, otherProb, nestR, nestC, foodProb );
        totalProb1(row, col, otherProb, foodProb, totalProb)

        demo(totalProb)
        annotateGraph(nestR, nestC, foodRow, foodCol)
        #plt.title("Time is " + str(time + 1))
        if(time==30):
            plt.pause(10)


        plt.clf()
        plt.draw()