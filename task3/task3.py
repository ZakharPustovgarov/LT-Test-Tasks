import json


def main():
    path = input("Введите путь до файла со значениями:")
    values = getFileAsJson(path)["values"];
    path = input("Введите путь до файла с тестами:")
    tests = getFileAsJson(path);
    path = input("Введите путь до файла для отчета:")

    assignValues(values, tests["tests"])
    saveJsonAsFile(path, tests)

    print("Отчет сформирован.")
    

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