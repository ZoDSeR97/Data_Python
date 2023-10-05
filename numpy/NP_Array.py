# Traditional import line
import numpy as np

# Creating 1d array or vector
a = np.array([1, 2, 3, 4, 5, 6])
print(f"\nVector shape: {a.shape}") # (6,) Base on Numpy document illustrate, this is a 6x1 vector
# There’s no difference between row and column vectors
print(a) # Console will print it as 1d array however
print(a[0])

# Creating a matrix
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"\nMatrix shape: {a.shape}") # (3, 4) an array with two dimensions refers as a matrix.
print(a)

# Creating a tensor
a = np.zeros((2,3,4)) # Creating a tensor fill with zeros
print(f"\nTensor shape: {a.shape}") # (2, 3, 4) for 3-D or higher dimensional arrays, the term tensor is also commonly used.
print(a) # At this point just give up on printing array for visualization

# Sorting Vector
a = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(f"\n{np.sort(a)}") # Returning sorted version of a
print(a)

# Concatenate 2 Vectors
b = np.array([9, 10, 11, 12])
print(f"\n{np.concatenate((a,b))}") # Return a combine version of a and b
print(f"{np.sort(np.concatenate((a,b)))}") # Return sorted combine version of a and b

# Reshape
c = np.ones((3,2,4)) # Creating a tensor fill with ones
print(f"\nTensor shape: {a.shape}")  
print(f"{np.reshape(c, newshape=(2,3,4), order='C')}") # order: C means to read/write the elements using C-like index order
print(f"Tensor shape: {a.shape}")

# Covert a Vector into Matrix
a = np.arange(6) # Creating a sorted Vector
b = a[np.newaxis, :] # Convert column vector to row vector
print(b) # Techically as illustrated by Console, it is now 2D which is a Matrix
c = a[:, np.newaxis] # Convert column vector to column vector
print(c)
b = np.expand_dims(a, axis=1) # Same thing as previous: Convert column vector to row vector
c = np.expand_dims(a, axis=0) # Same thing as previous: Convert column vector to column vector