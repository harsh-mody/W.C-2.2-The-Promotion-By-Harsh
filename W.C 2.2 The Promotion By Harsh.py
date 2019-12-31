from itertools import combinations
ans = 0
t = int(input("Please Enter The Number Of Terms In List : "))
arr = []
arr = list(map(int, input("Enter the Values To Be Stored In The Array Separated by a Space : ").split()))
if len(arr) == t:
    lst = arr
    def findPair(lst):
        return [pair for pair in combinations(lst, 2) if lst[0] < lst[1]]
    pairList = findPair(lst)
    numberOfPairsInPairList = len(pairList)
    for i in range(0, numberOfPairsInPairList):
        pairAtIPositionList = pairList[i]
        numberOfItemsInPair = len(pairAtIPositionList)
        numberAtPosition1 = pairAtIPositionList[0]
        numberAtPosition2 = pairAtIPositionList[1]
        bitwiseAns = numberAtPosition1 & numberAtPosition2
        ans = (ans + bitwiseAns) % 101
    print("The Final Answer Is :", ans)
else:
    print("T and Number Of Elements In Array Are Not Equal.")
