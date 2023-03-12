from counts0 import *
original = readData("data\cortex_svz_counts.csv")
counts ,index= count4each(original)
sumexpression=sumExinEach(index,original)
getZeroExpression(sumexpression,"data/")
print(sumexpression.shape)

original = readData("data90/dataquality.csv")
counts ,index= count4each(original)
sumexpression=sumExinEach(index,original)
getZeroExpression(sumexpression,"data90/")
print(sumexpression.shape)
