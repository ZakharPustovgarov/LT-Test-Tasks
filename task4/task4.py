
def main():
    path = input("Введите путь до файла с массивом чисел:")
    nums = getLinesFromFileAsArray(path)
    nums = getNumbersFromStringArray(nums)

    arithMean = getArithmeticMean(nums)
    closestToMean = getClosestToArithmeticMean(nums, arithMean)
    steps = getStepsToEqual(nums, closestToMean)

    if steps > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else: 
        print(steps)
    

def getLinesFromFileAsArray(path):
    with open(path, "r") as file:
        arr = file.readlines()
    return arr

def getNumbersFromStringArray(strArr):
    res = []
    for str in strArr:
        res.append(int(str))
    return res

def charToInt(char, isNegative):
     if isNegative:
         return int(char) * -1
     else:
         return int(char)

def getArithmeticMean(nums):
    sum = 0;
    for num in nums:
        sum+=num
    return sum/len(nums)

def getClosestToArithmeticMean(nums, arithMean):
    currentClosest = nums[0]
    currentClosestDiff = abs(arithMean-nums[0])
    for num in nums:
        diff = abs(arithMean - num)
        if diff < currentClosestDiff:
            currentClosest = num
            currentClosestDiff = diff
    return currentClosest

def getStepsToEqual(nums, ref):
    steps = 0
    for num in nums:
        steps+= abs(ref - num)
    return steps


main()    