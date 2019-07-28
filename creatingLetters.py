#last modification: 26.07, Marysia Hayder

def createLetter(fileName, sequence):
    file = open(fileName, "w")
    file.writelines(sequence)
    file.close()


def main():
    fileNamesList = ["n", "i", "c", "e", "f", "g", "h", "j", "l", "s", "t", "u", "y", "polish l", "modificated e"]
    seqsList = ["WSSSSSSSSSSSSSSSSSSSSWWWWWWWWWNNNNNNNNNNNNNNNNNNNNWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSENNNNNNNNNNNNNNNNNNNNEEEEEEEEESSSSSSSSSSSSSSSSSSSSEEEEEEEEEEENNNNNNNNNNNNNNNNNNNNN", #n
                "WSSSSSSSSSSSSSSSSSSSSSENNNNNNNNNNNNNNNNNNNNN", #i
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEN", #c
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNNNNNNNEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNNNNNNNEEEEEEEEEEEEEEEEEEEEN", #e
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSENNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNEEEEEEEEEEEEEEEEEEEEN", #f
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNWWWWWWWWWWWWWWWSEEEEEEEEEEEEEESSSSSSSSSSSWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEN", #g
                "WSSSSSSSSSSWWWWWWWWWWWWWWWWWWWNNNNNNNNNNWSSSSSSSSSSSSSSSSSSSSSENNNNNNNNNNEEEEEEEEEEEEEEEEEEESSSSSSSSSSENNNNNNNNNNNNNNNNNNNNN", #h
                "WSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWNNWSSSEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNNN", #j szerokie
                "WSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNN", #l
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEESSSSSSSSSWWWWWWWWWWWWWWWWWWWWSEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNWWWWWWWWWWWWWWWWWWWWNNNNNNNNNEEEEEEEEEEEEEEEEEEEEN", #s
                "WWWWWWWWWWWWWWWWWWWWWSEEEEEEEEEESSSSSSSSSSSSSSSSSSSSENNNNNNNNNNNNNNNNNNNNEEEEEEEEEEN", #t
                "WSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNWSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNNN", #u
                "WSSSSSSSSWWWWWWWWWWWWWWWWWWWNNNNNNNNWSSSSSSSSSEEEEEEEEEESSSSSSSSSSSSENNNNNNNNNNNNEEEEEEEEEENNNNNNNNN",#y
                "WWWWWWWWWWNNNNNNNNWSSSSSSSSSSWWWWWWWWWWSEEEEEEEEEESSSSSSSSSSSSEEEEEEEEEEENWWWWWWWWWWNNNNNNNNNNNNEEEEEEEEEEN", #polish l
                "WWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEENWWWWWWWWWWWWWWWWWWWWNNNEEEEEEEEEEEEEEEEEEEEN"]#mod e


    i = 0
    while i < len(fileNamesList):
        createLetter(fileNamesList[i], seqsList[i])
        i = i + 1

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())


