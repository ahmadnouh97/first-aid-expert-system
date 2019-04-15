from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class RequireSurgery(Fact):
    pass


# Fact - End

class Shock(KnowledgeEngine):

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Lie the casualty down with head flat on floor and reassure. DO NOT raise their legs.')
        instructions.append('Manage any other injury such as bleeding, wounds, burns and immobilise fractures.')
        instructions.append('Maintain the casualty’s body warmth.')
        instructions.append('Loosen any tight clothing.')
        self.reset()
        self.declare(RequireSurgery(input("Is the casualty likely to require any surgery?\n"
                                          "1- Yes\n"
                                          "2- No\n")))
        self.run()

    @Rule(RequireSurgery('1'))
    def conscious(self):
        instructions.append('DO NOT give anything by mouth.')
        self.continueTheRest()
        self.onComplete()

    @Rule(RequireSurgery('2'))
    def unconscious(self):
        instructions.append("Offer clear fluids e.g. small amounts of water frequently.")
        self.continueTheRest()
        self.onComplete()

    @staticmethod
    def continueTheRest():
        instructions.append('Monitor the casualty. DO NOT leave them alone.')
        instructions.append('Place casualty into the Recovery Position if they become unconscious.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
