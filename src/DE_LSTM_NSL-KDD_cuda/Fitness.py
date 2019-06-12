import numpy as np
from neuralnetwork import LSTM
import torch.optim as optim
import torch.nn as nn
import torch
from accuracyfunction import accuracy
import time
def fitness(data, hiddenLayer, outputLayer, epoch, batchSize, train_noStringTemp_X, x_train_tensor, y_train_tensor, x_test_tensor, y_test_tensor):
    # bulid lstm
    lstm = LSTM(np.size(train_noStringTemp_X,1), int(outputLayer), data[0].tolist())
    lstm.cuda()
    # set optimizer and lossFunction
    optimizer = optim.RMSprop(lstm.parameters(), lr=0.05)
    lossFunction = nn.CrossEntropyLoss()

    # split batch
    batch_train_dataset = torch.utils.data.TensorDataset(x_train_tensor, y_train_tensor)
    train_loader = torch.utils.data.DataLoader(batch_train_dataset, batch_size=batchSize, shuffle=False)

    # traning
    for eachepoch in range(int(epoch)):
        h = torch.Tensor(1, int(batchSize), data[0].tolist()).zero_() # hiddenLayerNumber, batchSize, hiddenSize
        c = torch.Tensor(1, int(batchSize), data[0].tolist()).zero_()
        for step, (batch_x, batch_y) in enumerate (train_loader):
            batch_x = batch_x.view(1, -1, np.size(train_noStringTemp_X, 1)) # seq_len batch_size input_dim
            if len(batch_x[0]) != int(batchSize):
                h = h.detach().cpu().numpy()
                c = c.detach().cpu().numpy()
                h = h[:,:len(batch_x[0]),:]
                c = c[:,:len(batch_x[0]),:]
                h = torch.from_numpy(h)
                c = torch.from_numpy(c)
            y_prediction, (h,c) = lstm(batch_x.cuda(), h.cuda(), c.cuda())
            y_prediction = y_prediction.view(np.size(batch_x.numpy(), 1), -1) # reshape from 3 dimention to 2 dimention
            loss = lossFunction(y_prediction, batch_y.cuda())
            optimizer.zero_grad()# clean optimizer
            loss.backward(retain_graph=True)# calculate new parameters
            optimizer.step()# update parameters
    h = torch.Tensor(1, len(x_test_tensor), data[0].tolist()).zero_()
    c = torch.Tensor(1, len(x_test_tensor), data[0].tolist()).zero_()

    x_test = x_test_tensor.view(1, -1, np.size(train_noStringTemp_X, 1))
    y_test_predic, _ = lstm(x_test.cuda(), h.cuda(), c.cuda())
    pred = y_test_predic.detach().cpu().numpy()
    pred = pred.reshape(-1, int(outputLayer))
    y_test_list_predic = np.argmax(pred, axis=1)
    
    accuracyvalue = accuracy(y_test_tensor, y_test_list_predic)
    return accuracyvalue, lstm