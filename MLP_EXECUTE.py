import os, sys

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def experiment(trainingPer, testingPer, neuron, epochs, runningMate, outputRate):
    commandList = [
        "cd " + CURRENT_PATH,
        "ls",
        # "./mlp.x sample.in 1 60 90 10 10 1 10 0"
        "./mlp.x sample.in {} {} {} {} {} {}".format(trainingPer, testingPer, neuron,
                                                     epochs, runningMate, outputRate)
    ]

    for command in commandList:
        mlpOpen = os.popen(command)
        mlpRead = mlpOpen.read()
        print(command)
        print(mlpRead)
        if command == commandList[-1]:
            fileResult = mlpRead.split('<RESULT FLAG>')[1]
            print(fileResult)
            filePath = CURRENT_PATH + "/{} {} {} {} {} {}.txt".format(trainingPer, testingPer, neuron,
                                                                      epochs, runningMate, outputRate)
            print(filePath)
            file = open(filePath, 'w')
            file.write(fileResult)
            file.close()


experiment(50, 40, 1, 100, 1, 1)
