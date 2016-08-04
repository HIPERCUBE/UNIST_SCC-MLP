import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

commandList = [
    "cd " + CURRENT_PATH,
    "ls"
    "./mlp.x sample.in 50 30 10 1000 1"
]

for command in commandList:
    mlpOpen = os.popen(command)
    mlpRead = mlpOpen.read()
    print(command)
    print(mlpRead)
