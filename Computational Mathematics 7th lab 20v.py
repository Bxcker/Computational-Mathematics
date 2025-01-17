import numpy as np


def iteration(A,C):
	k = 0
	e = 0.001
	A = np.array(A, dtype=float)
	X = np.zeros_like(C, float)
	XX = np.zeros_like(C, dtype= float)
	C = np.array(C, dtype=float)
	
	

	
	n = len(C)
	print("Халецкий:")
	while True:
		k += 1
		for i in range(n):
			XX[i] = C[i]
			for j in range(n):
				if j < i:
					XX[i] = XX[i] - A[i,j] * XX[j]
				else:
					if j > i:
						XX[i] = XX[i] - A[i,j] * X[j]

			XX[i] = XX[i] / A[i,i]

		check = 0
		for i in range(n):
			if abs(X[i] - XX[i]) < e:
				check += 1

			X[i] = XX[i]
		print(X)

		if check == n:
			break





def gssjrdn(A,C):
	a = A
	b = C
	a = np.array(a,dtype=float)
	b = np.array(b,dtype=float)
	n = len(b)

	#main loop 
	for k in range(n):
		#partial pivoting
		if np.fabs(a[k,k]) < 1.0e-12:
			for i in range(k+1,n):
				if np.fabs(a[i,k]) > np.fabs(a[k,k]):
					for j in range(k,n):
						a[k,j],a[i,j] = a[i,j],a[k,j]
					b[k],b[i] = b[i],b[k]
					break
		#Division of the pivot row
		pivot = a[k,k]
		for j in range(k,n):
			a[k,j] /= pivot
		b[k] /= pivot
		#Elimiination loop
		for i in range(n):
			if i == k or a[i,k] == 0:continue
			factor = a[i,k]
			for j in range(k,n):
				a[i,j] -= factor * a[k,j]
			b[i] -= factor * b[k]
	print("Проверка по методу Жордана-Гаусса")
	print(b)
	print("")


A = [[31,-4,6,-3,6],
	 [2,34,-4,7,-4],
	 [-7,9,29,5,-3],
	 [3,-4,4,25,0],
	 [6,-1,1,-8,34]]

C = [36,70,99,58,32]

iteration(A,C)
gssjrdn(A,C)