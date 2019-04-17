from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class HeatType(Fact):
    pass


# Fact - End

class HeatInducedConditions(KnowledgeEngine):
    @Rule(HeatType('stroke'))
    def heatStroke(self):
        instructions.append('Apply cool packs or ice to areas of large blood vessels (neck, groin and armpits) to '
                            'speed up cooling.')
        instructions.append('If possible cover with a wet sheet/towel, fan to increase air circulation (stop cooling '
                            'when body is cold to touch). Ensure that the casualty does not get too cold.')
        instructions.append('Give sips of cool fluids if fully conscious and able to swallow.')
        instructions.append('Call the ambulance.')
        self.onComplete()

    @Rule(HeatType('exhaustion'))
    def heatExhaustion(self):
        instructions.append('Sponge with cool water, stop when they feel cool to the touch. Ensure that the casualty '
                            'does not get too cold.')
        instructions.append('Seek medical aid if casualty vomits or does not recover promptly.')
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Stop any activity and rest and reassure the casualty in a cool place with circulating air.')
        instructions.append('Loosen tight clothing and remove unnecessary garments.')
        instructions.append('Give cool fluids to drink - frequent sips.')
        self.checkHeatType()

    def checkHeatType(self):
        self.reset()
        self.declare(HeatType(input('What\'s the type of the heat Induced Conditions? (stroke / exhaustion)')))
        self.run()