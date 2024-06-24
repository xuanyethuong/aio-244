def check_the_number(num):  # Question 5
    list_of_numbers = [1, 2, 3, 4]  # Example list of numbers
    results = False  # Initialize results as False
    # Loop through the range (1, 5)
    for i in range(1, 5):
        # Append current value of i to list_of_numbers
        list_of_numbers.append(i)

    if num in list_of_numbers:
        results = True  # Set results to True if N is found in list_of_numbers

    return results


def my_function(data, max, min):  # Question 6:
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


def my_function7(x, y):  # Question 7
    # Using extend to connect y into x
    x.extend(y)
    return x


def my_functionq8(n):  # Question 8
    min_value = n[0]
    for value in n:
        if value < min_value:
            min_value = value
    return min_value


def my_function9(n):  # Question 9
    # Tìm phần tử có giá trị lớn nhất trong danh sách n
    max_value = n[0]  # Giả sử phần tử đầu tiên là lớn nhất
    for value in n:
        if value > max_value:
            max_value = value
    return max_value


def my_function10(integers, number=1):  # Question 10
    return any(element == number for element in integers)


def my_function11(list_nums=[0, 1, 2]):  # Question 11
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


def my_function12(data):  # Question 12
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


def my_function13(y):  # Question 13
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var


def my_function14(x):  # Question 14
    return x[::-1]  # Đảo ngược chuỗi x


def function_helper(x):  # Question 15
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function15(data):  # Question 15
    res = [function_helper(x) for x in data]
    return res


if __name__ == '__main__':
    # Question 5:
    N = 7
    # Assert that check_the_number(N) returns False
    assert check_the_number(N) == False
    N = 2
    results = check_the_number(N)
    print(results)  # Print results for N = 2
    # Question 6:
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print("Câu 6")
    print(my_function(max=max, min=min, data=my_list))
    # Question 7:
    list_num1 = ['a', 2, 5]
    list_num2 = [1, 1]
    list_num3 = [0, 0]
    assert my_function7(list_num1, my_function7(
        list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]
    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]
    print(my_function7(list_num1, my_function7(list_num2, list_num3)))
    # Question 8:
    my_list = [1, 22, 93, -100]
    assert my_functionq8(my_list) == -100
    my_list1 = [1, 2, 3, -1]
    print(my_functionq8(my_list1))
    # Question 9:
    my_list = [1001, 9, 100, 0]
    assert my_function9(my_list) == 1001
    my_list9 = [1, 9, 9, 0]
    print(my_function9(my_list9))
    # Question 10:
    my_list = [1, 3, 9, 4]
    assert my_function10(my_list, -1) == False
    my_list = [1, 2, 3, 4]
    print(my_function10(my_list, 2))
    # Question 11:
    assert my_function11([4, 6, 8]) == 6
    print(my_function11())
    # Question 12:
    assert my_function12([3, 9, 4, 5]) == [3, 9]
    print(my_function12([1, 2, 3, 5, 6]))
    # Question 13:
    assert my_function13(8) == 40320
    print(my_function13(4))
    # Question 14:
    x = 'I can do it'
    assert my_function14(x) == "ti od nac I"
    x = 'apricot'
    print(my_function14(x))
    # Question 15:
    data = [10, 0, -10, -1]
    assert my_function15(data) == ['T', 'N', 'N', 'N']
    data = [2, 3, 5, -1]
    print(my_function15(data))
