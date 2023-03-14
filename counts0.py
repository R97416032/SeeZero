import numpy as np
import pandas as pd


def readData(path):
    data = pd.read_csv(path)
    genenames = data.columns
    f = open("data/genenames.txt", "w")
    for name in genenames:
        f.write(name + '\n')
    f.close()
    return data


def count4each(data):
    #因为有11个类别和1个未分类，需要对现有的标签进行类别修改
    #这里读取美俄个类别对应的标号
    f = open("clusterindex.txt")
    lines = f.readlines()
    f.close()
    clusterindex = []
    for line in lines:
        temp1 = line.strip("\n")
        temp2 = temp1.split(',')
        temp2 = [int(i) for i in temp2]
        clusterindex.append(temp2)
    counts = np.zeros(len(clusterindex))
    eachindex = [[] for i in range(len(counts))]

    for i in range(data.values.shape[0]):
        for index,j in enumerate(clusterindex):
            if data.values[i, 0] in j:
                eachindex[index].append(i)
                counts[index] += 1
                break
    f = open("data/eachnum.txt", "w")
    for count in counts:
        f.write(str(int(count)) + '\n')
    f.close()
    return counts, eachindex
def sumExinEach(index,data):
    sumexpression=np.ndarray(shape=(len(index),data.shape[1]))
    for i in range(1,len(index)):
        sumexpression[i]=np.sum(data.values[index[i]],axis=0)
    return sumexpression

def getZeroExpression(sumexpression,path):
    f = open("data/genenames.txt", "r")
    genenames=f.read().splitlines()
    genenames=np.array(genenames)
    zeroineach=[[]for i in range(sumexpression.shape[0])]
    for i in range(1,sumexpression.shape[0]):
        temp=genenames[np.argwhere(sumexpression[i]==0)].flatten()
        temp=temp.tolist()
        zeroineach[i]=[x for x in temp]
    nzeroinezch=[len(i) for i in zeroineach]
    f = open(path+"nzeroineach.txt", "w")
    for num in nzeroinezch:
        f.write(str(num) + '\n')
    f.close()
    uniqugenenames=[[]for i in range(len(zeroineach))]
    for i in range(1,len(zeroineach)):
        cur_gene=zeroineach[i]
        other=[a for x in zeroineach if x!=zeroineach[i] for a in x]
        uniqugenenames[i]=list((set(cur_gene)-set(other)))
    f = open(path+"unique/uniquezeroineach.txt", "w")
    for gene in uniqugenenames:
        f.write(str(gene)+ '\n')
    f.close()
    f = open(path+"unique/nuniquezeroineach.txt", "w")
    for gene in uniqugenenames:
        f.write(str(len(gene)) + '\n')
    f.close()
