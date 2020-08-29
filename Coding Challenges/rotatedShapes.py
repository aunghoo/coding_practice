
# Your Part 1 Solution

# Given a 44x44 matrix of 1s and 0s, return
# the shape classification as a string. The
# shape is formed by the 1s in the matrix.

# The following strings are valid return values:
# square, rectangle, triangle, oval, circle

LAST = 43 # global variable

def process_signal(matrix):
    # get top
    topR, topC = -1, -1
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 1:
                topR = r
                topC = c
                break
        if topR != -1:
            break

    # get left
    leftR, leftC = -1, -1
    for c in range(len(matrix)):
        for r in range(len(matrix)):
            if matrix[r][c] == 1:
                leftR = r
                leftC = c
                break
        if leftR != -1:
            break

    # get right
    rightR, rightC = -1, -1
    for c in reversed(range(len(matrix))):
        for r in range(len(matrix)):
            if matrix[r][c] == 1:
                rightR = r
                rightC = c
                break
        if rightR != -1:
            break

    # get bottom
    bottomR, bottomC = -1, -1
    for r in reversed(range(len(matrix))):
        for c in range(len(matrix)):
            if matrix[r][c] == 1:
                bottomR = r
                bottomC = c
                break
        if bottomR != -1:
            break

    TR = math.sqrt((topR-rightR)**2 + (topC-rightC)**2)
    TL = math.sqrt((topR-leftR)**2 + (topC-leftC)**2)
    BR = math.sqrt((bottomR-rightR)**2 + (bottomC-rightC)**2)
    BL = math.sqrt((bottomR-leftR)**2 + (bottomC-leftC)**2)



    # circleness = 0
    # if to
    # for i in [2, 3, 4]:
    #     TRinterX = int((topR-rightR)/i)
    #     TRinterY = int((topC-rightC)/i)
    #     print (TRinterX, TRinterY)
    #     if matrix[TRinterX][TRinterY] != 1:
    #         return 'oval'


    if TR == 0 or TL == 0 or BR == 0 or BL == 0:
        return 'triangle'


    if abs(TR - TL) < 5:
        if abs(leftR - rightR) < 5 and abs(topC - bottomC) < 5:
            return 'circle'
        return 'square'

    vertical = 0
    horizontal = 0
    TB = math.sqrt((topR-bottomR)**2 + (topC-bottomC)**2)
    RL = math.sqrt((rightR-leftR)**2 + (rightC-leftC)**2)
    if abs(TB - RL) < 20:
        return 'oval'
    return 'rectangle'






#
# def getCorners(matrix):
#     # get top
#     topR, topC = -1, -1
#     for r in range(len(matrix)):
#         for c in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 topR = r
#                 topC = c
#                 break
#         if topR != -1:
#             break

#     # get left
#     leftR, leftC = -1, -1
#     for c in range(len(matrix)):
#         for r in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 leftR = r
#                 leftC = c
#                 break
#         if leftR != -1:
#             break

#     # get right
#     rightR, rightC = -1, -1
#     for c in reversed(range(len(matrix))):
#         for r in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 rightR = r
#                 rightC = c
#                 break
#         if rightR != -1:
#             break

#     # get bottom
#     bottomR, bottomC = -1, -1
#     for r in reversed(range(len(matrix))):
#         for c in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 bottomR = r
#                 bottomC = c
#                 break
#         if bottomR != -1:
#             break

#     TR = sqrt((topR-rightR)**2 + (topC-rightC)**2)
#     TL = sqrt((topR-leftR)**2 + (topC-leftC)**2)
#     BR = sqrt((bottomR-rightR)**2 + (bottomC-rightC)**2)
#     BL = sqrt((bottomR-leftR)**2 + (bottomC-leftC)**2)

#     if abs(TR - TL) < 5:
#         return 'square'



# def rightAngle(r, c, matrix):
#     if matrix[r][c] == 1:
#         # top and either right or left
#         top, bottom, left, right = False, False, False, False
#         if r != 0:
#             if matrix[r-1][c] == 1:
#                 top = True
#         if r != LAST:
#             if matrix[r+1][c] == 1:
#                 bottom = True

#         if c != 0:
#             if matrix[r][c-1] == 1:
#                 left = True

#         if c != LAST:
#             if matrix[r][c+1] == 1:
#                 right = True

#         if (top and left) or (top and right):
#             return True

#         if (bottom and left) or (bottom and right):
#             return True

#         return False


# def checkRectOrSquare(matrix):

# def isTriangle(r, c, matrix):
#     for i in range(r, len(matrix)):
#         if rightAngle(i, c, matrix):
#             return True
#         if rightAngle(r, i, matrix):
#             return True
#     return False

# def isCircle(topR, topC, matrix):
#     height = 0
#     bottom = -1
#     for r in reversed(range(len(matrix))):
#         for c in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 bottom = r
#                 break
#         if bottom != -1:
#             break
#     height = abs(bottom - topR)


#     left= -1
#     width = -1
#     right = -1
#     for c in range(len(matrix)):
#         for r in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 left = c
#                 break
#         if left != -1:
#             break

#     for c in reversed(range(len(matrix))):
#         for r in range(len(matrix)):
#             if matrix[r][c] == 1:
#                 right = c
#                 break
#         if right != -1:
#             break
#     width = abs(right - left)

#     if abs(width - height) < 5:
#         return True

#     return False
