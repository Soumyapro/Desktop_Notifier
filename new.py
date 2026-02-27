import numpy as np

arr1 = np.arange(5)
arr2 = np.arange(5,10)

print(np.stack((arr1,arr2),axis=0)) #horizontal stacking
print(np.stack((arr1,arr2),axis=1)) #vertical stacking