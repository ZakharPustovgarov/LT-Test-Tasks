
def main():
    nums = readInput()

    midElem = sorted(nums)[len(nums) // 2]
    steps = sum(abs(num - midElem) for num in nums)

    if steps > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")
    else: 
        print(steps)


def readInput():
    while True:
        path = input("Введите путь до файла с массивом чисел:")

        try:       
            nums = getLinesFromFileAsArray(path)
        except OSError:
            print("Неверный путь до файла.\nПопробуйте ещё раз.\n")
            continue

        try:       
            nums = getNumbersFromStringArray(nums)
        except ValueError:
            print("Некорректный тип. В файле должны быть целые числа.\nПопробуйте ещё раз.\n")
            continue

        if len(nums) > 1:
            return nums
        else:
            print("Недостаточно чисел в массиве.\nПопробуйте ещё раз.\n")

def getLinesFromFileAsArray(path):
    with open(path, "r") as file:
        arr = file.readlines()
    return arr

def getNumbersFromStringArray(strArr):
    res = []
    for str in strArr:
        res.append(int(str))
    return res

main()   