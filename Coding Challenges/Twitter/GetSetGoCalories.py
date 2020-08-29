
def isPossible(calCounts, requiredCals):
    # Write your code here
    sumsSoFar = {0}
    for c in calCounts:
        if c < requiredCals:
            newSums = []
            for s in sumsSoFar:
                if s+c < requiredCals:
                    newSums.append(s+c)
                if s+c == requiredCals:
                    return True
            sumsSoFar.update(newSums)
    return False
