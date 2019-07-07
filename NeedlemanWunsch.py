# ostatnia zmiana: 04.07, Marysia Hayder

import os
from enum import Enum




def getSequence(number):
    seq = input("Podaj sekwencje nr %d: " % number)
    return seq


def createMatrix(seqA, seqB):
    matrix = [['-'] * (max(len(seqA), len(seqB)) + 2) for i in range(max(len(seqA), len(seqB)) + 2)]
    for i in range(len(seqA)):
        matrix[0][i + 2] = seqA[i]
        matrix[1][i + 2] = i
    for i in range(len(seqB)):
        matrix[i + 2][0] = seqB[i]
        matrix[i + 2][1] = i
    matrix[0][0] = '-'
    matrix[1][1] = matrix[0][1] = matrix[1][0] = 0
    return matrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def fillMatrix(matrix, seqA, seqB):
    for i in range(len(seqB)):
        for j in range(len(seqA)):
            if seqA[j] == seqB[i]:
                diff = 0
            else:
                diff = 1
            matrix[i + 2][j + 2] = min(matrix[i + 2 - 1][j + 2] + 1, matrix[i + 2][j + 2 - 1] + 1,
                                       matrix[i + 2 - 1][j + 2 - 1] + diff)
    printMatrix(matrix)
    return matrix


def reverse(word):
    return word[::-1]

Way = Enum('Way', 'left up')

def readMatrix(matrix, seqA, seqB):

    if len(seqA) > len(seqB):
        way=Way.left
    else:
        way = Way.up
    alignedA, alignedB = align(matrix, seqA, seqB, way)
    print(' ')
    alignedA=reverse(alignedA)
    alignedB = reverse(alignedB)
    print(alignedA)
    print(alignedB)
    return alignedA, alignedB


def align(matrix, seqA, seqB, way):
    maxI = len(seqB) + 1
    maxJ = len(seqA) + 1
    i = maxI
    j = maxJ
    alignedA = []
    alignedB = []
    if matrix[0][j] == matrix[i][0]:
        alignedA.append(matrix[0][j])
        alignedB.append(matrix[i][0])
        finalInsertion=False
    else:
        if way==Way.left:
            alignedB.append(matrix[0][0])
            alignedA.append(matrix[0][j])
            finalInsertion=True
        else:
            alignedB.append(matrix[i][0])
            alignedA.append(matrix[0][0])
            finalInsertion=True
    score = matrix[i][j]
    while i > 2 and j > 2:
        newFieldValue = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
        print("Step ", maxI - i, "score: ", score)
        print(matrix[i][j])
        if way == Way.left:
            if newFieldValue == matrix[i][j - 1]:
                alignedA.append(matrix[0][j - 1])
                if True == finalInsertion and matrix[0][j-1] == matrix[i][0]:
                    alignedB.append(matrix[0][j-1])
                else:
                    alignedB.append(matrix[0][0])
                j = j - 1
                print("I'm going left")
            elif newFieldValue == matrix[i - 1][j - 1]:
                alignedB.append(matrix[i - 1][0])
                alignedA.append(matrix[0][j - 1])
                i = i - 1
                j = j - 1
                print("I'm going diagonally")
            elif newFieldValue == matrix[i - 1][j]:
                alignedB.append(matrix[i - 1][0])
                alignedA.append(matrix[0][0])
                i = i - 1
                print("I'm going up")
        else:
            if newFieldValue == matrix[i - 1][j]:
                alignedB.append(matrix[i - 1][0])
                if True == finalInsertion and matrix[0][j] == matrix[i-1][0]:
                    alignedA.append(matrix[0][j])
                else:
                    alignedA.append(matrix[0][0])
                i = i - 1
                print("I'm going up")
            elif newFieldValue == matrix[i - 1][j - 1]:
                alignedB.append(matrix[i - 1][0])
                alignedA.append(matrix[0][j - 1])
                i = i - 1
                j = j - 1
                print("I'm going diagonally")
            elif newFieldValue == matrix[i][j - 1]:
                alignedB.append(matrix[0][0])
                alignedA.append(matrix[0][j - 1])
                j = j - 1
                print("I'm going left")
    if i > 1:
        while j > 2:
            alignedB.append(matrix[0][0])
            alignedA.append(matrix[0][j - 1])
            j = j - 1
            print("I'm going left")
    if j > 1:
        while i > 2:
            alignedB.append(matrix[i - 1][0])
            alignedA.append(matrix[0][0])
            i = i - 1
            print("I'm going up")
    return alignedA, alignedB


def countMatrix(alignedA, alignedB):
    length = len(alignedA)
    score = 0
    for i in range(length):
        if alignedA[i] == alignedB[i]:
            score = score + 1
    percentage2 = 100 * score / len(alignedA)
    print("Percentage: ", 100 * score / len(alignedA))
    return percentage2


def saveExperiment(seqA, seqB, alignedA, alignedB, percentage):
    fileName = input("Enter the file name: ")
    list = [" Sequence 1: ", seqA, "\n", " Sequence 2: ", seqB, "\n", " Percentage (alignment-derived): ",
            str(percentage), "\n", "Alignment: ", "\n",
            str(alignedA), "\n", str(alignedB)]
    file = open(fileName, "w")
    file.writelines(list)
    file.close()


def main():
    seqA = getSequence(1)
    seqB = getSequence(2)
    matrix = createMatrix(seqA, seqB)
    matrix = fillMatrix(matrix, seqA, seqB)
    alignedA, alignedB = readMatrix(matrix, seqA, seqB)
    percentage2 = countMatrix(alignedA, alignedB)
    saveExperiment(seqA, seqB, alignedA, alignedB, percentage2)
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
