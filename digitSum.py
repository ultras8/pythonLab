def digitSum(num):
    count = 0
    while num != 0:
        count += num % 10
        num//=10
    return count


print(digitSum(191))