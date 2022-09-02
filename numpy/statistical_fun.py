import numpy as np
## Generate random number from normal distribution

normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)

print(np.min(normal_array))

print(np.max(normal_array))

print(np.mean(normal_array))

print(np.median(normal_array))

print(np.std(normal_array))

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

print(np.max(arr, axis=1))
