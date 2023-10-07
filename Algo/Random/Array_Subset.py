# Given a integer array
# Divide array into 2 subsets A and B 
# With following conditions:
#   A and B does not intersect
#   Union of A and B is the original array
#   The length of subset A is minimal
#   Sum of A > Sum of B
# Return A in sorted increasing order form

# Example:
# [3, 7, 5, 6, 2]
# The subset A that satisfy condition are [6, 7]
#   Sum of A > Sum of B([2, 3, 5])
#   A and B does not intersect
#   Union of A and B is [2, 3, 5, 6, 7]
#   A size is 2, the smallest possible size

# Constraint
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^5 (where 0 <= i <= n)
# arr is not sorted

def subsetA(arr):
    # Write your code here
    n = len(arr)
    ans = []
    if n > 2:
        arr.sort()
        totalSum = sum(arr)
        cumSum = 0
        # Could use math here but...I couldn't figure it out
        for i in range(0, n):
            num = arr.pop()
            ans.append(num)
            totalSum-=num
            cumSum+=num
            if cumSum > totalSum:
                ans.sort()
                break
    else:
        ans.append(max(arr))
    return ans
    

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)
    print(result)