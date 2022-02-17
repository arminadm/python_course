# Armin Darabi Mahboub

def main():

    """input"""
    text = input()

    """calculation"""
    # make a list from text using split
    primitiveList = text.strip().split(" ")

    # make a clean list of all the required data
    cleanList = cleanData(primitiveList)

    """output"""
    printing(cleanList)


def cleanData(list):
    """begining requirements"""
    cleanList = []
    dotIndex = {}
    
    """main progress"""
    # saving all of the locations(index) from any dot so we can delete the word after them
    for word in list:
        if (word[len(word) - 1]) == ".":
            dotIndex[word] = list.index(word)
    
    # add all of the words(expect first) which starts with uppercase into a list
    for wordCounter in range(1, len(list)):
        word = list[wordCounter]
        if word[0].isupper():
            cleanList.append([word, wordCounter])
    
    # removing all of the words that come after (.) in cleanList
    for index in dotIndex.values():
        for eachItem in cleanList:
            if eachItem[1] == index + 1:
                cleanList.remove(eachItem)
    
    # remove (.) and (,) form any of the cleanlist words
    for itemCounter in range(len(cleanList)):
        cleanList[itemCounter][0] = cleanList[itemCounter][0].replace(".", "")
        cleanList[itemCounter][0] = cleanList[itemCounter][0].replace(",", "")

    return cleanList

def printing(list):
    for item in list:
        print(f"{item[1] + 1}:{item[0]}")

if __name__ == "__main__":
    main()