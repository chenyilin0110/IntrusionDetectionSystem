import numpy as np
import sys

algorithm = sys.argv[1]
dataset = sys.argv[2]
categories = sys.argv[3]

if dataset == "KDD99":
    # f = open('src/Plot/' + dataset + '/' + categories + 'class/' + dataset + '_' + categories + 'class_recall_Avg.txt', "a")
    # data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'accuracyprecisionrecall_' + categories + '.txt', delimiter=' ')
    # f.write(str(data[2]))
    # f.write(' ')
    # f.close()
    print("H")
else:
    # f = open('src/Plot/' + dataset + '/' + categories + 'class/' + dataset + '_' + categories + 'class_recall_Avg.txt', "a")
    # data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'accuracyprecisionrecall_' + categories + '.txt', delimiter=' ')
    # f.write(str(data[2]))
    # f.write(' ')
    # f.close()
    # Test-21
    f = open('src/Plot/' + dataset + '/' + categories + 'class/' + dataset + '_' + categories + 'class_recall_Avg-21.txt', "a")
    data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'accuracyprecisionrecall_' + categories + '-21.txt', delimiter=' ')
    f.write(str(data[2]))
    f.write(' ')
    f.close()