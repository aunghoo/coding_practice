#
# Complete the 'minPrice' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY cost as parameter.
#

def minPrice(cost):
    # Write your code here
    numBlocks = len(cost)
    numColors = len(cost[0])
    mem = [[0] * numColors for i in range(numBlocks)]
    for b in range(numBlocks):
        for c in range(numColors):
            if b == 0:
                mem[b][c] = cost[b][c]
            else:
                prevMin = sys.maxsize
                for i in range(numColors):
                    if i != c and mem[b-1][i] < prevMin:
                        prevMin = mem[b-1][i]
                mem[b][c] = cost[b][c] + prevMin
    print(mem[0])
    return min(mem[numBlocks-1])
