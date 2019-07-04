# ostatnia zmiana: 04.07, Marysia Hayder

import os

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout



class Aligner(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

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
        Aligner.printMatrix(matrix)
        return matrix

    def reverse(word):
        return word[::-1]

    def readMatrix(matrix, seqA, seqB):
        if len(seqA) > len(seqB):
            leftWay = True
        else:
            leftWay = False
        alignedA, alignedB = Aligner.align(matrix, seqA, seqB, leftWay)
        print(' ')
        alignedA = Aligner.reverse(alignedA)
        alignedB = Aligner.reverse(alignedB)
        print(alignedA)
        print(alignedB)

        return alignedA, alignedB

    def align(matrix, seqA, seqB, leftWay):
        maxI = len(seqB) + 1
        maxJ = len(seqA) + 1
        i = maxI
        j = maxJ
        alignedA = []
        alignedB = []
        alignedA.append(matrix[0][j])
        alignedB.append(matrix[i][0])
        score = matrix[i][j]
        while i > 2 and j > 2:
            newFieldValue = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
            print("Step ", maxI - i, "score: ", score)
            print(matrix[i][j])
            if leftWay == True:
                if newFieldValue == matrix[i][j - 1]:
                    alignedB.append(matrix[0][0])
                    alignedA.append(matrix[0][j - 1])
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

    def interface(self):
        label1 = QLabel("Sequence 1: ", self)
        label2 = QLabel("Sequence 2: ", self)
        label3 = QLabel("Percentage: ", self)

        systemT = QGridLayout()
        systemT.addWidget(label1, 0, 0)
        systemT.addWidget(label2, 1, 0)
        systemT.addWidget(label3, 2, 0)

        self.seqAEdt = QLineEdit()
        self.seqBEdt = QLineEdit()
        self.percentageEdt = QLineEdit()

        self.percentageEdt.readonly = True

        systemT.addWidget(self.seqAEdt, 0, 1)
        systemT.addWidget(self.seqBEdt, 1, 1)
        systemT.addWidget(self.percentageEdt, 2, 1)

        okBtn = QPushButton("Compare", self)
        systemT.addWidget(okBtn, 3, 0)
        self.setLayout(systemT)

        okBtn.clicked.connect(self.work)

        self.resize(500, 500)
        self.setWindowTitle("Sequence Aligner")
        self.show()

    def saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName):
        list = [" Sequence 1: ", seqA, "\n", " Sequence 2: ", seqB, "\n", " Percentage (alignment-derived): ",
            str(percentage), "\n", "Alignment: ", "\n",
            str(alignedA), "\n", str(alignedB)]

        file = open(fileName, "w")
        file.writelines(list)
        file.close()


    def work(self):
        sender = self.sender()
        seqA = str(self.seqAEdt.text())
        seqB = str(self.seqBEdt.text())
        fileName = str(self.fileNameEdt.text())
        matrix = Aligner.createMatrix(seqA, seqB)
        matrix = Aligner.fillMatrix(matrix, seqA, seqB)
        alignedA, alignedB = Aligner.readMatrix(matrix, seqA, seqB)
        percentage = Aligner.countMatrix(alignedA, alignedB)
        Aligner.saveExperiment(seqA, seqB, alignedA, alignedB, percentage, fileName)
        self.percentageEdt.setText(str(percentage))
        self.alignedAEdt.setText(str(alignedA))
        self.alignedBEdt.setText(str(alignedB))


    def interface(self):
        label1 = QLabel("Sequence 1: ", self)
        label2 = QLabel("Sequence 2: ", self)
        label3 = QLabel("Percentage: ", self)
        label4 = QLabel("Name of the file: ", self)
        label5 = QLabel("Alignment: ", self)

        systemT = QGridLayout()
        systemT.addWidget(label1, 0, 0)
        systemT.addWidget(label2, 1, 0)
        systemT.addWidget(label3, 3, 0)
        systemT.addWidget(label4, 2, 0)
        systemT.addWidget(label5, 5, 0)

        self.seqAEdt = QLineEdit()
        self.seqBEdt = QLineEdit()
        self.percentageEdt = QLineEdit()
        self.fileNameEdt = QLineEdit()
        self.alignedAEdt = QLineEdit()
        self.alignedBEdt = QLineEdit()

        self.percentageEdt.readonly = True
        self.alignedAEdt.readonly = True
        self.alignedBEdt.readonly = True

        systemT.addWidget(self.seqAEdt, 0, 1)
        systemT.addWidget(self.seqBEdt, 1, 1)
        systemT.addWidget(self.fileNameEdt, 2, 1)
        systemT.addWidget(self.percentageEdt, 3, 1)
        systemT.addWidget(self.alignedAEdt, 6, 1)
        systemT.addWidget(self.alignedBEdt, 5, 1)

        okBtn = QPushButton("Compare", self)
        systemT.addWidget(okBtn, 4, 0)
        self.setLayout(systemT)

        okBtn.clicked.connect(self.work)

        self.resize(500, 500)
        self.setWindowTitle("Sequence Aligner")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Aligner()
    sys.exit(app.exec_())
