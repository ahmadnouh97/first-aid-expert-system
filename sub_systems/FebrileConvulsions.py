from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start



# Fact - End

class FebrileConvulsions(KnowledgeEngine):
    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        pass