import torch

a = torch.tensor([1.0, 2.0, 5.0])
a.dtype

b = torch.tensor([1.0, 2.0, 5.0])
b.dtype
b = b.type(torch.float64)
b.dtype

d = a+b
d.dtype
c = torch.tensor([1,2,3])
c.dtype

e = a+c
e.dtype

A = torch.tensor([[1,2,3,4,], [3,2,1,0]])
A.dtype
A = A.type(torch.int32)
A.dtype

A.ndim
A.shape

D = torch.diag([3,2,5])
D = torch.diag(torch.tensor([3,2,5]))
D

