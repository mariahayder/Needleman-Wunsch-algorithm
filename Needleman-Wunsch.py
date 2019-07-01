# ostatnia zmiana: 01.07, Marysia Hayder

import os


def getSequence(number):
    seq = input("Podaj sekwencje nr %d: " % number)
    return seq


def createMatrix(seqA, seqB):
    matrix = [[1000] * (max(len(seqA), len(seqB)) + 2) for i in range(max(len(seqA), len(seqB)) + 2)]
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


def readMatrix(matrix, seqA, seqB):
    if len(seqA) > len(seqB):
        alignedA, alignedB, maxScore, score = readLeft(matrix, seqA, seqB)
    else:
        alignedA, alignedB, maxScore, score = readUp(matrix, seqA, seqB)
    print(' ')
    lastA=len(seqA)-1
    lastB=len(seqB)-1
    if seqA[lastA] !='-' and seqA[lastA]!='0' and seqB[lastB]!='-' and seqB[lastB]!='0':
        alignedA=alignedA
        alignedB=alignedB
    else:
        alignedA.remove(alignedA[lastA])
        alignedB.remove(alignedA[lastB])
    print(alignedA)
    print(alignedB)
    """
    percentage = 100 * (maxScore - score) / maxScore
    print("Score: ", score)
    print("MaxScore: ", maxScore)
    print("Percentage: ", percentage)
    """
    return alignedA, alignedB,


def readLeft(matrix, seqA, seqB):
    maxI = len(seqB) + 1
    maxJ = len(seqA) + 1
    i = maxI
    j = maxJ
    maxScore = 0
    alignedA = []
    alignedB = []
    for k in range(max(maxI, maxJ)):
        maxScore = maxScore + k
    score = matrix[i][j]
    alignedA.append(matrix[0][j])
    alignedB.append(matrix[i][0])
    while i > 2 and j > 2:
        newFieldValue = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
        print("Krok ", maxI - i, "score: ", score)
        print(matrix[i][j])
        if newFieldValue == matrix[i][j - 1]:
            alignedB.append(matrix[0][0])
            alignedA.append(matrix[0][j-1])
            j = j - 1
            print("ide na lewo")
        elif newFieldValue == matrix[i - 1][j - 1]:
            alignedB.append(matrix[i-1][0])
            alignedA.append(matrix[0][j-1])
            i = i - 1
            j = j - 1
            print("Ide na ukos")
        elif newFieldValue == matrix[i - 1][j]:
            alignedB.append(matrix[i-1][0])
            alignedA.append(matrix[0][0])
            i = i - 1
            print("ide do gory")
        score = score + newFieldValue
    return alignedA, alignedB, maxScore, score


def readUp(matrix, seqA, seqB):
    maxI = len(seqB) + 1
    maxJ = len(seqA) + 1
    i = maxI
    j = maxJ
    maxScore = 0
    alignedA = []
    alignedB = []
    for k in range(max(maxI, maxJ)):
        maxScore = maxScore + k
    score = matrix[i][j]
    alignedA.append(matrix[0][j])
    alignedB.append(matrix[i][0])
    while i > 2 and j > 2:
        newFieldValue = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
        print("Krok ", maxI - i, "score: ", score)
        print(matrix[i][j])
        if newFieldValue == matrix[i - 1][j]:
            alignedB.append(matrix[i - 1][0])
            alignedA.append(matrix[0][0])
            i = i - 1
            print("ide do gory")
        elif newFieldValue == matrix[i - 1][j - 1]:
            alignedB.append(matrix[i - 1][0])
            alignedA.append(matrix[0][j - 1])
            i = i - 1
            j = j - 1
            print("Ide na ukos")
        elif newFieldValue == matrix[i][j - 1]:
            alignedB.append(matrix[0][0])
            alignedA.append(matrix[0][j - 1])
            j = j - 1
        print("ide na lewo")
    return alignedA, alignedB, maxScore, score


def countMatrix(alignedA, alignedB):
    length = len(alignedA)
    score = 0
    for i in range(length):
        if alignedA[i] == alignedB[i]:
            score = score + 1
    percentage2 = 100 * score / len(alignedA)
    print("Percentage2: ", 100 * score / len(alignedA))
    return percentage2


def saveExperiment(seqA, seqB, alignedA, alignedB, percentage2):
    fileName = input("Podaj nazwe pilku: ")
    list = [" Sequence 1: ", seqA, "\n", " Sequence 2: ", seqB, "\n", " Percentage2 (alignment-derived): ", str(percentage2), "\n", "Alignment: ", "\n",
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
