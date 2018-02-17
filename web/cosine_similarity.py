from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import numpy as np

# input from LDA.py
#    t1 t2 t3 t4 t5
# u1  0, 1, 0, 0, 1
# u2  0, 0, 1, 1, 1
# u3  1, 1, 0, 1, 0
#

A =  np.array([[0, 1, 0, 0, 1], [0, 0, 1, 1, 1],[1, 1, 0, 1, 0]])
A_sparse = sparse.csr_matrix(A)

similarities = cosine_similarity(A_sparse)
print('pairwise dense output:\n {}\n'.format(similarities))

similarities_sparse = cosine_similarity(A_sparse,dense_output=False)
print('pairwise sparse output:\n {}\n'.format(similarities_sparse))


