from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import numpy as np

#    t1 t2 t3 t4 t5
# u1  0, 1, 0, 0, 1
# u2  0, 0, 1, 1, 1
# u3  1, 1, 0, 1, 0
#

A =  np.array([[0, 1, 0, 0, 1], [0, 0, 1, 1, 1],[1, 1, 0, 1, 0]])
A_sparse = sparse.csr_matrix(A)

similarities = cosine_similarity(A_sparse)
print('pairwise dense output:\n {}\n'.format(similarities))

#also can output sparse matrices
similarities_sparse = cosine_similarity(A_sparse,dense_output=False)
print('pairwise sparse output:\n {}\n'.format(similarities_sparse))



def overallTrust(globalTrust, localTrust, b):
	ot = [0, 0, 

def globalTrust(reputation, vote, a):
	gt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(0, len(reputation)):
		gt[i] = a * reputation[i] + (1-a) * vote[i]
	return gt	
	

reputation = [0.233451, 0.432233, 0.603234, 0.872123, 0.004323, 0.187345, 0.912090, 0.598312, 0.000404, 0.390123]

vote = [10, 2, 0, 4, 100, 193, 233, 12, 46, 31]

a = 0.75
b = 0.5
globaltrust = globalTrust(reputation, vote, a)
#localtrust = localTrust()
#overall = overallTrust(globalTrust, localTrust, b)
#print(overall)

