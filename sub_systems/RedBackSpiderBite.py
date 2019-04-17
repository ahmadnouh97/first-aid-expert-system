from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


class RedBackSpiderBite(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Lay the casualty down, rest and reassure.')
        instructions.append('Monitor the casualty constantly.')
        instructions.append('Apply a cold compress/cold pack to lessen the pain (no longer than twenty (20) minutes).')
        instructions.append('Seek medical aid promptly, if:\n'
                            '  + Person bitten is a young child, elderly or infirmed.\n'
                            '  + The casualty collapses.\n'
                            '  + Pain is severe.')
        self.onComplete()

    pass
