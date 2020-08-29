
# Given a 44x44 matrix of 1s and 0s, return
# the shape classification as a string. The
# shape is formed by the 1s in the matrix.

# The following strings are valid return values:
# square, rectangle, triangle, oval, circle

LAST = 43 # global variable

def process_signal(matrix):
    leftTopCorner = (-1, -1)
    # find the left top corner first
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1:
                leftTopCorner = (row, col)
                break
        if leftTopCorner != (-1, -1):
            break

    #check if it is a right angle corner
    if rightAngle(leftTopCorner[0], leftTopCorner[1], matrix):
        # return 'rectangle'
        rowInterested = leftTopCorner[0]
        colInterested = leftTopCorner[1]
        for r in range(rowInterested, len(matrix)):
            # find the bottom most pixel on the left side
            if matrix[r][colInterested] == 0 or r == LAST:
                width = r - 1 - rowInterested
                if rightAngle(r-1, colInterested, matrix):
                    # we know it's either rectangle or square
                    length = 0
                    for c in range(colInterested, len(matrix)):
                        if matrix[rowInterested][c] == 0 or c == LAST:
                            length = c - 1 - colInterested
                        # print (length, width)
                        if length == width:
                            return 'square'
                    return 'rectangle'
                return 'triangle'

    # check if triangle
    if isTriangle(leftTopCorner[0], leftTopCorner[1], matrix):
        return 'triangle'

    if isCircle(leftTopCorner[0], leftTopCorner[1], matrix):
        return 'circle'
    # check if oval or circle
    return 'oval'

def rightAngle(r, c, matrix):
    if matrix[r][c] == 1:
        # top and either right or left
        top, bottom, left, right = False, False, False, False
        if r != 0:
            if matrix[r-1][c] == 1:
                top = True
        if r != LAST:
            if matrix[r+1][c] == 1:
                bottom = True

        if c != 0:
            if matrix[r][c-1] == 1:
                left = True

        if c != LAST:
            if matrix[r][c+1] == 1:
                right = True

        if (top and left) or (top and right):
            return True

        if (bottom and left) or (bottom and right):
            return True

        return False


# def checkRectOrSquare(matrix):

def isTriangle(r, c, matrix):
    for i in range(r, len(matrix)):
        if rightAngle(i, c, matrix):
            return True
        if rightAngle(r, i, matrix):
            return True
    return False

def isCircle(topR, topC, matrix):
    height = 0
    bottom = -1
    for r in reversed(range(len(matrix))):
        for c in range(len(matrix)):
            if matrix[r][c] == 1:
                bottom = r
                break
        if bottom != -1:
            break
    height = abs(bottom - topR)


    left= -1
    width = -1
    right = -1
    for c in range(len(matrix)):
        for r in range(len(matrix)):
            if matrix[r][c] == 1:
                left = c
                break
        if left != -1:
            break

    for c in reversed(range(len(matrix))):
        for r in range(len(matrix)):
            if matrix[r][c] == 1:
                right = c
                break
        if right != -1:
            break
    width = abs(right - left)

    if abs(width - height) < 5:
        return True

    return False
