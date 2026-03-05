def main():
    path = input("Введите путь до файла с описанием эллипса:")
    ellips = getLinesFromFileAsArray(path)
    ellips = getNumbersFromStringArray(ellips)
    path = input("Введите путь до файла с точками:")
    dots = getLinesFromFileAsArray(path)
    dots = getNumbersFromStringArray(dots)

    if len(dots) < 1:
        print("В файле с точками нет точек.")
        return

    if len(dots) > 100:
        print("В файле с точками более ста точек.")
        return

    translateDotsToEllipsCenter(ellips, dots)
    resArr = checkDotsPositionToEllips(ellips, dots)

    for res in resArr:
        print(res)

    
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