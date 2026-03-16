def main():
    ellips = []
    dots = []

    while True:
        ellips = readInput("Введите путь до файла с описанием эллипса:")
        if len(ellips) < 2:
            print("В файле с описанием эллипса не хватает данных.\nПопробуйте ещё раз.\n")
            continue
        if len(ellips) > 2:
            print("В файле с описанием эллипса слишком много данных.\nПопробуйте ещё раз.\n")
            continue
        break

    while True:
        dots = readInput("Введите путь до файла с точками:")
        if len(dots) < 1:
            print("В файле с точками нет точек.\nПопробуйте ещё раз.\n")
            continue
        if len(dots) > 100:
            print("В файле с точками более ста точек.\nПопробуйте ещё раз.\n")
            continue
        break

    translateDotsToEllipsCenter(ellips, dots)
    resArr = checkDotsPositionToEllips(ellips, dots)

    for res in resArr:
        print(res)

def readInput(message):
    while True:
        value = []
        try:
            path = input(message)
            value = getLinesFromFileAsArray(path)
        except OSError:
            print("Неверный путь до файла.\nПопробуйте ещё раз.\n")
            continue

        try:
            value = getNumbersFromStringArray(value)
            return value   
        except ValueError:
            print("Неверное содержание файла. В файле должны быть пары целых чисел.\nПопробуйте ещё раз.\n")    
    
def getLinesFromFileAsArray(path):
    with open(path, "r") as file:
        arr = file.readlines()
    return arr

def getNumbersFromStringArray(strArr):
    res = []
    for strng in strArr:
        buf = strng.split()
        res.append([int(buf[0]), int(buf[1])])
    return res           

def translateDotsToEllipsCenter(ellips, dots):
    for dot in dots:
        dot[0] = dot[0] - ellips[0][0]
        dot[1] = dot[1] - ellips[0][1]

def checkDotsPositionToEllips(ellips, dots):
    a = ellips[1][0]
    b = ellips[1][1]
    res = []
    for dot in dots:
        equationRes = ellipsEquation(dot[0], dot[1], a, b)
        if equationRes < 1:
            res.append(1)
        elif equationRes == 1:
            res.append(0)
        else:
            res.append(2)
            
    return res

def ellipsEquation(x, y, a, b):
    return (x**2)/(a**2) + (y**2)/(b**2)


main()    