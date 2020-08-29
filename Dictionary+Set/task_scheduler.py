# This is a sandbox to experiment with CoderPad's execution capabilities.
# It's a temporary, throw-away session only visible to you.

    
#cooldown 4
#[1,2,2,1,2]
#1,2,_,_,_,_,2,1,_,_,_,2

#cooldown 3
#[1,2,1]
#1,2,_,_,1

#cooldown 3
#[1,2,3,4,1]
#1,2,3,4,1

#cooldown 2
#[1,1,1]
#1,_,_,1,_,_,1

from collections import deque

# time complexity: O(size of schedule)
# memory complexity: O(size of unique tasks in arr)
def scheduler(arr, cooldown):
    seen = {}
    count = 0
    for i in arr:
        if i in seen.keys() and seen[i] >= count - cooldown:
            filled = count - seen[i] - 1
            count += cooldown - filled
        seen[i] = count
        count += 1
    return count

# solution with less memory complexity
# time: O(count)
# space: O(min(cooldown,unique elems in arr))
def opt_scheduler(arr, cooldown):
    seen = {}
    queue = deque()
    count = 0
    for i in arr:
        if i in seen.keys() and seen[i] >= count - cooldown:
            gaps = count - seen[i] - 1
            if gaps <= cooldown:
                count += cooldown - gaps
        queue.append(i)
        if len(queue) > cooldown:
            print seen
            del seen[queue[0]]
            queue.popleft()
            print seen
        seen[i] = count
        count += 1
        
    return count

array = [1,1,1]
print opt_scheduler(array, 2)
