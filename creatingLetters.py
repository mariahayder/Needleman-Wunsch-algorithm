#last modification: 23.07, Marysia Hayder

def createLetter(fileName, sequence):
    file = open(fileName, "w")
    file.writelines(sequence)
    file.close()


def main():
    fileNamesList = ["n", "i", "c", "e", "f", "g", "h", "l", "s", "t", "u", "y", "polish l", "modificated e"]
    seqsList = ["WSSSSSSWNNNNNNWWWSSSSSSSENNNNNNESSSSSSEEEENNNNNNN",
                "WSSSSSSSENNNNNNN",
                "WWWWWSSSSSSSEEEEENWWWWNNNNNEEEEN",
                "WWWWWSSSSSSSEEEEENWWWWNNEEEENWWWWNNEEEEN",
                "WWWWWSSSSSSSENNNNEEEENWWWWNEEEEN",
                "WWWWWSSSSSSSEEEEENNNNWWWSEEESSWWWNNNNNEEEEN",
                "WSSSWWWNNNWSSSSSSSENNNEEESSSENNNNNNN",
                "WSSSSSSWNWSSEEENNNNNNN",
                "WSSSSSSSEEEENWWWNNNNNN",
                "WWWWWSSSSEEEESSWWWWSEEEEEENNNNWWWWNNEEEEEN",
                "WWWWWSEESSSSSSENNNNNNEEN",
                "WSSSSSSWWWNNNNNNWSSSSSSSEEEEENNNNNNN",
                "WSSWWWNNWSSSEESSSSENNNNEENNN",
                "WWNNWSSWWSEESSSSEEENWWNNNEEN",
                "WWWWWSSSSSSSEEEEENWWWWNNNEEEENWWWWNEEEEN"]
    i = 0
    while i < len(fileNamesList):
        createLetter(fileNamesList[i], seqsList[i])
        i = i + 1

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())


