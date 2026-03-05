def main():
    res1 = countPath(1)
    res2 = countPath(2)

    print(res1+res2)

def countPath(arrId):
    n = int(input(f"Введите n для {arrId}-го массива:"))
    m = int(input(f"Введите m для {arrId}-го массива:"))
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


main()    