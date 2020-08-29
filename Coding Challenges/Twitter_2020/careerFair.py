import collections

def maxEvents(arrival, duration):
    # Write your code here
    reached = 0
    lastBegin = 0
    numEvents = 0

    eventsMap = collections.defaultdict(int)
    for i in range(len(arrival)):
        if arrival[i] not in eventsMap:
            eventsMap[arrival[i]] = arrival[i]+duration[i]-1
        else:
            if arrival[i]+duration[i]-1 < eventsMap[arrival[i]]:
                eventsMap[arrival[i]] = arrival[i]+duration[i]-1
    arrival = sorted(arrival)

    for i in range(len(arrival)):
        if arrival[i] > reached:
            numEvents += 1
            reached = eventsMap[arrival[i]]
            lastBegin = arrival[i]
        # if there is another company during the time, replace if finishing earlier
        if arrival[i] >= lastBegin and arrival[i] < reached:
            if eventsMap[arrival[i]] < reached:
                reached = eventsMap[arrival[i]]
                lastBegin = arrival[i]
    return numEvents
