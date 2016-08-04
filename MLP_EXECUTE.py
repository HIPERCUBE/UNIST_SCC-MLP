import os, sys

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def experiment(trainingPer, testingPer, neuron, epochs, learningRate, outputRate):
    fileName = "{} {} {} {} {} {}".format(trainingPer, testingPer, neuron,
                                          epochs, learningRate, outputRate)
    filePath = CURRENT_PATH + "/result/" + fileName
    if not os.path.isfile(filePath):
        return

    commandList = [
        "cd " + CURRENT_PATH,
        "ls",
        # "./mlp.x sample.in 1 60 90 10 10 1 10 0"
        "./mlp.x sample.in " + fileName
    ]

    for command in commandList:
        mlpOpen = os.popen(command)
        mlpRead = mlpOpen.read()
        print(command)
        print(mlpRead)
        if command == commandList[-1]:
            fileResult = mlpRead.split('<RESULT FLAG>')[1]
            print(fileResult)
            filePath
            print(filePath)
            file = open(filePath + '.txt', 'w')
            file.write(fileResult)
            file.close()


for i in range(0, 30):
    for percent in range(5):
        experiment(50 + i, 40 - i, 40, 100, percent / 2.0, 1

# for percent in range(5):
#         experiment(70, 20, 1, 100, percent / 2.0, 1)
