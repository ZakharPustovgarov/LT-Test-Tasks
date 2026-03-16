def main():
    res1 = countPath(1)
    res2 = countPath(2)

    print(res1+res2)

def countPath(arrId):
    n = 0
    m = 0
    n = readInput(arrId, n, "n")
    m = readInput(arrId, m, "m")

    baseArr = range(1, n+1)
    currentPos = 0
    currentNum = 1
    res=""
    while True:
        res+= str(currentNum)
        currentPos+= m-1
        if currentPos >= n:
            currentPos-= n
        if currentPos == 0:
            break
        currentNum = baseArr[currentPos]
    return res

def readInput(arrId, value, valueName):
    while True:
        try:
            value = int(input(f"Введите {valueName} для {arrId}-го массива:"))
            break
        except ValueError:
            print(f"Некорректный тип. {valueName} должно быть целым числом. Попробуйте ещё раз.")
    return value



main()    