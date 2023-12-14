import numpy as np

# Find rank of a matrix
def MatrixRank2(A):
        M = np.array(A)
        shape = M.shape
        rows, cols = shape[0], shape[1]
        rank = cols if rows >= cols else rows
        for i in range(rank):
            if M[i,i] != 0:
                for j in range(rows):
                    if i != j:
                        M[j] = M[j]*M[i,i] - M[j,i] * M[i]
                # print(M)
            else:
                reduce = True
                for j in range(i + 1, rows):
                    if M[j,i] != 0:
                        M[i], M[j] = M[j], M[i].copy()
                        reduce = False
                        break
                if reduce:
                    rank -= 1
                    M[:,i] = M[:,rank]
                i -= 1

        return (rank)
