'''
by duyifan ID: 24215428
Chapter 2 Problems 3 MCM
'''
import numpy as np

num_of_delay = 6 # 需修改
longest_path_matrix = np.zeros((num_of_delay,num_of_delay))
longest_path_matrix = np.array([
                                [4, 4,-1, 4, 4,-1],
                                [-1,-1, 0,-1,-1,-1],
                                [ 4, 4,-1, 4, 4,-1],
                                [-1,-1,-1,-1,-1,-1],
                                [-1,-1,-1,-1,-1, 0],
                                [-1,-1,-1,-1,-1,-1]
                                ])
# 借用LPM的矩阵，此处-1表明无路径 需修改
Gd_bar_weights = longest_path_matrix * -1

f_vertor = np.zeros((num_of_delay,num_of_delay+1))
inf = float('inf')
f_vertor[:,0] = np.array([0,inf,inf,inf,inf,inf]) # 需修改
# print('initial f_vertor is \n:',f_vertor)

for j_f in range(1, num_of_delay+1):
    for i_f in range(num_of_delay):
        for k in range(num_of_delay):
            if Gd_bar_weights[k,i_f] == 1:
                continue
            else:
                f_vertor[i_f,j_f] = min(
                                        f_vertor[k,j_f-1]+Gd_bar_weights[k,i_f],
                                        f_vertor[i_f,j_f]
                                        )

# print('f_vertor is :\n',f_vertor)

result_1 = np.zeros((num_of_delay,num_of_delay))
for i in range(num_of_delay):
    for m in range(num_of_delay):
        result_1[i,m] = (f_vertor[i,num_of_delay] - f_vertor[i,m]) / (num_of_delay-m)

# print('result_1 is :\n',result_1)

max_result_1 = np.max(result_1, axis=1)
iteration_bound = np.min(max_result_1)*(-1)

print('iteration_bound is:',iteration_bound)


