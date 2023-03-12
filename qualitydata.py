import numpy as np
import pandas as pd


def quality_data(path):
    data = pd.read_csv(path)
    genenames = data.columns
    cellnums = data.values.shape[0]
    genenums = data.values.shape[1]
    zeronums=[]
    dropnames=[]
    for i in range(1, genenums):
        zeronum = np.sum(data.values[:, i] == 0)
        zeronums.append(zeronum)
        #不存在在95%以上细胞中不表达的基因
        if zeronum > 820:#90%不表达
            dropnames.append(genenames[i])

    print(dropnames)
    print(zeronums)
    data.drop(columns=dropnames,axis=1,inplace=True)
    data.to_csv("data90/dataquality.csv",index=False)


quality_data("data/cortex_svz_counts.csv")
