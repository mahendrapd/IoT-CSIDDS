import datetime
nAttr = 30
labelPosition=29
import random
def datetimenow():
    now = datetime.datetime.now()
    print (" Current date and time : ",now.strftime("%Y-%m-%d %H:%M:%S"))

def parsetext():
    datetimenow()
    print (" Hello Mahendra\n ->> Parse Data Set in List to use this function")
    global List
    global element
    pf=open("distfinaldataset.txt")
    List = pf.readlines()
    element=len(List)
    print ("Number of Instance :",element)
    pf.close()

def Datasetsplit():
    datetimenow()
    print ("Hello Mahendra\n ->> Split Data Set")
    parsetext()
    fp=open("finaldata4.txt","w")
    #rnum = random.sample(range(0,199537),50000)
    p=150000
    #rangek = 50000
    for i in range(49537):
        #print(random.randint(0,331327))
        #rnum=random.randint(0,331327)
        fp.write(List[p])
        p = p + 1
    fp.close()
    print ("Process Completed...")
    
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
    
def isnumeric(s):
    '''returns True if string s is numeric'''
    return all(c in "0123456789.+-\n" for c in s) and any(c in "0123456789" for c in s)

def isConvertString2int(f):
    print(f)
    mSize=200
    exactSize=0
    #fptr.write("sequence number\t")
    #fptr.write(str(f))
    #fptr.write("\n")
    mString= [ 0 for r in range(mSize)]
    mInt=[0 for l in range(mSize)]
    for i in range(element):
        t=0
        if(exactSize==0):
            mString[exactSize]=a[i][f]
            mInt[exactSize]=exactSize
            a[i][f]=exactSize
            exactSize=exactSize+1
            t=1
        else:
            for k in range(exactSize):
                if(a[i][f]==mString[k]):
                    a[i][f]=mInt[k]
                    t=1
        if(t==0):
            mString[exactSize]=a[i][f]
            mInt[exactSize]=exactSize
            a[i][f]=exactSize
            exactSize=exactSize+1
    #for p in range(exactSize):
        #fptr.write(str(mString[p]))
        #if(p != exactSize-1):
            #fptr.write(",")
    #fptr.write("\n")
    #for q in range(exactSize):
        #fptr.write(str(mInt[q]))
        #if(q != exactSize-1):
            #fptr.write(",")
    #fptr.write("\n")

def isParseString():
    parsedata()
    print("Data conversion function string to integer")
    wt=open("data.txt","w")
    for m in range(nAttr-1):
        if(isnumeric(a[0][m])):
            print ("Ok")
        else:
            print ("String in processing of feature : ")
            isConvertString2int(m)
    for i in range(element):
        for j in range(nAttr):
            wt.write(str(a[i][j]))
            if(j != (nAttr - 1)):
                wt.write("\t")
    print("Process Completed ...")
    
def nordataset():
    parsedata()
    print (" Hello Mahendra\n ->> Normalized data set to use this function")
    wt=open("normdata.txt","w")
    mint=open("minval.txt","w")
    maxt=open("maxval.txt","w")
    for j in range(nAttr-1):
        maxx=0
        miny=90000
        for i in range(element):
            p=isinstance(a[i][j], float)
            if(isnumeric(a[i][j]) or p):
                a[i][j] = float(a[i][j])
            else:
                a[i][j] = 0
            if(a[i][j] == -1):
                a[i][j] = 0
            if(maxx < a[i][j]):
                maxx = a[i][j]
            if(miny > a[i][j]):
                miny = a[i][j]
        if(maxx > miny):
            for i in range(element):
                a[i][j] = round((float(a[i][j]-miny)/(maxx-miny)),2)
        else:
            for i in range(element):
                a[i][j] = 0.0
        mint.write(str(miny))
        mint.write("\n")
        maxt.write(str(maxx))
        maxt.write("\n")
        print("process continue : ", j, miny, maxx)
    for i in range(element):
        for j in range(nAttr):
            wt.write(str(a[i][j]))
            if(j!=(nAttr-1)):
                wt.write(",")
    wt.close()
    print ("nordataset process complete..")
    
def writeintotext():
    datetimenow()
    print ("Hello Mahendra\n ->> Generate Distinct Data Set")
    parsetext()
    fp=open("distfinaldataset.txt","w")
    ele=element-1
    p=0
    for i in range(ele):
        p=p+1
        notdup=0
        k=i+1
        for j in range(k,element):
            if(List[i]==List[j]):
                notdup=1
                break
        if(notdup == 0):
            fp.write(List[i])
        if(p==5000):
            p=0
            print ("Remaining : ", element-i)
    fp.write(List[ele])
    fp.close()
    print ("Process Completed...")
    
