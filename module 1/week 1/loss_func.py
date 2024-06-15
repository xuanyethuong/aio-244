import random
import math

def regression_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('Number of samples must be an integer number')
        return
    num_samples = int(num_samples)
    
    total_loss = 0
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        if loss_name == 'MAE':
            loss = abs(target - predict)
        elif loss_name == 'MSE':
            loss = (target - predict) ** 2
        elif loss_name == 'RMSE':
            loss = math.sqrt((target - predict) ** 2)
        total_loss += loss
        print(f'Loss Name: {loss_name}, Sample: sample-{i}, Predict: {predict}, Target: {target}, Loss: {loss}')

    final_loss = total_loss / num_samples
    
    print(f'Final Loss: {final_loss}')

num_samples = input('Enter number of samples: ')
loss_name = input('Enter loss name (MAE, MSE, RMSE): ')
regression_loss(num_samples, loss_name)