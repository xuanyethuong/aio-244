def max_sliding_window(num_list, k):
    result = []
    size = len(num_list)
    print("size:", size)
    if k > size:
        print('k must be less than or equal to the number of elements in the list')
        return []

    for i in range(size - k + 1):
        # Lấy một đoạn con của danh sách có độ dài k
        print("i:", i)
        print("numlist: ", num_list[i:i + k])
        current_window = num_list[i:i + k]
        print("current_window", current_window)
        # Tìm giá trị lớn nhất trong đoạn con
        current_max = max(current_window)
        print("current_max:", current_max)
        # Lưu giá trị lớn nhất vào danh sách kết quả
        result.append(current_max)
    return result


if __name__ == '__main__':
    # Test
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    #k = 3
    #print(max_sliding_window(num_list, k))
    assert max_sliding_window([3 , 4 , 5 , 1 , -44] , 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3
    print (max_sliding_window( num_list , k))
