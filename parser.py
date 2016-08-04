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