def newAttProbCal():
    datetimenow()
    print (" Hello Mahendra\n ->> New approach to calculate attribute probability to use this function")
    parsedata()
    Theta=101
    MaxClass=6
    global numberOfClass
    #ColRange=labelPosition+1
    ncname=[0 for i in range(MaxClass)]
    pIndex=0
    for i in range(element):
        ltest=0
        if(pIndex==0):
            ncname[pIndex]=a[i][labelPosition]
            pIndex=pIndex+1
        else:
            for l in range(pIndex):
                if(a[i][labelPosition]==ncname[l]):
                    ltest=1
                    break
            if(ltest==0):
                ncname[pIndex]=a[i][labelPosition]
                pIndex=pIndex+1
                numberOfClass=pIndex
    
    #findelement()
    pt=open("attprob.txt","w")
    #ncname=["normal\n","DoS\n","U2R\n","R2L\n","Probe\n"]
    ec=[0 for i in range(numberOfClass)]
    aprob=[0 for i in range(labelPosition)]
    aev=[0 for i in range(Theta)]
    for j in range(labelPosition):
        true=1
        p=0
        mf=0
        for i in range(element):
            if(p==0):
                aev[p]=a[i][j]
                p=p+1
                true=0
            else:
                for k in range(p):
                    if(aev[k]==a[i][j]):
                        true=0
                        break
                    true=1
            if(true==1):
                aev[p]=a[i][j]
                p=p+1
        ne=0
        for m in range(p):
            ec=[0 for i in range(numberOfClass)]
            for i in range(element):
                if(aev[m]==a[i][j]):
                    for k in range(numberOfClass):
                        if(ncname[k]==a[i][labelPosition]):
                            ec[k]=1
                            break
            e=0
            for k in range(numberOfClass):
                if(ec[k]==1):
                    e=e+1
            if(e==numberOfClass):
                ne=ne+1
            else:
                mf=mf+float(e)/numberOfClass
        if(p==ne):
            aprob[j]=0
        else:
            aprob[j]=1-(float(1)/2)*((float(ne)/p)+(float(mf)/(p-ne)))
        print (j,aprob[j])
        pt.write(str(aprob[j]))
        pt.write("\n")
    print ("Process Completed...")
    
def arrorder():
    datetimenow()
    print (" Hello Mahendra\n ->> Arrange Attributes based on probability to use this function")
    pf = open("attprob.txt")
    wt = open("arorder.txt","w")
    #labelPosition=12
    arr = pf.readlines()
    ci=[0 for i in range(labelPosition)]
    ad=[-1 for i in range(labelPosition)]
    for i in range(labelPosition):
        arr[i]=float(arr[i])

    for i in range(labelPosition):
        x=0
        k=0
        true=1
        for j in range(labelPosition):
            if(x<=arr[j] and ci[j]==0 and arr[j]>0):
                x=arr[j]
                k=j
                true=0 
        if(true==0):
            ci[k]=1
            ad[i]=k        
    pf.close()
    for i in range(labelPosition):
        if(ad[i]>-1):
            wt.write(str(ad[i]))
            wt.write("\n")
            print (i,ad[i])            
    print ("array order Process Complete..")
    
def storefun():
    datetimenow()
    print (" Hello Mahendra\n ->> Arrange and make data set based on probability values")
    parsedata()
    #ColRange=labelPosition+1
    at=open("arorder.txt")
    ct=open("finaldataset.txt","w")
    arord=at.readlines()
    lenght=len(arord)
    print ("Length of Index : ", lenght)
    #Range=lenght-1
    for i in range(lenght):
        arord[i]=int(arord[i])
    for i in range(element):
        for j in range(lenght):
            ct.write(a[i][arord[j]])
            ct.write(",")
        ct.write(a[i][labelPosition])
        '''ct.write("attack\n")'''
    print ("storefun() Process Complete..")
    
def parsefinaldata():
    datetimenow()
    print ("Parse final DataSet in two dimensional Array to use this function")
    pf = open("distfinaldataset.txt")
    at = open("arorder.txt")
    alist = at.readlines()
    global lPosition
    lPosition=len(alist)
    global ColRange
    ColRange=lPosition+1
    print("Number of features : ",lPosition)
    global List
    List = pf.readlines()
    global element
    element=len(List)
    print("Number of Samples : ", element)
    global a
    a=[ [0 for j in range(ColRange)] for i in range(len(List))]
    for i in range(len(List)):
        str=List[i].split(",")
        for j in range(ColRange):
            a[i][j]=str[j]
    List[:]=[]
    pf.close()
    
