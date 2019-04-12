from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class Conscious(Fact):
    pass


# Fact - End

class AsthmaAttack(KnowledgeEngine):
    @Rule(Conscious('yes'))
    def conscious(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngineIfConscious
        subEngine.startEngine()

    @Rule(Conscious('no'))
    def noConscious(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngineIfNotConscious
        subEngine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Conscious(input('Is the casualty conscious? (yes / no)')))
        self.run()

    def initEngineIfConscious(self):
        instructions.append('Note: If CPR is required it may be more difficult to get a breath into the '
                            'casualty’s lungs.')
        self.onComplete()

    def initEngineIfNotConscious(self):
        instructions.append('Sit the casualty comfortably upright. Be calm and reassuring and don’t leave the '
                            'casualty alone.')
        instructions.append('Help the casualty to take four (4) puffs from their inhaler following their Asthma '
                            'Action Plan (if they have one).')

        instructions.append('Wait four (4) minutes – if the casualty still cannot breathe normally, give four (4) '
                            'more puffs in the same way.')

        instructions.append('If the casualty gets little or no relief from the inhaler, call Triple Zero (000) '
                            'for an ambulance.')

        instructions.append('Keep giving four (4) puffs every four (4) minutes until medical aid arrives.')

        self.onComplete()
