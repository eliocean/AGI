import torch
from torch import nn
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

Res_list = []

num_inputs, num_outputs, num_hiddens = 784, 10, 1
for w1_param in range(1, 1000, 5):
    for w2_param in range(1,1000,5):
        # W1 = nn.Parameter(torch.randn(num_inputs, num_hiddens, requires_grad=True) * 0.01)
        W1 = torch.Tensor(num_inputs, num_hiddens).fill_(w1_param) * 0.00001
        W1.requires_grad = True
        b1 = nn.Parameter(torch.zeros(num_hiddens, requires_grad=True))

        # W2 = nn.Parameter(torch.randn(num_hiddens, num_outputs, requires_grad=True) * 0.01)
        W2 = torch.Tensor(num_hiddens, num_outputs).fill_(w2_param) * 0.00001
        W2.requires_grad = True
        b2 = nn.Parameter(torch.zeros(num_outputs, requires_grad=True))
        params = [W1, b1, W2, b2]


        def relu(X):
            a = torch.zeros_like(X)
            return torch.max(X, a)


        def net(X):
            X = X.reshape((-1, num_inputs))
            H = relu(X @ W1 + b1)  # 这里“@”代表矩阵乘法
            return (H @ W2 + b2)


        loss = nn.CrossEntropyLoss(reduction='none')

        num_epochs, lr = 20, 0.1
        updater = torch.optim.SGD(params, lr=lr)
        train_loss, train_acc, test_acc = d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, updater)
        Res_list.append([train_loss, train_acc, test_acc])


print(Res_list)