import os
import parser
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.MLP

for root, dirs, files in os.walk('./result'):
    for file in files:
        fileInfo = file.split(' ')
        data = open(root + '/' + file).read()
        doc = {
            'training': fileInfo[0],
            'testing': fileInfo[1],
            'neuron': fileInfo[2],
            'epochs': fileInfo[3],
            'learningRate': fileInfo[4],
            'result': {
                'train': parser.trainResult(data),
                'test': parser.testResult(data),
                'val': parser.valResult(data),
                'sum': parser.trainResult(data) + parser.testResult(data) + parser.valResult(data)
            }
        }
        print doc
        db.results.insert(doc)
