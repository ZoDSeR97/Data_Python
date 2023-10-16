# Given 3 variables: i, j, k

# We want to sum sequence like:
# i + (i+1) + (i+2) + . . . + j + (j-1) + (j-2) + . . . + k
# where i increment to j
# where j decrement to k

def solution(i, j, k):
    sumIJ = sum(range(i, j)) # [i, j)
    sumJK = sum(range(j, k, -1)) # (k, j]
    return sumIJ+sumJK+k

def math_solution(i, j, k):
    # Sum from i to j
    sum_ij = ((j - i + 1) * (i + j)) // 2

    # Sum from j to k
    sum_jk = ((j - k + 1) * (j + k)) // 2
    return sum_ij+sum_jk - j # We added j twice so remove 1 j

if __name__ == "__main__":
    i, j, k = 0, 5, -1
    expected = 24 # 0 + 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 + 0 - 1 -2 = 24
    print(solution(i, j, k) == expected)
    print(math_solution(i,j,k) == expected)
    i, j, k = 0, 5, -2
    expected = 22 # 0 + 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 + 0 - 1 -2 = 22
    print(solution(i, j, k) == expected)
    print(math_solution(i,j,k) == expected)
    i, j, k = 1, 5, -3
    expected = 19 # 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 + 0 - 1 -2 - 3 = 19
    print(solution(i, j, k) == expected)
    print(math_solution(i,j,k) == expected)