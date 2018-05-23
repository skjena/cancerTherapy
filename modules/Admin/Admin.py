import os
import sys
sys.path.insert(0, "/home/skjena/cancerTherapy/modules")
from multiprocessing import Process, Queue
from CrossValidation.CVManager import CVManager
from DataDispatcher.DDManager import DispatchData
from NeuralNet.management.NNManager import NNManager
import time

class Admin:
    def __init__(self):
        self.status = Status("Admin")
        self.numFolds = 10
        self.rawDb = RDBManager()
        self.restApi = RAPIManager()
        self.DD = DDManager()
        while self.restApi.djangostatus == False:
            self.restApi.isRunning()
        if self.restApi.networkState == False:
            self.restApi.populate()
        self.origin = self.rawDb.GETDATASETFILE(self.restApi.network.settings.dataset)
        self.indexedDb = IDBManager(self.origin, self.numFolds)
        self.foldset = self.indexedDb.createFolds()
        self.crossValidate = CVManager(self.foldset)

    def initialize():
        self.status.message(1,"initialize()")

        #Initialize CVManager Obj
        self.CV = CVManager("/home/skjena/cancerTherapy/modules/RawDB/scripts/fm_mutations_independent.csv", self.numFolds)
        #Call CVManager's CrossValidate function which returns a list of fold-paths
        self.foldList = self.CV.CrossValidate("/home/skjena/cancerTherapy/modules/RawDB/scripts/fm_mutations_independent.csv",self.numFolds)
        
        #Start crossValidation process separately
        self.crossValidate = Process(target=self.CV.validation, args=(self.foldList,self.DDQTesting,self.DDQTraining))
        self.crossValidate.start()
        
        #Pop from testing and training queues until empty and pass paths to NN
        for i in range(1,self.numFolds+1):
            self.dispatchData = Process(target=self.DD.DispatchData)
            self.dispatchData.start()
            self.NN = NNManager(self.trainFold,s

        self.status.message(0,"initialize()")
        return
   
    def build(self):
        self.status.message(1, "build(self)")
        
         
