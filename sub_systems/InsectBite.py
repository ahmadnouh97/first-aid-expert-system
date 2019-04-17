from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class StingType(Fact):
    pass


# Fact - End

class InsectBite(KnowledgeEngine):
    @Rule(StingType('A'))
    def beeWaspSting(self):
        instructions.append("remove sting by scraping sideways with finger nail or sharp object.")
        self.performExtra()
        self.onComplete()

    @Rule(StingType('B'))
    def tickBite(self):
        instructions.append("If any signs of allergic reaction or casualty has a known allergy - DO NOT remove the "
                            "tick.")
        self.performExtra()
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        self.reset()
        self.declare(StingType(input("A: for bee/wasp bites, B: for Tick Bites:\n")))
        self.run()

    @staticmethod
    def performExtra():
        instructions.append("Apply a cold pack directly over the bite site to relieve pain.")
        instructions.append("Monitor casualty and seek medical aid if necessary.")
        instructions.append("If severe allergic reaction, call Triple Zero (000) for an ambulance. If the casualty is "
                            "carrying their own EpiPen® it should be given immediately.")
