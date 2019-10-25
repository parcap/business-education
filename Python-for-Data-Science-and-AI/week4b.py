import numpy as np
import matplotlib.pyplot as plt

# create a 1D numpy array
a = np.array([0, 1, 2, 3, 4])

print(type(a))
print(a.dtype)

# accessing elements of a numpy array
slice1 = a[1]
slice2 = a[1:3]

print(slice1)
print(slice2)

print(type(slice1))
print(type(slice2))

# array attributes
print(a.size)   # number of elements in the array
print(a.ndim)   # rank of the array
print(a.shape)  # tuple that returns the number of rows, columns in the array

# change the value of an element in an array
a[:3] = 100
a[0] = 75
a[1:3] = 250

print(a)

a[0:2] = 1000, 2000

print(a)

# basic operations
u = np.array([4, 1])
v = np.array([3, 2])

w = u + v
print(w)

y = 3 * w
print(y)

z = u * v
print(z)

d = np.dot(u, v)
print(d)

s = u + 1   # broadcasting
print(s)

sum_u = u.sum()
mean_u = u.mean()
max_u = u.max()

print(sum_u)
print(mean_u)
print(max_u)

x = np.array([0, np.pi / 2, np.pi])
y = np.sin(x)
print(x)
print(y)

ls = np.linspace(0, 2 * np.pi, 100)
sin_ls = np.sin(ls)
plt.plot(ls, sin_ls)


# create a 2D numpy array
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)

B = A[1, 2]
print(B)

C = A[1][2]
print(C)

D = A[0][0:2]
print(D)
print(type(D))

E = A[0, 0:2]
print(E)
print(type(E))

F = A[:]
print(F)

G = A + 1   # broadcasting
print(G)

H = np.sin(A)
print(H)

TP = A.T
print(TP)


X = np.array([[0, 1, 1], [1, 0, 1]])
Y = np.array([[1, 1], [1, 1], [-1, 1]])

print(X)
print(Y)

DP = np.dot(X,Y)
print(DP)