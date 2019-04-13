from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class PlaceOfInjury(Fact):
    pass


class BloodFlow(Fact):
    pass


# Fact - End
class Dislocation(KnowledgeEngine):

    @Rule(PlaceOfInjury('limp'))
    def limp(self):
        self.checkBloodFlow()

    @Rule(PlaceOfInjury('shoulder'))
    def shoulder(self):
        instructions.append('Support the casualties arm in position of least discomfort.')
        self.onComplete()

    @Rule(PlaceOfInjury('wrist'))
    def wrist(self):
        instructions.append('Apply a sling in a position of comfort.')
        self.onComplete()

    @Rule(BloodFlow('absent'))
    def bloodFlowAbsent(self):
        instructions.append('- Move limb gently to try and restore it.')
        self.performCommonInstruction()
        self.onComplete()

    @Rule(BloodFlow('not'))
    def bloodFlowNotAbsent(self):
        self.performCommonInstruction()
        self.onComplete()

    @staticmethod
    def performCommonInstruction():
        instructions.append('Call the ambulance.')
        instructions.append('Apply icepacks if possible, directly over the joint.')
        instructions.append('Rest and support the limb with padding and bandages.')

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Assist the casualty to sit or lie down in a comfortable position and reassure.')
        instructions.append('DO NOT attempt to put back into position.')
        self.checkPlaceOfInjury()

    def checkPlaceOfInjury(self):
        self.reset()
        self.declare(PlaceOfInjury(input('What is the location of injury? (limp / shoulder / wrist)')))
        self.run()

    def checkBloodFlow(self):
        self.reset()
        self.declare(BloodFlow(input('Check blood flow (absent / not)')))
        self.run()
