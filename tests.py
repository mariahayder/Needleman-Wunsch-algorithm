from NeedlemanWunsch import createMatrix, fillMatrix, readMatrix, countMatrix

def saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName):
    list = [" Sequence 1: ", seqA, "\n", " Sequence 2: ", seqB, "\n", " Percentage (alignment-derived): ",
            str(percentage), "\n", "Alignment: ", "\n",
            str(alignedA), "\n", str(alignedB)]
    file = open(fileName, "w")
    file.writelines(list)
    file.close()


def work(seqA, seqB, fileName):
    matrix = createMatrix(seqA, seqB)
    matrix = fillMatrix(matrix, seqA, seqB)
    alignedA, alignedB = readMatrix(matrix, seqA, seqB)
    percentage = countMatrix(alignedA, alignedB)
    saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName)


def main():
    work("abcd", "abcd", "ab1")
    work("aktbcd", "abcd", "ab2")
    work("abcd", "akcd", "ab3")
    work("abcd", "abcktd", "ab4")
    work("abcktd", "abcd", "ab5")
    work("abcd", "abcdkt", "ab6")
    work("abcd", "ktabcd", "ab7")
    work("ktabcd", "abcd", "ab8")
    work("ktabcduv", "abcd", "ab9")
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())