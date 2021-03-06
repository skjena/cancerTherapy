#!/usr/bin/env python
import sys
sys.path.insert(0, "/home/skjena/cancerTherapy/modules/RESTAPI/mutationDnnWeb")
import django
from django.conf import settings
#settings.configure()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mutationDnnWeb.settings")
django.setup()
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RESTAPI.mutationDnnWeb.mutationDnnWeb.settings")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RESTAPI.mutationDnnWeb.mutationDnnWeb.settings")
#django.setup()
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RESTAPI.mutationDnnWeb.mutationDnnWeb.settings")
#import sys
#sys.path.insert(0, "/home/skjena/cancerTherapy/modules")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'RESTAPI.mutationDnnWeb.mutationDnnWeb.settings'
import socket
from Status.Status import Status
from mutationDnnWeb.models import V1, State, Run, Arguments, Features, Settings
from mutationDnnWeb.serializers import V1Serializer, ArgSerializer, StateSerializer, RunSerializer, FeatureSerializer, SettingsSerializer
from typings.network import Network

class RAPIManager():
    def __init__(self):
        self.status = Status("RAPIManager")
        self.djangostatus = self.isRunning()
        self.network = Network()
        self.networkstate = False

    def getArguments(self):
        self.status.message(1, "getArguments(self)")
        model = Arguments.objects.get(id=3)
        self.network.arguments.learningRate = model.learningRate
        self.network.arguments.activation = model.activation
        self.network.arguments.regularization = model.regularization
        self.network.arguments.regularizationRate = model.regularizationRate
        self.network.arguments.problemType = model.problemType
        self.status.message(0, "getArguments(self)")
        return self.network.arguments

    def getState(self):
        self.status.message(1, "getState(self)")
        model = State.objects.get(id=1)
        self.network.state.batchSize = model.batchSize
        self.network.state.noise = model.noise
        self.network.state.trainToTestRatio = model.trainToTestRatio
        self.network.state.numHiddenLayers = model.numHiddenLayers
        self.network.state.networkShape = model.networkShape

        self.status.message(0, "getState(self)")
        return self.network.state

    def getFeatures(self):
        self.status.message(1, "getFeatures(self)")
        model = Features.objects.get(id=1)
        self.network.features.cXa = model.cXa
        self.network.features.cXg = model.cXg
        self.network.features.cXt = model.cXt
        self.network.features.tXa = model.tXa
        self.network.features.tXg = model.tXg
        self.network.features.tXc = model.tXc

        self.status.message(0, "getFeatures(self)")
        return self.network.features

    def getRun(self):
        self.status.message(1, "getRun(self)")
        model = Run.objects.get(id=1)
        self.network.run.reset = model.reset
        self.network.run.play = model.play
        self.network.run.nextButton = model.nextButton
        self.network.run.showTestData = model.showTestData
        self.network.run.discretize = model.discretize

        self.status.message(0, "getRun(self)")
        return self.network.run

    def getSettings(self):
        self.status.message(1, "getSettings(self)")
        model = Settings.objects.get(id=1)
        self.network.settings.dataset = model.dataset
        self.network.settings.weights = model.weights
        self.network.settings.biases = model.biases

        self.status.message(0, "getSettings(self)")
        return self.network.settings

    def populate(self):
        if self.djangostatus == False:
            self.isRunning()
            return self.networkstate

        self.status.message(1, "populate(self)")
        self.network.arguments = self.getArguments()
        self.network.state = self.getState()
        self.network.settings = self.getSettings()
        self.network.features = self.getFeatures()
        self.network.run = self.getRun()
        self.status.message(7)
        self.networkstate = True

        self.status.message(0, "populate(self)")
        return self.networkstate
    def isRunning(self):
        self.status.message(1, "isRunning(self)")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('0.0.0.0',80))
        sock.close()
        if result == 0:
            self.djangostatus = True
            self.status.message(9)
        else:
            self.djangostatus = False
            self.status.message(8)

        self.status.message(0, "isRunning(self)")
        return self.djangostatus

#!/usr/bin/env python
