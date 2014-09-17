import string
import operator
import sys


def getFileName():
    fileName = ""
    if len(sys.argv) < 2:
        fileName = input("What is the name of the file? ->")
    else:
        fileName = str(sys.argv[1])
    return fileName


def printTopTen(finalList):
    print("\n\n\nTop 10: \n\n\n")
    for i in range(0, 10):
        print("#%s {}".format(finalList[i]) % str(i + 1))



def numberOfWords(fileName):
    """
    (String)-> List
    Takes in a string with the name of the file
    :return: - Returns a list of the words found in the file in descending order of nuber of times they appear
    """
    file = open(fileName, "r")
    fileToString = file.read()
    fileToStringList = fileToString.split()
    file.close()
    print("Here all of the words that appear in the file: ")
    for i in range(0,len(fileToStringList)):
        fileToStringList[i] = fileToStringList[i].strip(".,;:")
        fileToStringList[i] = fileToStringList[i].lower()
        print(fileToStringList[i])
    print("\n\n\nCounting each word: \n\n\n")
    eachWordOnceList = {}
    for i in fileToStringList:
        if i not in eachWordOnceList:
            eachWordOnceList.update({i: 1})
        if i in eachWordOnceList:
            eachWordOnceList[i] += 1

    sortedWords = sorted(eachWordOnceList.items(), key=lambda x: x[1], reverse=True)
    finalList = []
    for i in range(0, len(sortedWords)):
        sortedWords[i] = str(sortedWords[i]).strip("',()'")
        sortedWords[i] = sortedWords[i][0:1].upper() + sortedWords[i][1:].replace("'", "").replace(","," =")
        #x = "".join(sortedWords[i])
        finalList.append(sortedWords[i])
        print(sortedWords[i])
    return finalList

def main():
    fName = getFileName()
    wordsList = numberOfWords(fName)
    printTopTen(wordsList)


if __name__ == "__main__":
    main()