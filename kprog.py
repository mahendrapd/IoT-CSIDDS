import random
import math
nAttr = 21
SelectedF = 11
setF = math.ceil(SelectedF / 2)
setF = int(setF)
nCluster = 2
nClass = 2
def parsedata():
    print ("Hello Mahendra\n ->> Parse Data Set in two dimensional Array to use function")
    pf = open("distfinaldataset.txt")
    global List
    ColRange = SelectedF + 1
    #ColRange=nAttr
    List = pf.readlines()
    global element
    element = len(List)
    print("Number of samples : ", element)
    global a
    a = [[0 for j in range(ColRange)] for i in range(len(List))]
    for i in range(len(List)):
        strt = List[i].split(",")
        for j in range(ColRange):
            a[i][j] = strt[j]
            if(j < ColRange - 1):
                a[i][j] = float(a[i][j])
    List[:] = []
    pf.close()
    #wt.close()
    print("data parsing Process completed...")

def parsecenter():
    print ("Parse Cluster Center Data into two dimensional Array")
    cf = open("clustCenter.txt")
    global Listc
    Listc = cf.readlines()
    print(len(Listc))
    global c
    c = [[0 for j in range(SelectedF)] for i in range(nCluster)]
    for i in range(nCluster):
        strt = Listc[i].split(",")
        for j in range(SelectedF):
            c[i][j] = strt[j]
            c[i][j] = float(c[i][j])
    Listc[:] = []
    cf.close()
    print("data parsing Process completed...")

def KmeansClustering():
    parsedata()
    print ("Hello Mahendra \n ->> K-means clustering algorithm")
    wt = open("clustCenter.txt", "w")
    it = open("niteration.txt", "w")
    cCenter = [[0 for j in range(SelectedF)] for i in range(nCluster)]
    R = random.sample(range(0, element), nCluster)
    R.sort()
    #print(R)
    for i in range(nCluster):
        for j in range(SelectedF):
            cCenter[i][j] = a[R[i]][j]
    #print(cCenter)
    niter = 0
    t = 1
    while(t == 1):
        niter = niter + 1
        print(niter)
        cC = [[0 for j in range(SelectedF)] for i in range(nCluster)]
        clustSamp = [0 for i in range(nCluster)]
        for i in range(element):
            index = 0
            dist = 99999
            ecluD = [0 for r in range(nCluster)]
            for k in range(nCluster):
                for j in range(SelectedF):
                    ecluD[k] = ecluD[k] + (a[i][j] - cCenter[k][j])**2
                ecluD[k] = math.sqrt(ecluD[k])
                if(dist > ecluD[k]):
                    dist = ecluD[k]
                    index = k
            for j in range(SelectedF):
                cC[index][j] = cC[index][j] + a[i][j]
            clustSamp[index] = clustSamp[index] + 1
        for k in range(nCluster):
            for j in range(SelectedF):
                if(clustSamp[k] > 0):
                    cC[k][j] = round(float(cC[k][j] / clustSamp[k]), 2)
        if(cCenter == cC):
            for k in range(nCluster):
                for j in range(SelectedF):
                    wt.write(str(cC[k][j]))
                    if(j < SelectedF - 1):
                        wt.write(",")
                    else:
                        wt.write("\n")
            it.write("Number of iterations : ")
            it.write(str(niter))
            t = 0
        else:
            cCenter = cC
    print("Process completed ..")

def testkmeans():
    parsedata()
    parsecenter()
    rt = open("results.txt", "w")
    lt = open("labels.txt", "w")
    result = [[0 for j in range(nClass)] for i in range(nCluster)]
    label = [0 for r in range(nClass)]
    l = 0
    for i in range(element):
        index = 0
        ld = 0
        t = 0
        dist = 99999
        ecluD = [0 for r in range(nCluster)]
        for k in range(nCluster):
            for j in range(SelectedF):
                ecluD[k] = ecluD[k] + (a[i][j] - c[k][j])**2
            ecluD[k] = math.sqrt(ecluD[k])
            if(dist > ecluD[k]):
                dist = ecluD[k]
                index = k
        if(l == 0):
            label[l] = a[i][SelectedF]
            #result[index][l] += 1
            ld = l
            l = l + 1
            t = 1
        else:
            for s in range(nClass):
                if(a[i][SelectedF] == label[s]):
                    ld = s
                    t = 1
                    break
        if(t == 0):
            label[l] = a[i][SelectedF]
            ld = l
            l = l + 1
        result[index][ld] += 1
    print(label)
    for i in range(nClass):
        lt.write(str(label[i]))
    print(result)
    for i in range(nCluster):
        for j in range(nClass):
            rt.write(str(result[i][j]))
            if(j < nClass - 1):
                rt.write("\t")
            else:
                rt.write("\n")
    print("Process Completed ..")

#parsedata()
KmeansClustering()
testkmeans()

