from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Facts - Start

class Case(Fact):
    pass


# Facts - End

class Poisoning(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Urgent medical aid required. Call Triple Zero (000) for an ambulance.')
        instructions.append('Call Poisons Information 13 11 26 and/or follow instructions on any containers.')
        instructions.append('Send any vomit, containers or notes with the casualty to hospital.')
        self.determineCasualtyCase()

    def determineCasualtyCase(self):
        pass

    pass