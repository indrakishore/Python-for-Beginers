import time

def makePR(countOfPR):
    """
        This function will do PR's for sunny
    """
    time.sleep(2)
    if (countOfPR%2 == 0):
        print('\nReadMe.md edited, its going to count anyways :)')
    else:
        print('\nPrint statement added, its going to count anyways :)')
    return countOfPR + 1


def isHacktoberfestCompleted(countOfPR):
    """
        This function will return true if sunny has completed 4 or more PR's, else it will do the PR's for him
    """

    if (countOfPR < 4):
        print("You have incomplete PR's, let me do it for you")
        while(countOfPR < 4):
            countOfPR = makePR(countOfPR)
        time.sleep(2)
        print("\nYou have successfully completed 4 PR's :)")
        return True
    return False

if __name__ == "__main__":
    countOfPR = 0
    if (isHacktoberfestCompleted(countOfPR)):
        time.sleep(2)
        print('\nCongratulations on completing Hacktoberfest 2021')
        time.sleep(2)
        size = input('\nEnter your T-shirt size (XS, S, M, L, XL, XXL) : ')
        time.sleep(2)
        print("\nHere is your Hacktoberfest2021 T-shirt : ")
        print("      __     __     ")
        print("    /    ---    \\")
        print("    --|  H21  |--")
        print("      |       |")
        print("       -------  ")
    else:
        print("You need to make atleast 4 PR's")

    
