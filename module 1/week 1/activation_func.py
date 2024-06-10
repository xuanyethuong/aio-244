import math
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def sig_func(x):
    sig = 1/(1+math.exp(-x))
    print (f"Giá trị hàm sigmoid của {x} là: {sig}")
def reLU_func(x):
    if x <= 0:
        reLU_value = 0
    reLU_value = x
    print (f"Giá trị hàm reLU của {x} là: {reLU_value}")
def eLU_func(x,alpha):
    if x <= 0:
        eLU_value = alpha*(math.exp(x)-1)
    eLU_value = x
    print (f"Giá trị hàm eLU của {x} là: {eLU_value}")
def activation_func(x, alpha, act_name):
    if not is_number(x):
        print ("must be a number")
        return
    if act_name == 'sigmoid':
        return sig_func(x)
    elif act_name == 'relu':
        return reLU_func(x)
    elif act_name == 'elu':
        return eLU_func(x,alpha)
    else:
        raise ValueError("Tên hàm không hợp lệ")
alpha = 2
activation_func(3, alpha,'sigmoid')
activation_func(1, alpha,'relu')
activation_func(-1, alpha,'elu')