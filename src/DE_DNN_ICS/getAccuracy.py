import numpy as np
import sys

algorithm = sys.argv[1]
dataset = sys.argv[2]
datasetNumber = sys.argv[3]
run = sys.argv[4]

# copy acc to other file 2 categories
for i in range(int(datasetNumber)):
    for j in range(int(run)):
        data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_2-' + str((i+1)) + '-' + str(j+1) + '.txt', delimiter='\n')
        print(data[-1])

# copy acc to other file 3 categories
for i in range(int(datasetNumber)):
    for j in range(int(run)):
        data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_3-' + str((i+1)) + '-' + str(j+1) + '.txt', delimiter='\n')
        print(data[-1])

# copy acc to other file multi categories
for i in range(int(datasetNumber)):
    for j in range(int(run)):
        data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_41-' + str((i+1)) + '-' + str(j+1) + '.txt', delimiter='\n')
        print(data[-1])