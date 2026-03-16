import json


def main():
    path = ""
    reportPath = ""
    values = 0
    tests = 0

    while True:
        path = input("Введите пути до файлов:")
        paths = path.split()

        try:
            valuesPath = getPathForFile(paths, "values.json")
            testsPath = getPathForFile(paths, "tests.json")
            reportPath = getPathForFile(paths, "report.json")
        except ValueError:
            print("Не хватает пути до одного из файлов. Пути должны заканчиваться следующими файлами: values.json, tests.json и report.json\nПопробуйте ещё раз.\n")
            continue

        try:
            values = getFileAsJson(valuesPath)["values"];
        except OSError:
            print("Неверный путь до файла values.json.\nПопробуйте ещё раз.\n")
            continue

        try:
            tests = getFileAsJson(testsPath);
            break;
        except OSError:
            print("Неверный путь до файла tests.json.\nПопробуйте ещё раз.\n")

    assignValues(values, tests["tests"])
    saveJsonAsFile(reportPath, tests)

    print("Отчет сформирован.")


def getPathForFile(paths, fileName):
    for path in paths:
        if path.find(fileName) != -1:
            return path
    raise ValueError

def getFileAsJson(path):
    with open(path, "r") as file:
        return json.load(file)

def getValueById(values, id):
    for val in values:
        if val["id"] == id:
            buf = val["value"]
            values.remove(val)
            return buf
    return "";

def assignValues(values, tests):
    id = ""
    value = ""
    testValues = ""
    for test in tests:
        id = test.get("id")
        value = test.get("value")
        if id != None and value != None:
            test["value"] = getValueById(values, id)
        testValues = test.get("values")
        if testValues != None:
            assignValues(values, testValues)

def saveJsonAsFile(path, jsonObj):
    with open(path, "w") as file:
        json.dump(jsonObj, file, indent=4, ensure_ascii=False)


main()   