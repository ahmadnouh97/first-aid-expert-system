from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class StingType(Fact):
    pass


class WoundOnLimb(Fact):
    pass


# Fact - End

class MarineStings(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Rest and reassure the casualty.')
        self.reset()
        self.declare(StingType(input('Please determine the sting\'s type:\n'
                                     '1- Catfish, stonefish, crown-of-thorns starfish\n'
                                     '2- Stingray\n')))
        self.run()

    @Rule(StingType('1'))
    def stingType1(self):
        self.checkWoundOnLimb()
        pass

    @Rule(StingType('2'))
    def stingType2(self):
        instructions.append('Stop any severe bleeding before placing stung part in hot water (no hotter than the '
                            'first aider can tolerate).')
        instructions.append('DO NOT remove the embedded stingray spines.')
        instructions.append('If possible place the stung area in hot water (no hotter than the first aider can '
                            'tolerate).')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        self.onComplete()

    def checkWoundOnLimb(self):
        self.reset()
        self.declare(WoundOnLimb(input('Is the wound on a limb? (yes / no)\n')))
        self.run()
        pass

    @Rule(WoundOnLimb('yes'))
    def woundOnLimb(self):
        instructions.append(
            'Carefully remove any remaining spines or barbs. Clean visible foreign material from the wound.')
        self.remainingInstructionsStingType1()

    @Rule(WoundOnLimb('no'))
    def woundNotOnLimb(self):
        self.remainingInstructionsStingType1()

    def remainingInstructionsStingType1(self):
        instructions.append('If possible place the stung area in hot water (no hotter than the first aider can '
                            'tolerate).')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        self.onComplete()

    pass
