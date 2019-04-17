from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class Conscious(Fact):
    pass


# Fact - End

class Stroke(KnowledgeEngine):

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Lay the casualty down, rest and reassure.')
        self.reset()
        self.declare(Conscious(input('Is the casualty conscious?\n'
                                     '1- Yes\n'
                                     '2- No\n')))
        self.run()

    @Rule(Conscious('1'))
    def conscious(self):
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        instructions.append('Rest and reassure the casualty.')
        instructions.append('Place in a position of comfort and support the head and shoulders with pillows.')
        instructions.append('Loosen tight clothing.')
        instructions.append('Ensure airway is clear and open and wipe any secretions away from the mouth.')
        instructions.append('Give nothing by mouth.')
        instructions.append('Monitor casualty until medical aid arrives.')
        self.onComplete()

    @Rule(Conscious('2'))
    def noConscious(self):
        instructions.append('Place into Recovery Position.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        self.onComplete()
