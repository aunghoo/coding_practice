#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#

def finalInstances(instances, averageUtil):
    # Write your code here
    limit = int(2*math.pow(10,8))
    i = 0
    while i < len(averageUtil):
        if averageUtil[i] > 60:
            if instances * 2 <= limit:
                instances = instances * 2
                i += 10
        elif averageUtil[i] < 25:
            if instances > 1:
                instances = int(math.ceil(float(instances)/2.0))
                i += 10
        i += 1
    return instances
