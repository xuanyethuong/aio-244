def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
if __name__ == '__main__':
    # Test
    string1 = 'Happiness'
    string2 = 'smiles'
    print(count_chars(string1))
    print(count_chars(string2))
    print (count_chars('smiles'))


