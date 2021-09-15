def main():
    file = open("log_sample.txt","r")
    completeLog = file.readlines()
    sameUserPages = []
    mostVisitedPages = []

    for idx, item in enumerate(completeLog):
        if idx == 0:
            prevUser = None 

        currentUser = item.split(";")[0]
        currentPage = item.split(";")[2]
    
        if prevUser is None or prevUser == currentUser: 
            prevUser = currentUser
            sameUserPages.append(currentPage.strip())
        else: 
            if len(sameUserPages) == 3:
                foundElementIndex = findElement(mostVisitedPages,sameUserPages)

                if foundElementIndex is False:
                    mostVisitedPages.append([sameUserPages,1])
                else:
                    mostVisitedPages[foundElementIndex][1] += 1
                    
                sameUserPages = []
                sameUserPages.append(currentPage.strip())
                prevUser = currentUser

    print (sortRanking(mostVisitedPages))

def findElement(array,element):
    if len(array) == 0:
        return False

    for idx, item in enumerate(array):
        if item[0] == element:
            return idx
        else:
            None

    return False

def sortRanking(array):
    return sorted(array,key=lambda x: -x[1])

if __name__ == "__main__":
    main()