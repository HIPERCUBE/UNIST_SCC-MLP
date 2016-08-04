import pylab
import parser

data = open('result.txt').read()

x = parser.parseX(data)

pylab.figure(1)
yTrain = parser.parseTrainError(data)
pylab.title('TRAIN')
pylab.xlabel('epochs')
pylab.ylabel('TRAIN_error')
pylab.plot(x, yTrain)

pylab.figure(2)
yTest = parser.parseTrainError(data)
pylab.title('TEST')
pylab.xlabel('epochs')
pylab.ylabel('TEST_error')
pylab.plot(x, yTest)

pylab.show()