import numpy as np
filepath =  "../resources/data.txt"
filedata = np.genfromtxt(filepath, delimiter=',')
filedata = filedata.astype('int32') # you can also change type to 'int64'
print(filedata)

print(filedata>50)

print(np.any(filedata > 50, axis = 0))
