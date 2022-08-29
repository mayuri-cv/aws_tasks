import numpy as np

val = np.array([1,2,3])
print(val)
val = np.array([(1,2,3),(4,5,6)])
print(val)

x = np.linspace(0,2,9)
print(x)
y = np.zeros((3,4,5))
print(y)
z = np.ones((3,4,5))
print(z)

print(np.random.random((5,5)))

print(np.random.rand(3))

print(np.random.rand(3,5))

# Random Integer values
print(np.random.randint(-4,3, size=(3,3)))

print(np.arange(1, 11))

print(np.arange(1, 14, 4))

e  = np.array([(1,2,3), (4,5,6)])
print(e)
new = e.reshape(3,2)
print(new)

# add a scalar to a 1-d array
x = np.arange(5)
print('x:  ', x)
print('x+1:', x + 1, end='\n\n')

y = np.random.uniform(size=(2, 5))
print('y:  ', y,  sep='\n')
print('y+1:', y + 1, sep='\n')

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)

print(after.flatten())

