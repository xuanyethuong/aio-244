#Viết function thực hiện đánh giá classification model bằng F1-Score
'''
• Precision = TP/(TP + FP)
• Recall = TP/(TP + F N)
• F1-score = 2 ∗ ((P recision ∗ Recall)/(P recision + Recall))
• Input: function nhận 3 giá trị tp, fp, fn
• Output: print ra kết quả của Precision, Recall, và F1-score
NOTE: Đề bài yêu cầu các điều kiện sau
• Phải kiểm tra giá trị nhận vào tp, fp, fn là type int, nếu là type khác thì print ví dụ check fn là float, print ’fn must be int’ và thoát hàm hoặc dừng chương trình.
• Yêu cầu tp, fp, fn phải đều lớn hơn 0, nếu không thì print ’tp and fp and fn must be greater than zero’ và thoát hàm hoặc dừng chương trình
'''
def evalute_classification(tp,fp,fn):
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
    if (tp<=0 or fp <= 0 or fn <= 0) :
        print ('tp and fp and fn must be greater than zero')
        return
    Precision = tp/(tp + fp)
    Recall = tp/(tp+ fn)
    F1_score = 2*((Precision*Recall)/(Precision + Recall))
    print (f"Precision:{Precision}, Recall: {Recall}, F1_score: {F1_score}")
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
def activation(x, alpha, act_name):
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
def calc_ae(y, y_hat):
    return abs(y - y_hat)
def calc_se(y, y_hat):
    return (y - y_hat) ** 2
def calc_approx_cos(x, n):
    cos_approx = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        cos_approx += term
    return cos_approx
def calc_approx_sin(x, n):
    sin_approx = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sin_approx += term
    return sin_approx
def calc_approx_sinh(x, n):
    sinh_approx = 0
    for k in range(n + 1):
        term = (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sinh_approx += term
    return sinh_approx
def calc_approx_cosh(x, n):
    cosh_approx = 0
    for k in range(n + 1):
        term = (x ** (2 * k)) / math.factorial(2 * k)
        cosh_approx += term
    return cosh_approx

### hàm chính 
if __name__ == "__main__":
    evalute_classification(2, 3, 5)
    # Test hàm activation_function
    alpha = 2
    activation(3, alpha,'sigmoid')
    activation(1, alpha,'relu')
    activation(-1, alpha,'elu')
    absolute_error = calc_ae(2, 9)
    print(f"absolute error: {absolute_error}")
    squared_error = calc_se(2, 1)
    print(f"squared error: {squared_error}")
    approx_cos = calc_approx_cos(3.14, 10)
    print(f"approx_cos: {approx_cos}")
    approx_sin = calc_approx_sin(3.14, 10)
    print(f"approx_sin: {approx_sin}")
    approx_sinh = calc_approx_sinh(3.14, 10)
    print(f"approx_sinh: {approx_sinh}")
    approx_cosh = calc_approx_cosh(3.14, 10)
    print(f"approx_cosh: {approx_cosh}")
