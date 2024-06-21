import torch
import torch.nn as nn
import torch.nn.functional as F

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)  # subtract max for numerical stability
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

# Example usage:
if __name__ == '__main__':
    x = torch.tensor([1 , 2, 3])

    softmax = Softmax()
    result = softmax(x)
    print(f"Softmax result: {result}")

    softmax_stable = SoftmaxStable()
    result_stable = softmax_stable(x)
    print(f"SoftmaxStable result: {result_stable}")