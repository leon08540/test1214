import numpy as np
from typing import List

def Determinant(A:List[List]) -> float:
  shape = A.shape
  if len(shape) < 2:
    raise ValueError("Array must be at least two-dimensional for this calculation")
  elif shape[0] != shape[1] or shape[0] < 2:
    raise ValueError("Can only calculate a determinant for a square matrix")
  return DetCalc(A)

def DetCalc(A:List[List]) -> float:
  det = 0
  if (len(A)>2):
    sign = -1
    for i in range(len(A)):
      sign *= -1
      det += A[0,i]*sign*DetCalc(np.delete(np.delete(A,0,0),i,1))
    return det
  else:
    return A[0,0]*A[1,1] - A[1,0]*A[0,1]



A = np.array([[3.0, 7,-5], [8, 1, 0], [3,3,2]])
D = np.linalg.det(A)
print(A)
print(D)
print(Determinant(A))
