import numpy as np

#Generating the binary 3D matrices
num1=10
size = (num1, 6, 4, 4)
prob_0 = 0.3 # 30% of zeros
prob_1 = 1 - prob_0 # 70% of ones

P = np.random.choice([0, 1], size=size, p=[prob_0, prob_1])


#Checking matrices to be unique
unique_set=[]
for idx in P:
    if not any(np.array_equal(idx, other_idx) for other_idx in unique_set):
        unique_set.append(idx)

with open('my_matricies.csv', 'w+') as main_matricies:
    for idx in unique_set:
        main_matricies.write('%s\n' % idx)
