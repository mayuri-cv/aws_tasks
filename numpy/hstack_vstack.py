import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])
print(f)
print(g)
print("\n Horizontal append",np.hstack((f,g)))

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(h1)
print(h2)
print(np.hstack((h1,h2)))

####vstack

f = np.array([1,2,3])
g = np.array([4,5,6])
print(f)
print(g)
print("\n Vertical append",np.vstack((f,g)))

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(v1)
print(v2)
print(np.vstack([v1,v2,v1,v2]))