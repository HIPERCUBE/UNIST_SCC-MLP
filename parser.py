import re


def splitLayer(data):
    return data.split('\n')


def parseLayer(data):
    return data.split('     ')


def parseX(data):
    array = []
    for layer in splitLayer(data):
        array.append(parseLayer(layer)[0])
    return array


def parseTrainError(data):
    array = []
    for layer in splitLayer(data):
        array.append(parseLayer(layer)[1])
    return array


def parseTestError(data):
    array = []
    for layer in splitLayer(data):
        array.append(parseLayer(layer)[2])
    return array


def search(regex, data):
    m = re.search(regex, data)
    try:
        return float(m.group())
    except AttributeError:
        return ''


def trainResult(data):
    return search(r'(?<=(TRAIN ERROR =  )).+', data)


def testResult(data):
    return search(r'(?<=(TEST  ERROR =  )).+', data)


def valResult(data):
    return search(r'(?<=(VAL   ERROR =  )).+', data)
