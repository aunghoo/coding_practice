def consecutive(num):
    # Write your code here
    combinations = 0
    if num == 1:
        return 1
    l = 1
    r = 2
    sumSoFar = 3
    while r < num:
        while l < r:
            while sumSoFar <= num:
                if sumSoFar == num:
                    combinations += 1
                    break
                if sumSoFar + r > num:
                    break
                r += 1
                sumSoFar += r
            sumSoFar -= l
            l += 1
        r += 1
        sumSoFar += r
    if combinations == 0:
        return 1
    return combinations