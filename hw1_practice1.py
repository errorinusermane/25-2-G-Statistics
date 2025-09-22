# latex: 수식 예쁘게 만들어주는 패키지임.

import numpy as np

a = np.arange(10)

a = np.array([2,0,-1])
b = np.array([1,3,4])
print(a@b)
np.inner(a,b)

A = np.array([[1,2,3,4],[3,2,1,0]])
A.ndim
A.shape
A.size

BB = np.arange(1,13)
BB
BB = BB.reshape(2,2,3)
BB[0]
BB[1]

CC = BB.reshape(3,2,2)
CC[0]
CC[1]
CC[2]

DD = BB.reshape(2,1,2,3)
DD[0]
DD[1]


A = np.arange(1,21)
B = A.reshape(4,5)
B[:2]
B[-2:]
B[1]

B[:, :2]
B[:, 1:2]

B[1:3, 1:3]
B[1:3, :][:,1:3]

B[[1,3],:][:,[1,3,4]]
B[[0,2,3],:][:,[0,-1]]

a = np.array([1,3,5,7])
a[1:2]
a[1]
