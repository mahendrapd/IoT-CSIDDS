import datetime
nAttr = 30
labelPosition=29
import random
import csv
def datetimenow():
    now = datetime.datetime.now()
    print (" Current date and time : ",now.strftime("%Y-%m-%d %H:%M:%S"))

def parsetext():
    datetimenow()
    print (" Hello Mahendra\n ->> Parse Data Set in List to use this function")
    global List
    global element
    pf=open("distfsdataset.txt")
    List = pf.readlines()
    element=len(List)
    print ("Number of Instance :",element)
    pf.close()

def parsedata():
    datetimenow()
    print (" Hello Mahendra\n ->> Parse Data Set in two dimensional Array to use this function")
    pf = open("dataset.txt")
    global List
    labelPosition=29
    ColRange=labelPosition+1
    List = pf.readlines()
    global element
    element=len(List)
    print(element)
    global a
    a=[ [0 for j in range(ColRange)] for i in range(len(List))]
    for i in range(len(List)):
        str=List[i].split(",")
        for j in range(ColRange):
            a[i][j]=str[j]
    List[:]=[]
    pf.close()

def csvwrite():
    #parsetext()
    parsedata()
    k=0
    p=0
    for i in range(element):
        if(a[i][labelPosition] == "normal\n"):
            a[i][labelPosition] = "normal"
            k = k + 1
        else:
            a[i][labelPosition] = "attack"
            p = p + 1
    List = a
    fields = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L',"Label"]
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(fields)
        writer.writerows(List)
    print(List[1])
    print(k,p)

def check():
    rows = [ ['Nikhil', 'COE', '2', '9.0\n'], 
         ['Sanchit', 'COE', '2', '9.1\n'], 
         ['Aditya', 'IT', '2', '9.3\n'], 
         ['Sagar', 'SE', '1', '9.5\n'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']]
    filename = "university_records.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)

def Datasetsplit():
    datetimenow()
    print ("Hello Mahendra\n ->> Split Data Set")
    parsetext()
    fp=open("mixeddataset.txt","w")
    rnum = random.sample(range(0,285734),285734)
    for i in range(285734):
        '''print(random.randint(0,331327))'''
        '''rnum=random.randint(0,331327)'''
        fp.write(List[rnum[i]])
    fp.close()
    print ("Process Completed...")
    
#parsetext()
#parsedata()
csvwrite()
#check()
#Datasetsplit()