def adhocbrs():
    print("Adhoc Bayesian-Rough Set function")
    parsefinaldata()
    print("<------ Program execution is started ------>")
    wt=open("result.txt","w")
    wt.write("\nNumber of samples : ")
    wt.write(str(element))
    wt.write("\nNumber of features : ")
    wt.write(str(lPosition))
    #print("Label position and Colrange : ",lPosition,ColRange)
    numberOfClass = 2
    theta = 0.9*lPosition
    theta = int(theta)
    #----------------------------------------------------------------------------------
    cname = [0 for c in range(numberOfClass)]
    cdata = [0 for d in range(numberOfClass)]
    index = 0
    for k in range(element):
        testp = 0
        if(index == 0):
            cname[index] = a[k][lPosition]
            cdata[index] = cdata[index] + 1
            index = index + 1
        else:
            for b in range(index):
                if(a[k][lPosition] == cname[b]):
                    cdata[b] = cdata[b] + 1
                    testp = 1
                    break
            if(testp == 0):
                cname[index] = a[k][lPosition]
                cdata[index] = cdata[index] + 1
                index = index + 1
    #-------------------------------------------------------------------------------------             
    cm=[ [0 for j in range(numberOfClass)] for i in range(numberOfClass)]
    nfold = 5
    for f in range(nfold):
        tData=[0 for i in range(numberOfClass)]
        testSample=0
        trainSample=0
        for i in range(element):
            if(i%nfold != f):
                for q in range(numberOfClass):
                    if(a[i][lPosition] == cname[q]):
                        tData[q] = tData[q] + 1
                trainSample = trainSample + 1         
        t = 0
        while(1):
            indt = t*nfold+f
            if(indt<element):
                amb = 0
                mclass = 0
                probD = [ [0 for l in range(lPosition)] for m in range(numberOfClass)]
                for i in range(element):
                    if(i%nfold != f):
                        simC = 0
                        cindex = 0
                        for q in range(numberOfClass):
                            if(a[i][lPosition] == cname[q]):
                               cindex = q 
                        for j in range(lPosition):
                            if(a[i][j] == a[indt][j]):
                                probD[cindex][j] = probD[cindex][j] + 1
                                simC = simC + 1
                        if(simC > theta):
                            if(mclass == 0):
                                mclass = a[i][lPosition]
                            else:
                                if(mclass != a[i][lPosition]):
                                    amb = 1
                if(mclass == 0 or amb == 1):
                    probB = 0
                    pindex = 0
                    gindex = 0
                    #val = [0 for c in range(numberOfClass)]
                    for z in range(numberOfClass):
                        if(a[indt][lPosition] == cname[z]):
                            gindex = z
                    for v in range(numberOfClass):
                        pr = 1
                        if(tData[v] > 0):
                            for j in range(lPosition):
                                pr = pr*float(probD[v][j])/tData[v] 
                            prob = float(tData[v])/cdata[v]
                            prob=prob*pr  
                            #val[v] = prob
                        if(probB < prob):
                            probB = prob
                            pindex = v
                    #print(probB,"\t",gindex,"\t",pindex)
                    cm[pindex][gindex] = cm[pindex][gindex] + 1
                    #print(probD)
                    #print(val)
                else:
                    for r in range(numberOfClass):
                        if(a[indt][lPosition] == cname[r]):
                            cm[r][r] = cm[r][r] + 1
                testSample = testSample + 1
            else:
                break
            t = t + 1 
        print("Completed fold :",f)
        #print(cname,tData,cdata)
        #print("Testing Sample =",testSample,"\tTraining Sample =",trainSample)
    wt.write("\n\nConfusion Matrix\n")
    for i in range(numberOfClass):
        for j in range(numberOfClass):
            wt.write(str(cm[i][j]))
            wt.write("\t")
        wt.write("\n")
    wt.write("\nLabels and samples are : \n")
    for i in range(numberOfClass):
        wt.write(str(cdata[i]))
        wt.write("\t")
        wt.write(cname[i])
        wt.write("\n")
    wt.close()
    print(cm)
    print("<-------- Program execution completed ------>")
    #print(cname,cdata)
def findelement():
    '''datetimenow()'''
    parsedata()
    print(" Hello Mahendra\n ->> Check data set attributes details to use this function")
    labelPosition=30
    ColRange=labelPosition+1
    point=open("depend.txt","w")
    np=open("ced.txt","w")
    b=[0 for i in range(element)]
    global ce
    ce=[0 for j in range(labelPosition)]
    t=0
    for j in range(labelPosition):
        j=j+1
        p=0
        for i in range(element):
            true=1
            if (p==0):
                b[p]=a[i][j]
                p=p+1
                true=0
            else:
                for k in range(p):
                    if(b[k]==a[i][j]):
                      true=0
                      break
                    else:
                        true=1
            if(true==1):
                b[p]=a[i][j]
                p=p+1
        
        point.write("sequence id : ")
        point.write(str(j))
        point.write("\n")
        for m in range(p):
            point.write(b[m])
            point.write(" ")
        point.write("\n")
        point.write("Total : ")
        
        ce[t]=p
        t=t+1
        
        point.write(str(p))
        point.write("\n")
        print (j,p)

    point.close()
    for j in range(t):
        np.write(str(ce[j]))
        np.write("\n")
    np.close() 
    print("Find element process Complete...")
    
#parsetext()
#parsedata()
#isParseString()
#nordataset()
#writeintotext()
#newAttProbCal()
#arrorder()
#storefun()
adhocbrs()
#findelement()
#Datasetsplit()
