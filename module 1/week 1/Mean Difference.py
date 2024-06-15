import math

def mean_difference_nth_root_error(y, y_hat, n, p):
    y_root_n = y ** (1/n)
    y_hat_root_n = y_hat ** (1/n)
    difference = abs(y_root_n - y_hat_root_n)
    loss = difference ** p
    return loss

y = 100
y_hat = 99.5
n = 2
p = 1

result = mean_difference_nth_root_error(y, y_hat, n, p)
print("Mean Difference of nth Root Error:", result)