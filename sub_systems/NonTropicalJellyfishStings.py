from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


class NonTropicalJellyfishStings(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Rest and reassure the casualty.')
        instructions.append('Prevent the casualty from rubbing stung area.')
        instructions.append('Monitor the casualty constantly.')
        instructions.append('Douse affected area with seawater, DO NOT use freshwater.')
        instructions.append('Pick off any remaining tentacles with fingers taking care not to get stung yourself.')
        instructions.append('If possible place the stung area in hot water (no hotter than the first aider can '
                            'tolerate).')
        instructions.append('Medical aid if required.')
        self.onComplete()

    pass
