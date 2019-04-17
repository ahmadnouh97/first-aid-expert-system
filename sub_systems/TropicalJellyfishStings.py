from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class VinegarUnavailable(Fact):
    pass


# Fact - End

class TropicalJellyfishStings(KnowledgeEngine):

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Remove casualty from water.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        instructions.append('Calm casualty.')
        instructions.append('Flood stung area with vinegar for at least thirty (30) seconds.')
        self.reset()
        self.declare(VinegarUnavailable(input('Is vinegar unavailable?\n'
                                              '1- Yes\n'
                                              '2- No\n')))
        self.run()

    @Rule(VinegarUnavailable('1'))
    def conscious(self):
        instructions.append('Flick tentacles off using a stick or gloved fingers and rinse with seawater.\n'
                            '  + DO NOT use freshwater, this will cause further stinging cell discharge.')
        self.continueTheRest()
        self.onComplete()

    @Rule(VinegarUnavailable('2'))
    def noConscious(self):
        self.continueTheRest()
        self.onComplete()

    @staticmethod
    def continueTheRest():
        instructions.append('Apply a cold pack.')
        instructions.append('Rest and reassure, monitor vital signs and consciousness until medical aid arrives.')
        instructions.append('Give CPR if necessary.')
