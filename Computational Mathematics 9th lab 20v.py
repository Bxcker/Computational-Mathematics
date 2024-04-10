import numpy as np
np.set_printoptions(linewidth=100, precision=5,suppress=True)



def main(A):
	
	A = np.array(A, float)
	B = np.zeros_like(A, float)
	T = np.zeros_like(A, float)
	y = np.zeros_like(A, float)
	x = np.zeros_like(A, float)
	o = np.zeros_like(A, float)
	n = len(A)

	for i in range(n):
		B[i,0] = A[i,0]
	for j in range(n):
		T[0,j] = A[0,j]/B[0,0]
	for k in range(1,n): #did a correction
		for i in range(k,n):
			B[i,k] = A[i,k]
			for m in range(k):
				B[i,k] = B[i,k] - B[i,m] * T[m,k]
		if k <= n-1:
			for j in range(k,n):
				T[k,j] = A[k,j]
				for m in range(k):
					T[k,j] = T[k,j] - B[k,m] * T[m,j]
				T[k,j] = T[k,j] / B[k,k]

	for i in range(n):
		for j in range(n):
			if j > i:
				y[i,j] = 0
			elif j == i:
				y[i,j] = 1 / B[i,i]
			elif j < i:
				for m in range(j, i):
					y[i,j] = y[i,j] - B[i,m] * y[m,j]
				y[i,j] = y[i,j] / B[i,i]

	for i in range(n-1, -1, -1):
		for j in range(n-1,-1,-1):
			if j < i:
				x[i,j] = 0
			elif j == i:
				x[i,j] = 1
			elif j > i:

				for m in range(i+1, j+1):
					x[i,j] = x[i,j] - T[i,m] * x[m,j]

	

	print(f"B:\n{B}")
	print(f"T:\n{T}")
	print(f"Y:\n{y}")
	print(f"X:\n{x}")
	print("")
	print(np.matmul(x,y))
	print("Для проверки")
	print(np.linalg.inv(A))

A = [[5,1,9,6,7,7],
	 [5,5,3,2,2,6],
	 [3,3,7,3,7,1],
	 [4,5,1,1,2,6],
	 [3,6,7,9,1,8],
	 [7,3,6,1,8,6]]

main(A)


