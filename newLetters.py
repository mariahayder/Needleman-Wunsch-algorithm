#last modification: 23.07, Marysia Hayder

from NeedlemanWunsch import createMatrix, fillMatrix, readMatrix, countMatrix, printMatrix
import os, sys

def saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName):
    list = [" Sequence 1: ", seqA, "\n", " Sequence 2: ", seqB, "\n", " Percentage (alignment-derived): ",
            str(percentage), "\n", "Alignment: ", "\n",
            str(alignedA), "\n", str(alignedB)]
    os.chdir("diff=1")
    file = open(fileName, "w")
    file.writelines(list)
    file.close()


def work(fileA, fileB, fileName):
    file=open(fileA, "r")
    seqA=file.readline()
    file.close()
    file = open(fileB, "r")
    seqB = file.readline()
    file.close()
    matrix = createMatrix(seqA, seqB)
    matrix = fillMatrix(matrix, seqA, seqB)
    alignedA, alignedB = readMatrix(matrix, seqA, seqB)
    percentage = countMatrix(alignedA, alignedB)
    saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName)


def main():
    comparedLetters = ["n", "i", "c", "e", "f", "g", "h", "l", "s", "t", "u", "y", "polish l", "modificated e"]
    os.mkdir("diff=1")
    for i in range(len(comparedLetters)):
        for j in range(i + 1, len(comparedLetters)):
            pathname = os.path.dirname(sys.argv[0])
            fullPath=os.path.abspath(pathname)
            os.chdir(fullPath)
            fileName = []
            fileName.append(comparedLetters[i])
            fileName.append('_')
            fileName.append(comparedLetters[j])
            fileName = str(fileName)
            work(comparedLetters[i], comparedLetters[j], fileName)
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())