def word_count(file_path):
    word_count_dict = {}
    with open(file_path, 'r') as file:
        content = file.read()
        # Convert the content to lowercase
        content = content.lower()
        # Separate the words from the content, using split to separate by whitespace
        words = content.split()
        # Count the occurrences of each word
        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    return word_count_dict
if __name__ == '__main__':
    # test
    file_path = 'd:/AIO-Git/aio-244/module 1/week 2/P1_data.txt'
    print(word_count(file_path))
    result = word_count(file_path)
    print("Value of 'man' :", result['man'])
    

