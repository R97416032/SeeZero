import numpy as np
a=[1,1,1,1,3,4]
b=np.array(a).reshape(2,3)
print(np.sum(b[:,0]==0))