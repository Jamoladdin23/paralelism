from multiprocessing import Process, Manager# MULTIPROCESSING FOR, PEREMNOJIT MATRIC
import numpy as np# FOR TABLICNIX VIDOV DANNIX

def multiply_matrices(A, B, result, row):
    result[row] = [sum(A[row][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]


if __name__ == '__main__':
        # TABLICA DANNIX
    A = np.array([
        [1, 3, 5],      #TUT RYADOCHOK UMNAJAETSYA
        [2, 4, 6],
    ])

    B = np.array([
        [5, 3],         # NA STOLBCI
        [4, 2],
        [1, 6]
    ])

    with Manager() as manager:
        result = manager.list([None] * A.shape[0])
        processes = [Process(target=multiply_matrices, args=(A, B, result, i)) for i in range(A.shape[0])]


        for p in processes:
            p.start()

        for p in processes:
            p.join()


        result_matrix = np.array(result)
        print("Result:")
        print(result_matrix)

