'''
by duyifan ID: 24215428
Chapter 2 Problems 4 LPM
'''
import numpy as np

num_of_delay = 3 # 需修改
longest_path_matrix = np.zeros((num_of_delay,num_of_delay,num_of_delay))
longest_path_matrix[:,:,0] = np.array([
                                    [ 4, 0,-1],
                                    [ 5,-1, 0],
                                    [ 5,-1,-1],
                                    ])
# 需修改
K_set = np.arange(num_of_delay)
iteration_bound = 0 # initialize the iteration bound
# print (K_set)

for d in range(1, num_of_delay):
    for i in range(num_of_delay):
        for j in range(num_of_delay):
            for k in K_set:
                if longest_path_matrix[i,k,0] == -1 or longest_path_matrix[k,j,d-1] == -1:
                    continue
                else:
                    longest_path_matrix[i,j,d] = max(
                                                    -1,
                                                    (longest_path_matrix[i,k,0]+longest_path_matrix[k,j,d-1]),
                                                    longest_path_matrix[i,j,d]
                                                    )

# print(longest_path_matrix[:,:,3])

for d in range(num_of_delay):
    for i in range(num_of_delay):
        if longest_path_matrix[i,i,d] == 0:
            continue
        else:
            iteration_bound = max(iteration_bound, longest_path_matrix[i,i,d]/(d+1))

print('iteration_bound is:',iteration_bound)