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
def activation_function(x,alpha):
    if not is_number(x):
        print ("must be a number")
        return
    else:
        sig_f = sig_func(x)
        reLU_f = reLU_func(x)
        eLU_f = eLU_func(x,alpha)
if __name__ == "__main__":
    evalute_classification(2, 3, 5)
    # Test hàm activation_function
    x = 10  # Thay đổi giá trị x để kiểm tra các trường hợp khác nhau
    alpha = 1.0
    activation_function(x, alpha)