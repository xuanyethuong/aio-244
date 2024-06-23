def levenshtein_distance(source, target):
    m, n = len(source), len(target)
    
    # Create a matrix to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp)
    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i
        print(f"dp[{i}][0]:{dp[i][0]}")
    for j in range(n + 1):
        dp[0][j] = j
        # Compute the Levenshtein distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost) # Substitution

    return dp[m][n]
if __name__ == '__main__':
# Test the function
    source = "kitten"
    target = "sitting"
    print(f"The Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")
    print("The Levenshtein distance between hola and hello", levenshtein_distance(" hola ", " hello "))