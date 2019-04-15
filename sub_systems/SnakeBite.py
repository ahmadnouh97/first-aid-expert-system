from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class BiteOnLimb(Fact):
    pass


# Fact - End

class SnakeBite(KnowledgeEngine):

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Lay the casualty down, rest and reassure.')
        self.reset()
        self.declare(BiteOnLimb(input('Is the bite on a limb?\n'
                                      '1- Yes\n'
                                      '2- No\n')))
        self.run()

    @Rule(BiteOnLimb('1'))
    def biteOnLimb(self):
        instructions.append('Apply a broad pressure bandage over the bite site as soon as possible.')
        self.continueTheRest()
        self.onComplete()

    @Rule(BiteOnLimb('2'))
    def biteNotOnLimb(self):
        self.continueTheRest()
        self.onComplete()

    @staticmethod
    def continueTheRest():
        instructions.append('Then apply a further elasticised or firm bandage - start at fingers or toes and move up '
                            'the limb as far as can be reached. Apply tightly but without stopping blood flow.')
        instructions.append('Splint the limb including the joints on either side of the bite.')
        instructions.append('Ensure the casualty does not move.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        instructions.append('Write down the time that the casualty was bitten and when the bandage was applied.')
        instructions.append('DO NOT:\n'
                            '+ Wash the venom off the skin (it may aid in identification).\n'
                            '++ Cut the bitten area and try to suck venom out of the wound.\n'
                            '++ Use a tourniquet.\n'
                            '++ Try and catch the snake.\n')
