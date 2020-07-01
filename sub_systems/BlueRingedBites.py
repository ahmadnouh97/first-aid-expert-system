from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start
class BiteOnLimp(Fact):
    pass


# Fact - End

class BlueRingedBites(KnowledgeEngine):
    @Rule(BiteOnLimp('1'))
    def bitOnLimp(self):
        instructions.append('apply a firm broad crepe or elasticised roller bandage starting just above the fingers '
                            'or toes, and moving upwards on the bitten limb as far as can be reached and immobilise '
                            'the limb with a splint.')
        instructions.append('Monitor casualty closely for signs of adverse reactions or deterioration.')
        instructions.append('Call the ambulance')
        instructions.append('Prepare to perform cardiopulmonary resuscitation (CPR) if necessary.')
        self.onComplete()

    @Rule(BiteOnLimp('2'))
    def bitIsNotOnLimp(self):
        instructions.append('Monitor casualty closely for signs of adverse reactions or deterioration.')
        instructions.append('Call the ambulance')
        instructions.append('Prepare to perform cardiopulmonary resuscitation (CPR) if necessary.')
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Calm casualty and keep them still.')
        self.checkIfBiteOnLimp()

    def checkIfBiteOnLimp(self):
        self.reset()
        self.declare(BiteOnLimp(input('Is the bite on a limb? \n1- Yes\n2- No\n')))
        self.run()