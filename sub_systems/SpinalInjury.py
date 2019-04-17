from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class Conscious(Fact):
    pass


# Fact - End

class SpinalInjury(KnowledgeEngine):

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
        instructions.append('DO NOT move unless in a dangerous situation.')
        instructions.append('Rest and reassure.')
        instructions.append('Loosen tight clothing.')
        instructions.append('Support and hold head and neck in a neutral position, place hands on either side of the '
                            'casualty’s head to prevent twisting or bending the spine.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        self.onComplete()

    @Rule(Conscious('2'))
    def noConscious(self):
        instructions.append('Reassure the casualty.')
        instructions.append('Place into the recovery position whilst holding the head and spine in a neutral '
                            'position to prevent twisting or bending during movement.')
        instructions.append(
            'Support head and neck in the neutral position place hands on either side of the casualty’s '
            'head to prevent twisting or bending the spine.')
        instructions.append('Maintain a clear and open airway.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        self.onComplete()
