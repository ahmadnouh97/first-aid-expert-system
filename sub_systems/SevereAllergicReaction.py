from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Facts - Start

class Breathing(Fact):
    pass


class AdrenalineInjector(Fact):
    pass


# Facts - End

class SevereAllergicReaction(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.checkBreathing
        engine.startEngine()

    def checkBreathing(self):
        instructions.append('Lay the casualty flat.')
        self.reset()
        self.declare(Breathing(input('Is the breathing difficult?\n'
                                     '1- Yes\n'
                                     '2- No\n')))
        self.run()

    @Rule(Breathing('1'))
    def during(self):
        instructions.append('Allow them to sit.')
        self.checkAdrenalineInjector()

    @Rule(Breathing('2'))
    def after(self):
        self.checkAdrenalineInjector()

    def checkAdrenalineInjector(self):
        instructions.append('DO NOT allow them to stand or walk.')
        self.reset()
        self.declare(Breathing(input('Does the casualty carry an adrenaline auto-injector?\n'
                                     '1- Yes\n'
                                     '2- No\n')))
        self.run()

    @Rule(AdrenalineInjector('1'))
    def hasAdrenaline(self):
        instructions.append('Use their injector immediately.')
        self.finish()
        self.onComplete()

    @Rule(AdrenalineInjector('2'))
    def hasNotAdrenaline(self):
        self.finish()
        self.onComplete()

    @staticmethod
    def finish():
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance immediately.')
        instructions.append('If required assist the casualty with an adrenaline auto-injector (EpiPen®).')
        instructions.append('+ Form a firm fist around the EpiPen® and pull off the BLUE SAFETY RELEASE.')
        instructions.append('+ Place ORANGE END against outer mid-thigh at a 90° angle (can be injected through '
                            'clothing).')
        instructions.append('+ Push top button down hard until a click is heard or felt and hold in place for three ('
                            '3) seconds.')
        instructions.append("+ Remove EpiPen® and dispose of it safely being careful of the needle.")
        instructions.append('Commence CPR at any time if the casualty is unresponsive and is not breathing normally.')

    pass
